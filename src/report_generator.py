
from pathlib import Path


def generate_report(report_data, output_path):
    """Generate and save a log analysis report."""

    output_file = Path(output_path)

    lines = [
        "APPLICATION LOG ANALYSIS REPORT",
        "=" * 35,
        f"Total entries: {report_data['total_lines']}",
        f"Valid entries: {report_data['total_valid_entries']}",
        f"Malformed entries: {report_data['malformed_count']}",
        "",
        "LOG LEVEL SUMMARY",
        "-" * 20,
        f"INFO: {report_data['info_count']}",
        f"WARNING: {report_data['warning_count']}",
        f"ERROR: {report_data['error_count']}",
        "",
        "FREQUENTLY OCCURRING ERRORS",
        "-" * 28,
    ]

    frequent_errors = report_data["frequent_errors"]

    if frequent_errors:
        for message, count in frequent_errors:
            lines.append(f"{message} - {count} occurrences")
    else:
        lines.append("No errors found.")

    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(
            "\n".join(lines) + "\n",
            encoding="utf-8",
        )
        print(f"Report saved to: {output_file}")

    except OSError as error:
        print(f"Could not save report: {error}")
