"""
AEGIS Demonstration Video Generator
Synchronized EXACTLY to Video_Project_4.srt timestamps.
ZERO Overlays. ZERO Timestamps. ZERO Popups. Pure Full HD Native Capture.
"""

import os
import sys
import time
import shutil
import cv2
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")

BASE_URL    = "http://127.0.0.1:5173"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
RAW_DIR     = r"d:\SIH 2026\output_videos\raw_synced"
FINAL_WEBM  = r"d:\SIH 2026\AEGIS_Demo_Walkthrough.webm"
FINAL_MP4   = r"d:\SIH 2026\AEGIS_Demo_Walkthrough.mp4"

# Exact Millisecond Timestamps from Video_Project_4.srt
# Scene transitions occur at these exact elapsed seconds from start of video:
SCENE_TIMESTAMPS = [
    ("Landing Hub",         0.000),   # 00:00:00,000 -> Intro
    ("Institution Portal", 19.931),   # 00:00:19,931 -> "First up is the institution portal..."
    ("Simulated Clock",    41.610),   # 00:00:41,610 -> "Now here's one of my absolute favorite features..."
    ("Scrutiny Officer",   56.578),   # 00:00:56,578 -> "Next, the scrutiny officer's desk..."
    ("Regional Officer",   73.227),   # 00:01:13,227 -> "Switching to the regional officer view..."
    ("Bureau Officer",     86.760),   # 00:01:26,760 -> "At the headquarters level..."
    ("EVC Coordinator",    98.944),   # 00:01:38,944 -> "for physical visits, the EVC coordinator..."
    ("Committee Member",  110.798),   # 00:01:50,798 -> "During appeals, SAC and SHC..."
    ("Compliance Officer",124.503),   # 00:02:04,503 -> "Our compliance officer tracks..."
    ("Senior Authority",  137.581),   # 00:02:17,581 -> "when it reaches the senior AICTE authority..."
    ("System Admin",      152.131),   # 00:02:32,131 -> "System admins get a visual node graph..."
    ("Statutory Auditor", 167.885),   # 00:02:47,885 -> "Finally, the statutory auditor portal..."
    ("Brand Outro",       186.590),   # 00:03:06,590 -> "That's Aegis bringing accountability..."
    ("Video End",         194.070),   # 00:03:14,070 -> End of voiceover
]

os.makedirs(RAW_DIR, exist_ok=True)

# Smooth mouse tracker state
_cur_x = 960.0
_cur_y = 540.0

def smooth_move(page, target_x, target_y, duration=0.45, steps=20):
    """Smooth ease-in-out native mouse cursor motion."""
    global _cur_x, _cur_y
    start_x, start_y = _cur_x, _cur_y
    step_duration = duration / steps
    for i in range(1, steps + 1):
        t = i / steps
        ease = t * t * (3.0 - 2.0 * t)  # smoothstep curve
        cx = start_x + (target_x - start_x) * ease
        cy = start_y + (target_y - start_y) * ease
        page.mouse.move(cx, cy)
        time.sleep(step_duration)
    _cur_x = target_x
    _cur_y = target_y

def smooth_point(page, x, y, hold=1.5, duration=0.45):
    """Moves to (x, y) and pauses to allow viewer to absorb the feature."""
    smooth_move(page, x, y, duration=duration)
    time.sleep(hold)

def smooth_click(page, x, y, hold_after=0.6, duration=0.35):
    """Smooth move to (x, y), native click, and brief hold."""
    smooth_move(page, x, y, duration=duration)
    page.mouse.click(x, y)
    time.sleep(hold_after)

def smooth_click_locator(page, locator, hold_after=0.6, duration=0.35):
    """Locates an element, finds its center coordinates, moves smoothly and clicks."""
    try:
        box = locator.bounding_box()
        if box:
            cx = box["x"] + box["width"] / 2.0
            cy = box["y"] + box["height"] / 2.0
            smooth_move(page, cx, cy, duration=duration)
            page.mouse.click(cx, cy)
            time.sleep(hold_after)
            return True
    except Exception as e:
        print(f"  [warn] click failed: {e}")
    return False

def smooth_scroll(page, target_y):
    page.evaluate(f"window.scrollTo({{top: {target_y}, behavior: 'smooth'}})")
    time.sleep(0.6)

