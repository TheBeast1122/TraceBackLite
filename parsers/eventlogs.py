import win32evtlog

from datetime import datetime


def parse_eventlogs():
    """
    Parse Windows System Event Log.

    Returns:
        List[dict]
    """

    events = []

    try:

        server = "localhost"
        log_type = "System"

        hand = win32evtlog.OpenEventLog(
            server,
            log_type
        )

        flags = (
            win32evtlog.EVENTLOG_BACKWARDS_READ
            |
            win32evtlog.EVENTLOG_SEQUENTIAL_READ
        )

        total_events = 0

        while total_events < 200:

            records = win32evtlog.ReadEventLog(
                hand,
                flags,
                0
            )

            if not records:
                break

            for record in records:

                total_events += 1

                event_id = record.EventID & 0xFFFF

                if event_id == 6005:
                    action = "System Startup"

                elif event_id == 6006:
                    action = "System Shutdown"

                elif event_id == 1074:
                    action = "System Restart"

                elif event_id == 1:
                    action = "System Event"

                else:
                    action = f"Event ID {event_id}"

                events.append({
                    "time": record.TimeGenerated,
                    "artifact": "Event Log",
                    "source": "Windows",
                    "action": action,
                    "target": log_type,
                    "details": f"Event ID {event_id}"
                })

                if total_events >= 200:
                    break

    except Exception as e:

        print(
            f"Event Log Parser Error: {e}"
        )

    return events