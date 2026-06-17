from parsers.hashing import calculate_hashes
import hashlib
import os

def calculate_hashes(filepath):
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            md5.update(chunk)
            sha256.update(chunk)

    return {
        "file": os.path.basename(filepath),
        "size": os.path.getsize(filepath),
        "md5": md5.hexdigest(),
        "sha256": sha256.hexdigest()
    }
print("\n=== EVIDENCE HASHES ===\n")

for browser_name, history_path in BROWSERS.items():

    try:
        hash_info = calculate_hashes(history_path)

        print(f"\n[{browser_name}]")
        print(f"File: {hash_info['file']}")
        print(f"Size: {hash_info['size']} bytes")
        print(f"MD5: {hash_info['md5']}")
        print(f"SHA256: {hash_info['sha256']}")

    except:
        pass
    