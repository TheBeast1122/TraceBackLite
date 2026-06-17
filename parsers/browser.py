import sqlite3
import shutil
import os
from datetime import datetime, timedelta

def chromium_time_to_datetime(chrome_time):
    return datetime(1601, 1, 1) + timedelta(microseconds=chrome_time)

def parse_chromium_history(history_file, browser_name):
    events = []

    if not os.path.exists(history_file):
        raise FileNotFoundError("History file not found")

    temp_db = f"temp_{browser_name}.db"

    shutil.copy2(history_file, temp_db)

    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT url, title, last_visit_time
        FROM urls
        ORDER BY last_visit_time DESC
        LIMIT 50
    """)

    for url, title, visit_time in cursor.fetchall():
        events.append({
            "time": chromium_time_to_datetime(visit_time),
            "event": f"Visited {url}",
            "source": browser_name
        })

    conn.close()
    os.remove(temp_db)

    return events