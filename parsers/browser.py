import sqlite3
import shutil
import os
from datetime import datetime, timedelta


def chromium_time_to_datetime(chrome_time):
    """
    Convert Chromium timestamp to Python datetime.
    """
    return datetime(1601, 1, 1) + timedelta(microseconds=chrome_time)


def classify_browser_activity(url):
    """
    Convert raw URLs into meaningful forensic actions.
    """

    url = url.lower()

    if "facebook.com" in url:
        return "Opened Facebook Profile"

    elif "linkedin.com" in url:
        return "Viewed LinkedIn Profile"

    elif "instagram.com" in url:
        return "Viewed Instagram Profile"

    elif "tomba.io" in url:
        return "Reverse Email Lookup"

    elif "intelx.io" in url:
        return "OSINT Search"

    elif "emailsherlock.com" in url:
        return "Reverse Email Lookup"

    elif "mailmeteor.com" in url:
        return "Reverse Email Lookup"

    elif "search.yahoo.com" in url:
        return "Web Search"

    elif "google.com/search" in url:
        return "Web Search"

    elif "bing.com/search" in url:
        return "Web Search"

    elif "search.brave.com" in url:
        return "Web Search"

    return "Visited Website"


def parse_chromium_history(history_file, browser_name):
    """
    Parse Chromium browser history.

    Returns:
        List[dict]
    """

    events = []

    if not os.path.exists(history_file):
        raise FileNotFoundError(
            f"History file not found: {history_file}"
        )

    temp_db = f"temp_{browser_name}.db"

    try:

        shutil.copy2(history_file, temp_db)

        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                url,
                title,
                last_visit_time
            FROM urls
            ORDER BY last_visit_time DESC
        """)

        rows = cursor.fetchall()

        for url, title, visit_time in rows:

            try:

                action = classify_browser_activity(url)

                events.append({
                    "time": chromium_time_to_datetime(
                        visit_time
                    ),
                    "artifact": "Browser",
                    "source": browser_name,
                    "action": action,
                    "target": url,
                    "details": title
                })

            except Exception:
                continue

        conn.close()

    finally:

        if os.path.exists(temp_db):
            os.remove(temp_db)

    return events