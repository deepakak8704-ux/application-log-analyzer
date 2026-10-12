
import sys
import pytest
from pathlib import Path
from datetime import datetime

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from log_filter import filter_logs


@pytest.fixture
def sample_logs():
    return [
        {
            "timestamp": datetime(2026, 10, 12, 9, 0, 0),
            "level": "INFO",
            "message": "Application started",
        },
        {
            "timestamp": datetime(2026, 10, 12, 9, 1, 0),
            "level": "WARNING",
            "message": "Disk space is low",
        },
        {
            "timestamp": datetime(2026, 10, 12, 9, 2, 0),
            "level": "ERROR",
            "message": "Database connection failed",
        },
        {
            "timestamp": datetime(2026, 10, 13, 9, 0, 0),
            "level": "ERROR",
            "message": "Invalid user credentials",
        },
    ]


def test_filter_by_level(sample_logs):
    result = filter_logs(sample_logs, level="ERROR")

    assert len(result) == 2
    assert all(log["level"] == "ERROR" for log in result)


def test_filter_by_keyword(sample_logs):
    result = filter_logs(sample_logs, keyword="database")

    assert len(result) == 1
    assert result[0]["message"] == "Database connection failed"


def test_filter_by_date(sample_logs):
    result = filter_logs(
        sample_logs,
        filter_date="2026-10-12",
    )

    assert len(result) == 3


def test_combined_filters(sample_logs):
    result = filter_logs(
        sample_logs,
        level="ERROR",
        keyword="database",
        filter_date="2026-10-12",
    )

    assert len(result) == 1
    assert result[0]["message"] == "Database connection failed"


def test_invalid_level(sample_logs):
    import pytest

    with pytest.raises(ValueError):
        filter_logs(sample_logs, level="DEBUG")


def test_invalid_date(sample_logs):
    import pytest

    with pytest.raises(ValueError):
        filter_logs(sample_logs, filter_date="2026-13-45")
