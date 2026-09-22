def load_scorer():
    """Use scorer.py if the student has built it. Otherwise run unscored."""
    try:
        import scorer  # noqa: PLC0415
    except ImportError:
        return None
    judge = getattr(scorer, "judge", None)
    return judge if callable(judge) else None
