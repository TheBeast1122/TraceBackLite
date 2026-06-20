def sort_timeline(events):
    """
    Sort timeline by timestamp.

    Returns:
        List[dict]
    """

    return sorted(
        events,
        key=lambda event: event["time"]
    )