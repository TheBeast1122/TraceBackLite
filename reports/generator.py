from datetime import datetime


def generate_report(timeline, output_file):
    """
    Generate forensic timeline report.

    Args:
        timeline (list): Timeline events
        output_file (str): Report filename

    Returns:
        str
    """

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as report:

        report.write(
            "TRACEBACK LITE FORENSIC REPORT\n"
        )

        report.write(
            "=" * 60 + "\n"
        )

        report.write(
            f"Generated: {datetime.now()}\n\n"
        )

        report.write(
            f"Total Events: {len(timeline)}\n\n"
        )

        report.write(
            "TIMELINE\n"
        )

        report.write(
            "=" * 60 + "\n\n"
        )

        for event in timeline:

            report.write(
                f"{event.get('time')} | "
                f"{event.get('artifact')} | "
                f"{event.get('action')} | "
                f"{event.get('target')}\n"
            )

            details = event.get(
                "details",
                ""
            )

            if details:
                report.write(
                    f"    Details: {details}\n"
                )

        report.write("\n")

        report.write(
            "=" * 60 + "\n"
        )

        report.write(
            "ARTIFACT STATISTICS\n"
        )

        report.write(
            "=" * 60 + "\n"
        )

        stats = {}

        for event in timeline:

            artifact = event.get(
                "artifact",
                "Unknown"
            )

            stats[artifact] = (
                stats.get(
                    artifact,
                    0
                ) + 1
            )

        for artifact, count in stats.items():

            report.write(
                f"{artifact}: {count} events\n"
            )

    return output_file