 API Data History Tracker (SQLite + Excel)

This project is a Python-based automation tool designed to fetch data from APIs, maintain a historical database without duplicates, and export the results into professional Excel reports.

## Key Features
- **API Integration:** Fetches real-time data using the `requests` library.
- **Duplicate Prevention:** Uses SQLite `PRIMARY KEY` and `INSERT OR IGNORE` logic to ensure data is only saved once.
- **Automated Reporting:** Generates an `.xlsx` report using `pandas` for easy data analysis.
- **Process Logging:** Tracks every step (API calls, DB writes, errors) in a `tracker.log` file.

## 🛠️ Tech Stack
- **Python 3.x**
- **SQLite3** (Database)
- **Pandas** (Data Manipulation & Excel)
- **Requests** (API Communications)
- **Logging** (System Tracking)

## 📋 How It Works
1. The script initializes a local SQLite database and a log file.
2. It fetches the latest posts from a sample REST API.
3. It filters and formats the data into a clean structure.
4. It attempts to insert records into the database (skipping existing ones).
5. It exports the entire database history into an Excel file named `review.xlsx`.

## 📂 Project Structure
- `main.py`: The core automation script.
- `tracker.db`: Local database file (generated automatically).
- `tracker.log`: Logs of the program's execution.
- `review.xlsx`: Final Excel report.