def sleep_until_exact_timestamp(t_start, target_elapsed_seconds):
    """Guarantees the script pauses until the exact millisecond required by SRT."""
    elapsed = time.time() - t_start
    remaining = target_elapsed_seconds - elapsed
    if remaining > 0:
        time.sleep(remaining)
    now = time.time() - t_start
    print(f"  -> Timestamp reached: {now:.2f}s (Target: {target_elapsed_seconds:.2f}s)")


def record_synced_walkthrough():
    with sync_playwright() as p:
        print("[1/3] Initializing Playwright 1080p recording context (Strictly ZERO Overlays)...")
        browser = p.chromium.launch(
            executable_path=CHROME_PATH,
            args=["--start-maximized", "--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=1,
            record_video_dir=RAW_DIR,
            record_video_size={"width": 1920, "height": 1080},
        )
        page = context.new_page()

        # Start master clock
        t_start = time.time()
        print(f"Master Clock Started at t=0.00s\n")

        try:
            # =========================================================================
            # SCENE 1: AEGIS LANDING HUB (Target: 0.000s -> 19.931s)
            # Voiceover: "Hey everyone, welcome to Aegis... Let's jump in. First up is..."
            # =========================================================================
            print(f"[01/13] Scene 1: Landing Hub (0.000s -> 19.931s)")
            page.goto(f"{BASE_URL}/", wait_until="networkidle")
            time.sleep(1.2)

            # Move slowly across AEGIS title & tagline
            smooth_point(page, 728, 120, hold=2.5, duration=0.6)
            smooth_point(page, 728, 195, hold=2.2, duration=0.5)

            # Hover across role cards
            smooth_point(page, 360, 560, hold=1.8, duration=0.5)
            smooth_point(page, 560, 560, hold=1.6, duration=0.4)

            # Point to "Enter Institution Portal" button
            enter_inst_btn = page.locator('button:has-text("Enter Institution Portal")').first
            box = enter_inst_btn.bounding_box()
            if box:
                smooth_point(page, box["x"] + box["width"]/2, box["y"] + box["height"]/2, hold=1.5, duration=0.4)

            # Exact transition to Scene 2 at 19.931s
            sleep_until_exact_timestamp(t_start, 19.931)

            # =========================================================================
            # SCENE 2: ROLE 1 - INSTITUTION PORTAL (Target: 19.931s -> 41.610s)
            # Voiceover: "the institution portal for college principals. Right away they see this compliance health score..."
            # =========================================================================
            print(f"[02/13] Scene 2: Institution Portal (19.931s -> 41.610s)")
            page.goto(f"{BASE_URL}/institution", wait_until="networkidle")
            time.sleep(0.8)

            # Point at Compliance Health Ring (88/100)
            smooth_point(page, 440, 290, hold=3.2, duration=0.5)

            # Point at Urgent Attention Carousel - Lease expiry in 21 days alert
            smooth_point(page, 720, 510, hold=3.2, duration=0.5)

            # Scroll down to My Applications Stepper
            smooth_scroll(page, 460)
            smooth_point(page, 960, 550, hold=2.2, duration=0.4)

            # Scroll up and click "Documents & Lease Vault" tab
            smooth_scroll(page, 0)
            vault_tab = page.locator('button:has-text("Documents & Lease Vault")').first
            smooth_click_locator(page, vault_tab, hold_after=1.2)

            # Point to 30-year lease validity bar
            smooth_point(page, 450, 360, hold=2.5, duration=0.4)

            # Exact transition to Scene 3 at 41.610s
            sleep_until_exact_timestamp(t_start, 41.610)

            # =========================================================================
            # SCENE 3: SIMULATED CLOCK TIME MACHINE (Target: 41.610s -> 56.578s)
            # Voiceover: "Now here's one of my absolute favorite features... Fast forward 7 days. Boom..."
            # =========================================================================
            print(f"[03/13] Scene 3: Simulated Clock (41.610s -> 56.578s)")
            # Point to Simulated Clock Chip in Header
            smooth_point(page, 1200, 23, hold=1.8, duration=0.5)

            # Click "+7d" Button
            plus7_btn = page.locator('button[title*="Fast-forward"]').first
            smooth_click_locator(page, plus7_btn, hold_after=2.0)

            # Click Notification Bell to inspect live reactive alerts
            bell_btn = page.locator('button[title*="Notification"]').first
            smooth_click_locator(page, bell_btn, hold_after=2.8)

            # Close notification drawer
            page.keyboard.press("Escape")
            time.sleep(0.6)

            # Exact transition to Scene 4 at 56.578s
            sleep_until_exact_timestamp(t_start, 56.578)

            # =========================================================================
            # SCENE 4: ROLE 2 - SCRUTINY OFFICER (Target: 56.578s -> 73.227s)
            # Voiceover: "Next, the scrutiny officer's desk. These red and amber heat strips show exactly..."
            # =========================================================================
            print(f"[04/13] Scene 4: Scrutiny Officer (56.578s -> 73.227s)")
            page.goto(f"{BASE_URL}/scrutiny", wait_until="networkidle")
            time.sleep(0.8)

            # Point to Queue item with ageing heat-strip
            smooth_point(page, 320, 240, hold=2.8, duration=0.5)

            # Move across statutory checklist evaluation matrix
            smooth_point(page, 950, 380, hold=3.0, duration=0.5)

            # Click "Case Summary" button to open modal
            summary_btn = page.locator('button:has-text("Case Summary")').first
            smooth_click_locator(page, summary_btn, hold_after=2.8)

            # Close modal with Escape
            page.keyboard.press("Escape")
            time.sleep(0.6)

            # Exact transition to Scene 5 at 73.227s
            sleep_until_exact_timestamp(t_start, 73.227)

            # =========================================================================
            # SCENE 5: ROLE 3 - REGIONAL OFFICER (Target: 73.227s -> 86.760s)
            # Voiceover: "Switching to the regional officer view, they get an interactive heat map of India..."
            # =========================================================================
            print(f"[05/13] Scene 5: Regional Officer (73.227s -> 86.760s)")
            page.goto(f"{BASE_URL}/regional", wait_until="networkidle")
            time.sleep(0.8)

            # Point to India SVG heat map
            smooth_point(page, 660, 320, hold=2.2, duration=0.5)

            # Click Western Region on map
            smooth_click(page, 615, 315, hold_after=1.2, duration=0.35)

            # Switch to "Workload Board" Tab
            workload_tab = page.locator('button:has-text("Workload Board")').first
            smooth_click_locator(page, workload_tab, hold_after=1.8)

            # Point to officer workload swimlanes & reassign button
            smooth_point(page, 850, 380, hold=2.0, duration=0.45)

            # Exact transition to Scene 6 at 86.760s
            sleep_until_exact_timestamp(t_start, 86.760)

            # =========================================================================
            # SCENE 6: ROLE 4 - BUREAU OFFICER (Target: 86.760s -> 98.944s)
            # Voiceover: "At the headquarters level, the Bureau officer watches national trends..."
            # =========================================================================
            print(f"[06/13] Scene 6: Bureau Officer (86.760s -> 98.944s)")
            page.goto(f"{BASE_URL}/bureau", wait_until="networkidle")
            time.sleep(0.8)

            # Point to National Pulse KPI cards
            smooth_point(page, 728, 120, hold=2.2, duration=0.5)

            # Point to comparative regional bar race chart
            smooth_point(page, 728, 380, hold=2.5, duration=0.5)

            # Point to persistent live alerts rail on the right
            smooth_point(page, 1200, 320, hold=2.0, duration=0.5)

            # Exact transition to Scene 7 at 98.944s
            sleep_until_exact_timestamp(t_start, 98.944)

            # =========================================================================
            # SCENE 7: ROLE 5 - EVC COORDINATOR (Target: 98.944s -> 110.798s)
            # Voiceover: "for physical visits, the EVC coordinator has automated conflict of interest guards..."
            # =========================================================================
            print(f"[07/13] Scene 7: EVC Coordinator (98.944s -> 110.798s)")
            page.goto(f"{BASE_URL}/evc", wait_until="networkidle")
            time.sleep(0.8)

            # Point to EVC Scheduling Queue with statutory delay badges
            smooth_point(page, 410, 300, hold=2.0, duration=0.5)

            # Click "Expert Pool & Conflict Guard" tab
            coi_tab = page.locator('button:has-text("Expert Pool & Conflict Guard")').first
            smooth_click_locator(page, coi_tab, hold_after=2.2)

            # Point to conflict-flagged expert row
            smooth_point(page, 728, 320, hold=2.2, duration=0.45)

            # Exact transition to Scene 8 at 110.798s
            sleep_until_exact_timestamp(t_start, 110.798)

            # =========================================================================
            # SCENE 8: ROLE 6 - COMMITTEE MEMBER (Target: 110.798s -> 124.503s)
            # Voiceover: "During appeals, SAC and SHC committee members review digital dossiers..."
            # =========================================================================
            print(f"[08/13] Scene 8: Committee Member (110.798s -> 124.503s)")
            page.goto(f"{BASE_URL}/committee", wait_until="networkidle")
            time.sleep(0.8)

            # Point to hearing agenda queue on the left
            smooth_point(page, 360, 260, hold=2.2, duration=0.5)

            # Click on case dossier
            smooth_click(page, 360, 280, hold_after=1.5, duration=0.35)

            # Point to recommendation editor and time-bound undertakings conditions
            smooth_point(page, 960, 400, hold=2.8, duration=0.5)

            # Exact transition to Scene 9 at 124.503s
            sleep_until_exact_timestamp(t_start, 124.503)

            # =========================================================================
            # SCENE 9: ROLE 7 - COMPLIANCE OFFICER (Target: 124.503s -> 137.581s)
            # Voiceover: "Our compliance officer tracks post approval promises on this 6 stage Kanban board..."
            # =========================================================================
            print(f"[09/13] Scene 9: Compliance Officer (124.503s -> 137.581s)")
            page.goto(f"{BASE_URL}/compliance", wait_until="networkidle")
            time.sleep(0.8)

            # Point across 6-stage undertakings Kanban columns
            smooth_point(page, 350, 350, hold=2.2, duration=0.5)

            # Switch to "Lease & Document Radar" tab
            radar_tab = page.locator('button:has-text("Lease & Document Radar")').first
            smooth_click_locator(page, radar_tab, hold_after=2.0)

            # Point to concentric radar rings (30, 60, 90 days)
            smooth_point(page, 728, 400, hold=2.5, duration=0.5)

            # Exact transition to Scene 10 at 137.581s
            sleep_until_exact_timestamp(t_start, 137.581)

            # =========================================================================
            # SCENE 10: ROLE 8 - SENIOR AUTHORITY (Target: 137.581s -> 152.131s)
            # Voiceover: "when it reaches the senior AICTE authority... strictly enforces typing a statutory reason..."
            # =========================================================================
            print(f"[10/13] Scene 10: Senior Authority (137.581s -> 152.131s)")
            page.goto(f"{BASE_URL}/authority", wait_until="networkidle")
            time.sleep(0.8)

            # Point to Executive Council KPI briefing cards
            smooth_point(page, 728, 160, hold=2.2, duration=0.5)

            # Scroll down to pending decisions shelf
            smooth_scroll(page, 340)
            smooth_point(page, 728, 380, hold=2.0, duration=0.4)

            # Click "Decide (Sign)" button to reveal the mandatory statutory reason requirement modal
            decide_btn = page.locator('button:has-text("Decide (Sign)")').first
            smooth_click_locator(page, decide_btn, hold_after=2.5)

            # Close modal with Escape
            page.keyboard.press("Escape")
            time.sleep(0.5)
            smooth_scroll(page, 0)

            # Exact transition to Scene 11 at 152.131s
            sleep_until_exact_timestamp(t_start, 152.131)

            # =========================================================================
            # SCENE 11: ROLE 9 - SYSTEM ADMINISTRATOR (Target: 152.131s -> 167.885s)
            # Voiceover: "System admins get a visual node graph designer... tune SLA days per stage..."
            # =========================================================================
            print(f"[11/13] Scene 11: System Administrator (152.131s -> 167.885s)")
            page.goto(f"{BASE_URL}/admin", wait_until="networkidle")
            time.sleep(0.8)

            # Move across visual node graph workflow designer canvas
            smooth_point(page, 800, 350, hold=2.2, duration=0.5)
            smooth_point(page, 580, 275, hold=1.6, duration=0.4)
            smooth_point(page, 1000, 420, hold=1.6, duration=0.4)

            # Switch to "SLA & Timeline Rules" in sidebar
            sla_tab = page.locator('button:has-text("SLA & Timeline Rules")').first
            smooth_click_locator(page, sla_tab, hold_after=1.8)

            # Point to SLA threshold sliders
            smooth_point(page, 728, 250, hold=2.5, duration=0.5)

            # Exact transition to Scene 12 at 167.885s
            sleep_until_exact_timestamp(t_start, 167.885)

            # =========================================================================
            # SCENE 12: ROLE 10 - STATUTORY AUDITOR (Target: 167.885s -> 186.590s)
            # Voiceover: "Finally, the statutory auditor portal... cryptographically chained using SHA-256 hashes..."
            # =========================================================================
            print(f"[12/13] Scene 12: Statutory Auditor (167.885s -> 186.590s)")
            page.goto(f"{BASE_URL}/auditor", wait_until="networkidle")
            time.sleep(0.8)

            # Point to SHA-256 hash-chained immutable audit ledger
            smooth_point(page, 728, 280, hold=2.8, duration=0.5)

            # Scroll down to show hash chain column and cryptographic verification
            smooth_scroll(page, 220)
            smooth_point(page, 728, 380, hold=2.4, duration=0.45)
            smooth_scroll(page, 0)

            # Click case row to show Case Provenance Reconstruction Scrubber
            smooth_click(page, 728, 280, hold_after=2.5, duration=0.4)

            # Point to reconstruction timeline scrubber
            smooth_point(page, 728, 450, hold=2.5, duration=0.5)

            # Exact transition to Scene 13 at 186.590s
            sleep_until_exact_timestamp(t_start, 186.590)

            # =========================================================================
            # SCENE 13: BRAND OUTRO & REGULATORY SAFEGUARD (Target: 186.590s -> 194.070s)
            # Voiceover: "That's Aegis bringing accountability, transparency and speed to AICTE approvals. Thank you so much."
            # =========================================================================
            print(f"[13/13] Scene 13: Outro (186.590s -> 194.070s)")
            page.goto(f"{BASE_URL}/", wait_until="networkidle")
            time.sleep(0.8)

            # Slow, authoritative pan over AEGIS logo & regulatory safeguard text
            smooth_point(page, 728, 120, hold=2.5, duration=0.6)
            smooth_point(page, 728, 315, hold=2.5, duration=0.5)

            # Wait for exact end of voiceover at 194.070s
            sleep_until_exact_timestamp(t_start, 194.070)

            print("\n[2/3] Closing context and finalizing recording...")
            context.close()
            browser.close()

        except Exception as exc:
            print(f"\n[ERROR] Walkthrough failed: {exc}")
            try:
                context.close()
                browser.close()
            except Exception:
                pass
            raise

    # =========================================================================
    # STEP 3: Encode WebM to MP4 at 1:1 Natural Speed
    # =========================================================================
    print("\n[3/3] Encoding MP4 with 1:1 Frame Mapping (Zero speedup, zero dropping)...")
    webm_files = [
        os.path.join(RAW_DIR, f)
        for f in os.listdir(RAW_DIR)
        if f.endswith(".webm")
    ]
    if not webm_files:
        print("ERROR: No raw capture webm found!")
        return

    # Pick latest webm file
    webm_files.sort(key=os.path.getmtime, reverse=True)
    raw_webm = webm_files[0]
    shutil.copy2(raw_webm, FINAL_WEBM)

    cap = cv2.VideoCapture(raw_webm)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) or 1920
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or 1080
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total / fps

    print(f"  -> Captured: {total} frames @ {fps:.1f} fps")
    print(f"  -> Final Duration: {duration:.2f}s (~{int(duration//60)}m {int(duration%60):02d}s)")

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(FINAL_MP4, fourcc, fps, (width, height))
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        count += 1
        if count % 500 == 0:
            print(f"    Encoding: {count}/{total} frames ({(count/total)*100:.0f}%)")

    cap.release()
    out.release()

    size_mb = os.path.getsize(FINAL_MP4) / (1024 * 1024)
    print("\n" + "=" * 65)
    print("SUCCESS: PERFECTLY SYNCED AEGIS DEMO VIDEO GENERATED!")
    print(f"  Target Duration:  194.07s (3m 14s)")
    print(f"  Actual Duration:  {duration:.2f}s")
    print(f"  MP4 File:         {FINAL_MP4}")
    print(f"  WebM File:        {FINAL_WEBM}")
    print(f"  Resolution:       {width}x{height} (1080p Full HD)")
    print(f"  File Size:        {size_mb:.2f} MB")
    print("=" * 65)


if __name__ == "__main__":
    record_synced_walkthrough()
