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