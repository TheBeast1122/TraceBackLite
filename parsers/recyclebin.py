import os
from datetime import datetime

RECYCLE_BIN_PATH = r"C:\$Recycle.Bin"


def parse_recyclebin():
    """
    Parse Windows Recycle Bin.

    Returns:
        List[dict]
    """

    events = []

    if not os.path.exists(RECYCLE_BIN_PATH):
        return events

    try:

        for sid in os.listdir(
            RECYCLE_BIN_PATH
        ):

            sid_path = os.path.join(
                RECYCLE_BIN_PATH,
                sid
            )

            if not os.path.isdir(
                sid_path
            ):
                continue

            for item in os.listdir(
                sid_path
            ):

                try:

                    if not item.startswith("$R"):
                        continue

                    full_path = os.path.join(
                        sid_path,
                        item
                    )

                    deleted_time = (
                        datetime.fromtimestamp(
                            os.path.getmtime(
                                full_path
                            )
                        )
                    )

                    events.append({
                        "time": deleted_time,
                        "artifact": "Recycle Bin",
                        "source": "Windows",
                        "action": "Deleted",
                        "target": item,
                        "details": full_path
                    })

                except Exception:
                    continue

    except Exception:
        pass

    return events