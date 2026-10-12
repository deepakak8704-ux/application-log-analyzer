
from collections import Counter


def analyze_logs(parsed_logs):
    """Analyze parsed log entries and return summary statistics."""

    level_counts = Counter()
    error_messages = []

    for log in parsed_logs:
        level_counts[log["level"]] += 1

        if log["level"] == "ERROR":
            error_messages.append(log["message"])

    frequent_errors = Counter(error_messages)

    return {
        "total_valid_entries": len(parsed_logs),
        "info_count": level_counts["INFO"],
        "warning_count": level_counts["WARNING"],
        "error_count": level_counts["ERROR"],
        "frequent_errors": frequent_errors.most_common(),
    }
