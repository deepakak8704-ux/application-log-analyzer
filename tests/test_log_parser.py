
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from log_parser import parse_log_line


def test_parse_valid_log():
    result = parse_log_line(
        "2026-10-12 09:00:00 INFO Application started"
    )

    assert result is not None
    assert result["level"] == "INFO"
    assert result["message"] == "Application started"


def test_parse_malformed_log():
    result = parse_log_line("INVALID LOG ENTRY")

    assert result is None


def test_parse_invalid_date():
    result = parse_log_line(
        "2026-13-12 09:00:00 ERROR Invalid date"
    )

    assert result is None
