def build_timeline(events):
    return sorted(events, key=lambda x: x["time"], reverse=True)