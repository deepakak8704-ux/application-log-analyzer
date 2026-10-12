
import sys
from pathlib import Path

import pytest

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from report_generator import generate_report


@pytest.fixture
def sample_report_data():
    return {
        "total_lines": 8,
        "total_valid_entries": 7,
        "malformed_count": 1,
        "info_count": 2,
        "warning_count": 2,
        "error_count": 3,
        "frequent_errors": [
            ("Database connection failed", 2),
            ("Invalid user credentials", 1),
        ],
    }


def test_generate_report_creates_file(tmp_path, sample_report_data):
    report_path = tmp_path / "output" / "report.txt"

    generate_report(sample_report_data, report_path)

    assert report_path.exists()


def test_report_contains_correct_summary(tmp_path, sample_report_data):
    report_path = tmp_path / "report.txt"

    generate_report(sample_report_data, report_path)
    content = report_path.read_text(encoding="utf-8")

    assert "Total entries: 8" in content
    assert "Valid entries: 7" in content
    assert "Malformed entries: 1" in content
    assert "INFO: 2" in content
    assert "WARNING: 2" in content
    assert "ERROR: 3" in content


def test_report_contains_frequent_errors(tmp_path, sample_report_data):
    report_path = tmp_path / "report.txt"

    generate_report(sample_report_data, report_path)
    content = report_path.read_text(encoding="utf-8")

    assert "Database connection failed - 2 occurrences" in content
    assert "Invalid user credentials - 1 occurrences" in content


def test_report_when_no_errors_exist(tmp_path, sample_report_data):
    report_path = tmp_path / "report.txt"
    sample_report_data["frequent_errors"] = []

    generate_report(sample_report_data, report_path)
    content = report_path.read_text(encoding="utf-8")

    assert "No errors found." in content
