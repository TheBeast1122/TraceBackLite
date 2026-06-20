import winreg
from datetime import datetime


def parse_usb_history():
    """
    Parse USB device history from registry.

    Returns:
        List[dict]
    """

    events = []

    try:

        registry_path = r"SYSTEM\CurrentControlSet\Enum\USBSTOR"

        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            registry_path
        )

        for i in range(
            winreg.QueryInfoKey(key)[0]
        ):

            try:

                device_name = winreg.EnumKey(
                    key,
                    i
                )

                device_key = winreg.OpenKey(
                    key,
                    device_name
                )

                for j in range(
                    winreg.QueryInfoKey(device_key)[0]
                ):

                    try:

                        instance = winreg.EnumKey(
                            device_key,
                            j
                        )

                        events.append({
                            "time": datetime.now(),
                            "artifact": "USB",
                            "source": "Registry",
                            "action": "USB Connected",
                            "target": device_name,
                            "details": instance
                        })

                    except Exception:
                        continue

            except Exception:
                continue

    except Exception:
        pass

    return events