import sqlite3
import shutil
import os
from datetime import datetime, timedelta


def chromium_time_to_datetime(chrome_time):
    """
    Convert Chromium timestamp to Python datetime.
    """
    return datetime(1601, 1, 1) + timedelta(
        microseconds=chrome_time
    )


def parse_downloads(history_file, browser_name):
    """
    Parse Chromium downloads.

    Returns:
        List[dict]
    """

    events = []

    if not os.path.exists(history_file):
        raise FileNotFoundError(
            f"History file not found: {history_file}"
        )

    temp_db = f"temp_downloads_{browser_name}.db"

    try:

        shutil.copy2(history_file, temp_db)

        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                target_path,
                start_time
            FROM downloads
            ORDER BY start_time DESC
        """)

        rows = cursor.fetchall()

        for target_path, start_time in rows:

            try:

                if not target_path:
                    continue

                filename = os.path.basename(
                    target_path
                )

                events.append({
                    "time": chromium_time_to_datetime(
                        start_time
                    ),
                    "artifact": "Download",
                    "source": browser_name,
                    "action": "Downloaded",
                    "target": filename,
                    "details": target_path
                })

            except Exception:
                continue

        conn.close()

    finally:

        if os.path.exists(temp_db):
            os.remove(temp_db)

    return events