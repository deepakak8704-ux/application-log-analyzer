
# Application Log Analyzer & Error Reporting System

## 1. Project Overview

The Application Log Analyzer & Error Reporting System is a Python-based project that reads application log files, identifies log levels, detects malformed entries, analyzes errors, and generates a summary report.

This project was developed as part of the SkyCurve Technologies internship.

## 2. Features

- Read `.log` and `.txt` files.
- Parse timestamps, log levels, and messages.
- Identify INFO, WARNING, and ERROR entries.
- Detect malformed log entries.
- Count entries by log level.
- Find frequently occurring error messages.
- Filter logs by level, keyword, and date.
- Generate a text-based analysis report.
- Record application events and warnings using Python logging.
- Handle invalid files and malformed log entries.
- Run automated tests using pytest.

## 3. Technologies Used

- Python
- Regular Expressions
- pathlib
- datetime
- collections.Counter
- logging
- pytest

## 4. Project Structure

```text
application-log-analyzer/
├── src/
│   ├── main.py
│   ├── log_loader.py
│   ├── log_parser.py
│   ├── log_analyzer.py
│   ├── log_filter.py
│   └── report_generator.py
├── data/
│   └── sample.log
├── output/
│   └── report.txt
├── logs/
│   └── app.log
├── tests/
│   ├── test_log_parser.py
│   ├── test_log_analyzer.py
│   └── test_log_filter.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 5. Installation

Make sure Python is installed on your computer.

Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

## 6. Run the Application

From the project root directory, run:

```bash
python src/main.py
```

The application reads `data/sample.log`, analyzes its entries, displays a summary in the terminal, and saves the report to `output/report.txt`.

Application logs are recorded in `logs/app.log`.

## 7. Run the Tests

Run the following command from the project root directory:

```bash
python -m pytest -v
```

The project currently contains 19 automated tests covering log loading, parsing, analysis, filtering, and report generation.

## 8. Sample Results

For the included sample log file:

- Total entries: 8
- Valid entries: 7
- Malformed entries: 1
- INFO entries: 2
- WARNING entries: 2
- ERROR entries: 3

Frequently occurring errors:

- Database connection failed: 2 occurrences
- Invalid user credentials: 1 occurrence

## 9. Output

The generated report includes:

- Total number of log entries
- Number of valid and malformed entries
- Counts for each log level
- Frequently occurring error messages

The report is saved as `output/report.txt`.

## 10. Future Improvements

- Support filtering through command-line arguments.
- Allow users to specify custom input files.
- Export reports in CSV or JSON format.
- Add more tests for file loading and report generation.
- Provide date-range filtering and additional statistics.

## 11. Author

Deepak

SkyCurve Technologies Internship Project
