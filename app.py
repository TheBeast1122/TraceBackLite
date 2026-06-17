from parsers.browser import parse_chromium_history
from parsers.timeline import build_timeline

BROWSERS = {
    "Brave": r"C:\Users\offic\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\History",
    "Chrome": r"C:\Users\offic\AppData\Local\Google\Chrome\User Data\Default\History",
    "Edge": r"C:\Users\offic\AppData\Local\Microsoft\Edge\User Data\Default\History"
}

all_events = []

print("\n=== TRACEBACK LITE ===\n")

for browser_name, history_path in BROWSERS.items():
    try:
        events = parse_chromium_history(history_path, browser_name)
        all_events.extend(events)
        print(f"[+] {browser_name}: {len(events)} records loaded")

    except Exception as e:
        print(f"[-] {browser_name}: {e}")

timeline = build_timeline(all_events)

print("\n=== TRACEBACK TIMELINE ===\n")

for event in timeline[:20]:
    print(
        f"{event['time']} | "
        f"{event['source']} | "
        f"{event['event']}"
    )