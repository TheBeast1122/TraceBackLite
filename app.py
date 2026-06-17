from parsers.browser import parse_chromium_history
from parsers.timeline import build_timeline
from parsers.hashing import calculate_hashes

BROWSERS = {
    "Brave": r"C:\Users\offic\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\History",
    "Chrome": r"C:\Users\offic\AppData\Local\Google\Chrome\User Data\Default\History",
    "Edge": r"C:\Users\offic\AppData\Local\Microsoft\Edge\User Data\Default\History"
}

all_events = []

print("\n=== TRACEBACK LITE ===\n")

# Load browser history
for browser_name, history_path in BROWSERS.items():

    try:
        events = parse_chromium_history(history_path, browser_name)
        all_events.extend(events)

        print(f"[+] {browser_name}: {len(events)} records loaded")

    except FileNotFoundError:
        print(f"[-] {browser_name}: History file not found")

    except Exception as e:
        print(f"[-] {browser_name}: {e}")

# Build timeline
timeline = build_timeline(all_events)

print("\n=== TRACEBACK TIMELINE ===\n")

for event in timeline[:20]:
    print(
        f"{event['time']} | "
        f"{event['source']} | "
        f"{event['event']}"
    )

# Evidence Hashes
print("\n=== EVIDENCE HASHES ===\n")

for browser_name, history_path in BROWSERS.items():

    try:
        hash_info = calculate_hashes(history_path)

        print(f"\n[{browser_name}]")
        print(f"File: {hash_info['file']}")
        print(f"Size: {hash_info['size']} bytes")
        print(f"MD5: {hash_info['md5']}")
        print(f"SHA256: {hash_info['sha256']}")

    except FileNotFoundError:
        continue

    except Exception as e:
        print(f"Hashing error for {browser_name}: {e}")

print("\n=== ANALYSIS COMPLETE ===")