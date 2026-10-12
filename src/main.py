
import logging
from pathlib import Path

from log_loader import load_logs
from log_parser import parse_log_line
from log_analyzer import analyze_logs
from report_generator import generate_report


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "sample.log"
REPORT_FILE = BASE_DIR / "output" / "report.txt"
LOG_FILE = BASE_DIR / "logs" / "app.log"


# Configure application logging
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True,
)

logger = logging.getLogger(__name__)


def main():
    """Run the complete log analysis application."""

    logger.info("Log analysis started")

    try:
        # Step 1: Load raw log entries
        raw_logs = load_logs(DATA_FILE)

        if not raw_logs:
            logger.warning("No log entries loaded from %s", DATA_FILE)
            print("No log entries loaded. Check the input file.")
            return

        logger.info("Loaded %d raw log entries", len(raw_logs))

        # Step 2: Parse log entries
        parsed_logs = []
        malformed_count = 0

        for line_number, line in enumerate(raw_logs, start=1):
            parsed = parse_log_line(line)

            if parsed is None:
                malformed_count += 1
                logger.warning(
                    "Malformed log entry at line %d: %s",
                    line_number,
                    line,
                )
            else:
                parsed_logs.append(parsed)

        logger.info(
            "Parsing completed: %d valid, %d malformed",
            len(parsed_logs),
            malformed_count,
        )

        # Step 3: Analyze valid entries
        analysis = analyze_logs(parsed_logs)

        # Step 4: Prepare report data
        report_data = {
            "total_lines": len(raw_logs),
            "total_valid_entries": analysis["total_valid_entries"],
            "malformed_count": malformed_count,
            "info_count": analysis["info_count"],
            "warning_count": analysis["warning_count"],
            "error_count": analysis["error_count"],
            "frequent_errors": analysis["frequent_errors"],
        }

        # Step 5: Generate and save the report
        generate_report(report_data, REPORT_FILE)

        # Step 6: Display summary in the terminal
        print("\n--- Application Log Analysis Report ---")
        print(f"Input file: {DATA_FILE.name}")
        print(f"Total entries: {len(raw_logs)}")
        print(f"Valid entries: {len(parsed_logs)}")
        print(f"Malformed entries: {malformed_count}")
        print(f"INFO count: {analysis['info_count']}")
        print(f"WARNING count: {analysis['warning_count']}")
        print(f"ERROR count: {analysis['error_count']}")

        print("\nFrequently Occurring Errors:")

        if analysis["frequent_errors"]:
            for message, count in analysis["frequent_errors"]:
                print(f"{message}: {count} occurrence(s)")
        else:
            print("No errors found.")

        print(f"\nReport location: {REPORT_FILE}")
        print(f"Application log: {LOG_FILE}")

        logger.info("Log analysis completed successfully")

    except (OSError, ValueError, KeyError, TypeError):
        logger.exception("Log analysis failed")
        print(
            "An error occurred during log analysis. "
            f"Check the application log: {LOG_FILE}"
        )


if __name__ == "__main__":
    main()
