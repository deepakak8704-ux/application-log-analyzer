
import sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from log_analyzer import analyze_logs


def test_analyze_log_levels():
    logs = [
        {"level": "INFO", "message": "Started"},
        {"level": "WARNING", "message": "Low disk"},
        {"level": "ERROR", "message": "Database failed"},
        {"level": "ERROR", "message": "Database failed"},
    ]

    result = analyze_logs(logs)

    assert result["total_valid_entries"] == 4
    assert result["info_count"] == 1
    assert result["warning_count"] == 1
    assert result["error_count"] == 2


def test_frequent_errors():
    logs = [
        {"level": "ERROR", "message": "Database failed"},
        {"level": "ERROR", "message": "Database failed"},
    ]

    result = analyze_logs(logs)

    assert result["frequent_errors"] == [
        ("Database failed", 2)
    ]
