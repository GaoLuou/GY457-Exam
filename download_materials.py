# -*- coding: utf-8 -*-
"""
GY457 Material Downloader
Run this script to download all course materials from LSE Moodle.
The browser profile from scrape_course.py is reused (login remembered).
"""

import asyncio
import sys
from pathlib import Path
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).parent
PROFILE_DIR = BASE_DIR / "pw_profile"

# ──────────────────────────────────────────────────────────────
# AT 2025 Lecture Slides (Autumn Term)
# ──────────────────────────────────────────────────────────────
AT_LECTURES = [
    ("AT_Topic0_Intro.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5036747/mod_resource/content/1/GY457%20AT%202025%20Topic%200.pdf"),
    ("AT_Topic1_Urban_Systems.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5036977/mod_resource/content/1/GY457%20AT%202025%20Topic%201.pdf"),
    ("AT_Topic2_Agglomeration.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378499/mod_resource/content/3/GY457%20AT%202025%20Topic%202.pdf"),
    ("AT_Topic3_Labour_Markets.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378523/mod_resource/content/2/GY457%20AT%202025%20Topic%203.pdf"),
    ("AT_Topic4_Housing_Supply.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378562/mod_resource/content/3/GY457%20AT%202025%20Topic%204.pdf"),
    ("AT_Topic5_Monocentric_City.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378595/mod_resource/content/2/GY457%20AT%202025%20Topic%205.pdf"),
    ("AT_Topic5_with_Solutions.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378600/mod_resource/content/2/GY457%20AT%202025%20Topic%205_with_solutions.pdf"),
    ("AT_Topic6_Edge_Cities.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378625/mod_resource/content/3/GY457%20AT%202025%20Topic%206.pdf"),
    ("AT_Topic7_Gentrification.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378691/mod_resource/content/4/GY457%20AT%202025%20Topic%207.pdf"),
    ("AT_Topic8_House_Prices.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378657/mod_resource/content/5/GY457%20AT%202025%20Topic%208.pdf"),
    ("AT_Topic9_Gentrification_II.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378719/mod_resource/content/3/GY457%20AT%202025%20Topic%209.pdf"),
    ("AT_Topic9_with_Solutions.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5727320/mod_resource/content/1/GY457%20AT%202025%20Topic%209_with_solutions.pdf"),
    ("AT_Topic10.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378730/mod_resource/content/3/GY457%20AT%202025%20Topic%2010.pdf"),
]

# ──────────────────────────────────────────────────────────────
# WT 2026 Lecture Slides (Winter Term)
# ──────────────────────────────────────────────────────────────
WT_LECTURES = [
    ("WT_Topic1_Handout.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5755069/mod_resource/content/0/GY457_2026_WT_Topic%201_Handout%20v1.pdf"),
    ("WT_Topic1_Complete.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5755070/mod_resource/content/1/GY457_2026_WT_Topic%201_Complete%20lecture%20v1.pdf"),
    ("WT_Topic2_Handout.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5757343/mod_resource/content/0/GY457_2026_WT_Topic%202_Handout%20v1.pdf"),
    ("WT_Topic2_Complete.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5757342/mod_resource/content/0/GY457_2026_WT_Topic%202_Complete%20lecture%20v1.pdf"),
    ("WT_Topic3_Handout.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5762392/mod_resource/content/0/GY457_2026_WT_Topic%203_Handout%20v1.pdf"),
    ("WT_Topic3_Complete.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5762393/mod_resource/content/0/GY457_2026_WT_Topic%203_Complete%20lecture%20v1.pdf"),
    ("WT_Topic4_Handout.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5766101/mod_resource/content/0/GY457_2026_WT_Topic%204_Handout%20%20v1.pdf"),
    ("WT_Topic4_Complete.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5766100/mod_resource/content/0/GY457_2026_WT_Topic%204_Complete%20lecture%20v1.pdf"),
    ("WT_Topic5_Handout.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5771919/mod_resource/content/0/GY457_2026_WT_Topic%205_Handout%20v1.pdf"),
    ("WT_Topic6_Handout.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5780226/mod_resource/content/0/GY457_2026_WT_Topic%206_Handout%20%20v1.pdf"),
    ("WT_Topic6_Complete.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5780225/mod_resource/content/0/GY457_2026_WT_Topic%206_Complete%20lecture%20v1.pdf"),
    ("WT_Topic7_Handout.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5781088/mod_resource/content/0/GY457_2026_WT_Topic%207_Handout%20v1.pdf"),
    ("WT_Topic7_Complete.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5781087/mod_resource/content/0/GY457_2026_WT_Topic%207_Complete%20lecture%20v1.pdf"),
    ("WT_Topic8_Handout.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5780782/mod_resource/content/0/GY457_WT2026_Topic8_handout.pdf"),
    ("WT_Topic8_Complete.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5780783/mod_resource/content/0/GY457_WT2026_Topic8_full%20topic%20notes.pdf"),
]

