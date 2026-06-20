import os
from datetime import datetime

PREFETCH_PATH = r"C:\Windows\Prefetch"


def parse_prefetch():
    """
    Parse Windows Prefetch files.

    Returns:
        List[dict]
    """

    events = []

    if not os.path.exists(PREFETCH_PATH):
        return events

    try:

        for filename in os.listdir(PREFETCH_PATH):

            if not filename.endswith(".pf"):
                continue

            full_path = os.path.join(
                PREFETCH_PATH,
                filename
            )

            try:

                modified_time = datetime.fromtimestamp(
                    os.path.getmtime(full_path)
                )

                exe_name = filename.split("-")[0]

                events.append({
                    "time": modified_time,
                    "artifact": "Prefetch",
                    "source": "Windows",
                    "action": "Program Executed",
                    "target": exe_name,
                    "details": full_path
                })

            except Exception:
                continue

    except Exception:
        pass

    return events