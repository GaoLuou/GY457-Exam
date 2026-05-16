# -*- coding: utf-8 -*-
"""
GY457 Course Scraper
Opens a browser, waits for user to log in, then scrapes all resources.
Course URL: https://moodle.lse.ac.uk/course/view.php?id=12295
"""

import asyncio
import json
import re
import sys
from pathlib import Path
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

COURSE_URL = "https://moodle.lse.ac.uk/course/view.php?id=12295"
BASE_DIR = Path(__file__).parent
PROFILE_DIR = BASE_DIR / "pw_profile"


async def wait_for_login(page):
    """Block until user is logged into Moodle (course page loaded)."""
    print(">>> Waiting for login...")
    for i in range(180):
        await asyncio.sleep(2)
        try:
            title = await page.title()
            url = page.url
            # Successfully on course page when title does NOT say "Log in"
            if ("Log in" not in title and "login" not in url.lower()
                    and "moodle.lse.ac.uk" in url):
                print(f">>> Logged in! Title: {title}")
                return True
            if i % 15 == 0 and i > 0:
                print(f"    Still waiting... ({i*2}s) - title: {title[:50]}")
        except Exception:
            pass
    return False


async def scrape():
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=False,
            accept_downloads=True,
        )
        page = await context.new_page()

        print(f">>> Opening: {COURSE_URL}")
        await page.goto(COURSE_URL)
        await page.wait_for_load_state("domcontentloaded")
        await asyncio.sleep(2)

        title = await page.title()
        print(f">>> Title: {title}")

        # If on login page, wait for user to log in
        if "Log in" in title or "login" in page.url.lower():
            print("\n=== Please log in to Moodle in the browser window ===")
            print("=== The script will continue automatically after login ===\n")
            logged_in = await wait_for_login(page)
            if not logged_in:
                print(">>> Timeout waiting for login. Exiting.")
                await context.close()
                return
            # Go to course page after login
            await page.goto(COURSE_URL)
            await page.wait_for_load_state("networkidle")
            await asyncio.sleep(3)
        else:
            print(">>> Already logged in!")

        final_title = await page.title()
        print(f">>> Course page: {final_title}")

        # Expand all sections
        print("\n>>> Expanding sections...")
        for sel in ["[data-action='expandall']", ".expandall", "#expandcollapse a"]:
            try:
                btn = await page.query_selector(sel)
                if btn:
                    await btn.click()
                    await asyncio.sleep(2)
                    print(f">>> Clicked expand all ({sel})")
                    break
            except Exception:
                pass

        # Scroll page to trigger lazy loading
        try:
            for scroll in range(1, 5):
                await page.evaluate(f"window.scrollTo(0, document.body.scrollHeight * {scroll}/4)")
                await asyncio.sleep(0.5)
            await page.evaluate("window.scrollTo(0, 0)")
        except Exception:
            pass
        await asyncio.sleep(2)

        # Collect all resource/file links
        print("\n>>> Collecting links...")
        results = []
        existing_urls = set()

        all_links = await page.query_selector_all("a[href]")
        print(f">>> Total <a> elements on page: {len(all_links)}")

        for link in all_links:
            try:
                href = await link.get_attribute("href") or ""
                text = (await link.inner_text()).strip()
                text = re.sub(r'\s+', ' ', text).strip()

                is_pf = "pluginfile.php" in href
                is_act = any(x in href for x in [
                    "mod/resource/view", "mod/url/view",
                    "mod/folder/view", "mod/page/view"
                ])

                if not (is_pf or is_act):
                    continue
                if href in existing_urls:
                    continue
                if not text:
                    text = href.split("/")[-1].replace("%20", " ")

                # Get section name from DOM
                section_name = await link.evaluate(
                    """el => {
                        let node = el;
                        while (node && node !== document.body) {
                            node = node.parentElement;
                            if (!node) break;
                            const cls = node.className || '';
                            if (cls.includes('section') || cls.includes('course-section') ||
                                node.getAttribute('data-for') === 'section' ||
                                node.hasAttribute('data-sectionid')) {
                                const h = node.querySelector(
                                    '.section-title a, .sectionname, h3, h4, .section_title');
                                if (h) return h.innerText.trim().replace(/\\s+/g, ' ').slice(0, 80);
                            }
                        }
                        return 'Other';
                    }"""
                )

                rtype = "pluginfile" if is_pf else "activity"
                results.append({
                    "section": section_name,
                    "name": text,
                    "url": href,
                    "type": rtype
                })
                existing_urls.add(href)
                print(f"  [{section_name[:32]}] {text[:52]}")
            except Exception:
                pass

        print(f"\n>>> Total resources: {len(results)}")

        # Resolve activity pages -> direct download URLs
        act = [r for r in results if r["type"] == "activity"]
        if act:
            print(f"\n>>> Resolving {len(act)} activity pages...")
            for item in act:
                try:
                    await page.goto(item["url"])
                    await page.wait_for_load_state("networkidle")
                    await asyncio.sleep(1)
                    links = await page.query_selector_all("a[href*='pluginfile']")
                    if links:
                        item["direct_url"] = await links[0].get_attribute("href")
                        print(f"  OK: {item['name'][:55]}")
                    elif "pluginfile" in page.url:
                        item["direct_url"] = page.url
                        print(f"  OK(redir): {item['name'][:55]}")
                    else:
                        print(f"  --: {item['name'][:55]}")
                except Exception as e:
                    print(f"  [!] {item['name'][:40]}: {e}")

        # Save
        out = BASE_DIR / "scraped_links.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\nDone! Saved {len(results)} resources -> {out}")

        await context.close()


if __name__ == "__main__":
    asyncio.run(scrape())
