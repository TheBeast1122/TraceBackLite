import os

from parsers.browser import parse_chromium_history
from parsers.downloads import parse_downloads
from parsers.prefetch import parse_prefetch
from parsers.usb import parse_usb_history
from parsers.recyclebin import parse_recyclebin
from parsers.eventlogs import parse_eventlogs

from reports.generator import generate_report
from reports.csv_export import export_csv

from timeline.merger import merge_timelines
from timeline.sorter import sort_timeline

BROWSERS = {
"Chrome": os.path.expandvars(
r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\History"
),
"Edge": os.path.expandvars(
r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\History"
),
"Brave": os.path.expandvars(
r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Default\History"
)
}

def main():

```
os.makedirs("output", exist_ok=True)

print("\n===================================")
print("      TRACEBACK LITE v1")
print("===================================\n")

browser_events = []
download_events = []

for browser_name, history_path in BROWSERS.items():

    print(f"[+] Processing {browser_name}")

    try:
        browser_events.extend(
            parse_chromium_history(
                history_path,
                browser_name
            )
        )

        download_events.extend(
            parse_downloads(
                history_path,
                browser_name
            )
        )

    except Exception as e:
        print(f"[-] {browser_name}: {e}")

try:
    print("[+] Processing Prefetch")
    prefetch_events = parse_prefetch()
except Exception as e:
    print(f"[-] Prefetch Error: {e}")
    prefetch_events = []

try:
    print("[+] Processing USB History")
    usb_events = parse_usb_history()
except Exception as e:
    print(f"[-] USB Error: {e}")
    usb_events = []

try:
    print("[+] Processing Recycle Bin")
    recycle_events = parse_recyclebin()
except Exception as e:
    print(f"[-] Recycle Bin Error: {e}")
    recycle_events = []

try:
    print("[+] Processing Event Logs")
    eventlog_events = parse_eventlogs()
except Exception as e:
    print(f"[-] Event Log Error: {e}")
    eventlog_events = []

all_events = merge_timelines(
    browser_events,
    download_events,
    prefetch_events,
    usb_events,
    recycle_events,
    eventlog_events
)

timeline = sort_timeline(all_events)

print("\n========== UNIFIED TIMELINE ==========\n")

for event in timeline[:500]:
    try:
        print(
            f"{event.get('time', '')} | "
            f"{event.get('artifact', '')} | "
            f"{event.get('action', '')} | "
            f"{event.get('target', '')}"
        )
    except Exception:
        pass

print(f"\n[+] Total Events: {len(timeline)}")

report_path = os.path.join(
    "output",
    "traceback_report.txt"
)

generate_report(
    timeline,
    report_path
)

print(f"[+] Report Saved: {report_path}")

csv_path = os.path.join(
    "output",
    "timeline.csv"
)

export_csv(
    timeline,
    csv_path
)

print(f"[+] CSV Saved: {csv_path}")

print("\n=== ANALYSIS COMPLETE ===")
```

if **name** == "**main**":
main()
import os

from parsers.browser import parse_chromium_history
from parsers.downloads import parse_downloads
from parsers.prefetch import parse_prefetch
from parsers.usb import parse_usb_history
from parsers.recyclebin import parse_recyclebin
from parsers.eventlogs import parse_eventlogs

from reports.generator import generate_report
from reports.csv_export import export_csv

from timeline.merger import merge_timelines
from timeline.sorter import sort_timeline


BROWSERS = {
    "Chrome": os.path.expandvars(
        r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\History"
    ),
    "Edge": os.path.expandvars(
        r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\History"
    ),
    "Brave": os.path.expandvars(
        r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Default\History"
    )
}


def main():

    os.makedirs("output", exist_ok=True)

    print("\n===================================")
    print("      TRACEBACK LITE v1")
    print("===================================\n")

    browser_events = []
    download_events = []

    # Browser History
    for browser_name, history_path in BROWSERS.items():

        print(f"[+] Processing {browser_name}")

        try:
            browser_events.extend(
                parse_chromium_history(
                    history_path,
                    browser_name
                )
            )

            download_events.extend(
                parse_downloads(
                    history_path,
                    browser_name
                )
            )

        except Exception as e:
            print(f"[-] {browser_name}: {e}")

    # Prefetch
    try:
        print("[+] Processing Prefetch")
        prefetch_events = parse_prefetch()

    except Exception as e:
        print(f"[-] Prefetch Error: {e}")
        prefetch_events = []

    # USB
    try:
        print("[+] Processing USB History")
        usb_events = parse_usb_history()

    except Exception as e:
        print(f"[-] USB Error: {e}")
        usb_events = []

    # Recycle Bin
    try:
        print("[+] Processing Recycle Bin")
        recycle_events = parse_recyclebin()

    except Exception as e:
        print(f"[-] Recycle Bin Error: {e}")
        recycle_events = []

    # Event Logs
    try:
        print("[+] Processing Event Logs")
        eventlog_events = parse_eventlogs()

    except Exception as e:
        print(f"[-] Event Log Error: {e}")
        eventlog_events = []

    # Merge all events
    all_events = merge_timelines(
        browser_events,
        download_events,
        prefetch_events,
        usb_events,
        recycle_events,
        eventlog_events
    )

    # Sort timeline
    timeline = sort_timeline(all_events)

    print("\n========== UNIFIED TIMELINE ==========\n")

    for event in timeline[:500]:
        try:
            print(
                f"{event.get('time', '')} | "
                f"{event.get('artifact', '')} | "
                f"{event.get('action', '')} | "
                f"{event.get('target', '')}"
            )
        except Exception:
            pass

    print(f"\n[+] Total Events: {len(timeline)}")
    print(f"[+] Browser Events: {len(browser_events)}")
    print(f"[+] Download Events: {len(download_events)}")
    print(f"[+] Prefetch Events: {len(prefetch_events)}")
    print(f"[+] USB Events: {len(usb_events)}")
    print(f"[+] Recycle Events: {len(recycle_events)}")
    print(f"[+] Event Log Events: {len(eventlog_events)}")

    # Artifact Counts
    print("\n===== ARTIFACT COUNTS IN TIMELINE =====")

    counts = {}

    for event in timeline:
        artifact = event.get("artifact", "Unknown")
        counts[artifact] = counts.get(artifact, 0) + 1

    for artifact, count in counts.items():
        print(f"{artifact}: {count}")

    # TXT Report
    report_path = os.path.join(
        "output",
        "traceback_report.txt"
    )

    generate_report(
        timeline,
        report_path
    )

    print(f"[+] Report Saved: {report_path}")

    # CSV Report
    csv_path = os.path.join(
        "output",
        "timeline.csv"
    )

    export_csv(
        timeline,
        csv_path
    )

    print(f"[+] CSV Saved: {csv_path}")

    print("\n=== ANALYSIS COMPLETE ===")


if __name__ == "__main__":
    main()