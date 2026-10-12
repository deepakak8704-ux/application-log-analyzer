
import re
from datetime import datetime


LOG_PATTERN = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"(INFO|WARNING|ERROR) (.+)$"
)


def parse_log_line(line):
    """Parse one log line into a dictionary."""

    match = LOG_PATTERN.match(line.strip())

    if not match:
        return None

    timestamp_text, level, message = match.groups()

    try:
        timestamp = datetime.strptime(
            timestamp_text, "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        return None

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message,
    }
