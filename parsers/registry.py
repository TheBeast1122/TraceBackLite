import winreg
from datetime import datetime


USERASSIST_PATH = (
    r"Software\Microsoft\Windows\CurrentVersion"
    r"\Explorer\UserAssist"
)


def parse_userassist():
    """
    Parse UserAssist registry entries.

    Returns:
        List[dict]
    """

    events = []

    try:

        root = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            USERASSIST_PATH
        )

        guid_count = winreg.QueryInfoKey(root)[0]

        for i in range(guid_count):

            guid = winreg.EnumKey(root, i)

            try:

                count_key = winreg.OpenKey(
                    root,
                    f"{guid}\\Count"
                )

                value_count = winreg.QueryInfoKey(
                    count_key
                )[1]

                for j in range(value_count):

                    try:

                        value_name, value_data, _ = (
                            winreg.EnumValue(
                                count_key,
                                j
                            )
                        )

                        events.append({
                            "time": datetime.now(),
                            "artifact": "Registry",
                            "source": "UserAssist",
                            "action": "Program Recorded",
                            "target": value_name,
                            "details": ""
                        })

                    except Exception:
                        continue

            except Exception:
                continue

    except FileNotFoundError:
        pass

    return events