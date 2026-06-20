import csv


def export_csv(timeline, filename="timeline.csv"):

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Time",
            "Artifact",
            "Action",
            "Target"
        ])

        for event in timeline:

            writer.writerow([
                event.get("time", ""),
                event.get("artifact", ""),
                event.get("action", ""),
                event.get("target", "")
            ])

    return filename