
from datetime import datetime, date


def filter_logs(
    parsed_logs,
    level=None,
    keyword=None,
    filter_date=None,
):
    """Filter parsed logs by level, keyword, and date."""

    filtered_logs = []

    if isinstance(filter_date, str):
        try:
            filter_date = date.fromisoformat(filter_date)
        except ValueError:
            raise ValueError("Date must use YYYY-MM-DD format.")

    if filter_date is not None and not isinstance(filter_date, date):
        raise TypeError("filter_date must be a date or YYYY-MM-DD string.")

    if level is not None:
        level = level.upper()

        if level not in {"INFO", "WARNING", "ERROR"}:
            raise ValueError("Invalid log level.")

    if keyword is not None:
        keyword = keyword.casefold()

    for log in parsed_logs:
        if level is not None and log["level"] != level:
            continue

        if keyword is not None and keyword not in log["message"].casefold():
            continue

        if filter_date is not None:
            timestamp = log["timestamp"]

            if isinstance(timestamp, datetime):
                timestamp = timestamp.date()

            if timestamp != filter_date:
                continue

        filtered_logs.append(log)

    return filtered_logs
