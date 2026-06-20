def merge_timelines(*timelines):
    """
    Merge multiple event lists.

    Returns:
        List[dict]
    """

    merged = []

    for timeline in timelines:

        if timeline:
            merged.extend(
                timeline
            )

    return merged