# ──────────────────────────────────────────────────────────────
# Seminars
# ──────────────────────────────────────────────────────────────
SEMINARS = [
    # AT 2025 Seminars
    ("AT_Seminar1.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5059315/mod_resource/content/1/GY457%20SEMINAR%20Topic%201.pdf"),
    ("AT_Seminar2.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378497/mod_resource/content/2/GY457%20SEMINAR%20Topic%202.pdf"),
    ("AT_Seminar5.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378597/mod_resource/content/2/GY457%20SEMINAR%20Topic%205.pdf"),
    ("AT_Seminar6.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378628/mod_resource/content/2/GY457%20SEMINAR%20Topic%206.pdf"),
    ("AT_Seminar7.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378685/mod_resource/content/4/GY457%20SEMINAR%20Topic%207.pdf"),
    ("AT_Seminar8.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378661/mod_resource/content/2/GY457%20SEMINAR%20Topic%208.pdf"),
    ("AT_Seminar9.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378715/mod_resource/content/2/GY457%20SEMINAR%20Topic%209.pdf"),
    # WT 2026 Seminars
    ("WT_Seminar1_Debate.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5754164/mod_resource/content/0/GY457%20Seminar%201%20%28w3%29%20-%20Debate%20-%202026_WT%20Gr%20A1%20%20A2%20.pdf"),
    ("WT_Seminar2_Debate.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5754168/mod_resource/content/0/GY457%20Seminar%202%20%28w4%29%20-%20Debate%20-%202026_WT%20Gr%20A1%20%20A2.pdf"),
    ("WT_Seminar3_Problem_Set.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5754172/mod_resource/content/0/GY457%20Seminar%203%20%28w5%29%20-%20Problem%20Set%20-%202026_WT%20%28briefing%20for%20all%20sub-groups%29.pdf"),
    ("WT_Seminar4_Cities_Presentations.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5754176/mod_resource/content/0/GY457%20Seminar%204%20%28w8%29%20-%20Group%20presentations%20%28Cities%20around%20the%20world%29%20-%20WT%202026%20%28Briefing%20for%20all%20sub-groups%29.pdf"),
    ("WT_Seminar5_Past_Exam.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5754250/mod_resource/content/0/GY457%20Seminar%205%20%28w9%29%20-%20Past%20exam%20question%20-%202026%20WT%20%28briefing%20for%20all%20sub-groups%29.pdf"),
    ("WT_Seminar5_Lecturer_Comments.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5783606/mod_resource/content/0/GY457%20Seminar%205%20%28w9%29%20Lecturer%20comments%20-%202026%20WT%20v2.pdf"),
    ("WT_Seminar6_Key_Papers.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5754325/mod_resource/content/0/GY457%20Seminar%206%20%28w10%29%20-%20Key%20paper%20presentations%20-%202026%20WT%20%28briefing%20for%20presenters%20and%20all%29.pdf"),
    ("WT_Seminar3_Bartik_Explained.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5754173/mod_resource/content/1/GY457%20Seminar%203%20%28Addon%202%29%20Bartik%20explained.pdf"),
]

