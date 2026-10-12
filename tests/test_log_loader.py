import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from log_loader import load_logs

def test_load_valid_log_file(tmp_path):
    log_file = tmp_path / "sample.log"
    log_file.write_text(
        "2026-10-12 09:00:00 INFO Application started\n",
        encoding="utf-8",
    )

    result = load_logs(log_file)

    assert len(result) == 1
    assert result[0] == "2026-10-12 09:00:00 INFO Application started"


def test_load_valid_txt_file(tmp_path):
    text_file = tmp_path / "sample.txt"
    text_file.write_text("First entry\nSecond entry\n", encoding="utf-8")

    result = load_logs(text_file)

    assert result == ["First entry", "Second entry"]


def test_unsupported_file_type(tmp_path, capsys):
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text("some,data\n", encoding="utf-8")

    result = load_logs(csv_file)

    assert result == []
    assert "Unsupported file type" in capsys.readouterr().out


def test_missing_file(capsys, tmp_path):
    missing_file = tmp_path / "missing.log"

    result = load_logs(missing_file)

    assert result == []
    assert "File not found" in capsys.readouterr().out
