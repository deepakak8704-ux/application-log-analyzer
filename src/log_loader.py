
from pathlib import Path


def load_logs(file_path):
    """Load log entries from a .log or .txt file."""

    path = Path(file_path)

    if path.suffix.lower() not in (".log", ".txt"):
        print(f"Error: Unsupported file type: {path.suffix}")
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            return file.read().splitlines()

    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return []

    except OSError as error:
        print(f"Error reading file: {error}")
        return []