# ──────────────────────────────────────────────────────────────
# Extra Readings / Supplementary Materials
# ──────────────────────────────────────────────────────────────
EXTRA_READINGS = [
    ("DiPasquale_Wheaton_1996_Ch01.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378442/mod_resource/content/1/%5B01_01%5D%20DiPasquale%20%20Wheaton%201996%20Ch01.pdf"),
    ("Krugman_1991_Geography_Trade_Ch02.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378478/mod_resource/content/0/%5B22%5D%20Krugman%201991%20Geography%20and%20Trade%20-%20Ch02.pdf"),
    ("Gentrification_Economists_Planners.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378706/mod_resource/content/2/Gentrification-%20Perspectives%20of%20Economists%20and%20Planners%20.pdf"),
    ("Extra_Notes_IV.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378503/mod_resource/content/1/Extra_%20Intro%20to%20IV.pdf"),
    ("Guardian_Oxford_Housing_2014.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378828/mod_resource/content/2/The%20Guardian%20on%20Oxford%202014-03.pdf"),
    ("Estimating_Supply_Elasticity_Q_unknown.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378833/mod_resource/content/1/Estimating_Supply_Elasticity_when_Q_is_NA.pdf"),
    ("House_Price_Capitalization_Explained.xlsx",
     "https://moodle.lse.ac.uk/pluginfile.php/4378754/mod_resource/content/1/Explaining%20the%20extent%20of%20house%20price%20capitaliation.xlsx"),
    ("Tulip_Bubble_History_2000.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378947/mod_resource/content/1/The%20Tulip%20Bubble%20History%20Business%20Week%202000-04.pdf"),
    ("Agglomeration_Crossword.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/4378482/mod_resource/content/3/Agglomeration%20Crossword.pdf"),
]

# ──────────────────────────────────────────────────────────────
# Revision Materials
# ──────────────────────────────────────────────────────────────
REVISION = [
    ("Revision_Lecture_Part2.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5789649/mod_resource/content/0/Revision%202025-26%20GY457lecho%20v4%20incl.%20mock%20exam%20feedback%20%28Part%202%29.pdf"),
    ("Mock_Exam_Feedback_Part1.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5789191/mod_resource/content/0/GY457%202025_26%20Mock%20exam%20feedback%20%28Part%201%29.pdf"),
    ("Marking_Criteria_2025_26.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5735149/mod_resource/content/0/Marking%20criteria%20for%20GY457%20Exam%20Paper%20for%202025-6%20cohort%20%28and%20beyond%29.pdf"),
    ("Syllabus_AT2025.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5004362/mod_resource/content/1/GY457_AT2025_syllabus.pdf"),
    ("Syllabus_WT2026.pdf",
     "https://moodle.lse.ac.uk/pluginfile.php/5757337/mod_resource/content/0/GY%20457%20Syllabus%20WT%202026%20-%20Blocks%20I-III%20v2.pdf"),
    ("Pre_Mock_Guide.mp4",
     "https://moodle.lse.ac.uk/pluginfile.php/5767417/mod_resource/content/0/GY457%20Pre-mock%20guide.mp4"),
]

FILES = {
    "lectures": AT_LECTURES,
    "wt-lectures": WT_LECTURES,
    "seminars": SEMINARS,
    "extra-readings": EXTRA_READINGS,
    "revision-materials": REVISION,
}


async def download_all():
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=False,
            accept_downloads=True,
        )
        page = await context.new_page()

        # Quick login check
        await page.goto("https://moodle.lse.ac.uk/course/view.php?id=12295")
        await page.wait_for_load_state("networkidle")
        title = await page.title()

        if "Log in" in title:
            print("Please log in to Moodle in the browser. Waiting...")
            for _ in range(120):
                await asyncio.sleep(2)
                t = await page.title()
                if "Log in" not in t:
                    print("Logged in!")
                    break

        total = sum(len(v) for v in FILES.values())
        done = 0

        for folder, file_list in FILES.items():
            target_dir = BASE_DIR / folder
            target_dir.mkdir(exist_ok=True)

            for filename, url in file_list:
                target_path = target_dir / filename
                if target_path.exists():
                    print(f"  [skip] {filename}")
                    done += 1
                    continue

                try:
                    async with context.expect_download(timeout=60_000) as dl_info:
                        await page.goto(url)
                    download = await dl_info.value
                    await download.save_as(target_path)
                    done += 1
                    print(f"  [{done}/{total}] {filename}")
                except Exception as e:
                    print(f"  [FAIL] {filename}: {e}")

        await context.close()
        print(f"\nDone! Files saved in: {BASE_DIR}")


if __name__ == "__main__":
    asyncio.run(download_all())
