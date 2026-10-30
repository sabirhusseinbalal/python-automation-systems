# Automated Report Generator (CSV → PDF)

## Description

A simple sales report generator built with Python, Pandas, NumPy, and ReportLab.

It reads sales data from a CSV file, checks the data, calculates useful summaries, and generates a PDF report.

---

## What this project does

- Reads sales data from a CSV file
- Checks required columns and data values
- Calculates total revenue, cost, and profit margin
- Finds the top 5 products by revenue
- Calculates revenue by category and month
- Generates a PDF sales report

---

## Modules Used

- `pandas` – Reads and processes CSV data
- `numpy` – Checks financial calculations
- `reportlab` – Generates PDF reports
- `pathlib` – Handles file and folder paths
- `datetime` – Converts and handles dates

---

## Project Structure

```text
06_automated_report_generator/
├── main.py
├── config.py
├── data_processor.py
├── report_generator.py
├── input/
│   └── sales_raw.csv
├── output/
│   └── sales_report.pdf
├── requirements.txt
└── README.md
```

---

## How to Run

1. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. Place your sales CSV file inside the `input/` folder with the name `sales_raw.csv`.

3. Make sure your CSV contains these columns:

   ```text
   product, category, quantity, unit_price, unit_cost,
   revenue, cost, margin, order_date
   ```

4. Run the program:

   ```bash
   python main.py
   ```

5. Open the `output/` folder to find the generated `sales_report.pdf`.

**Note:** The report is overwritten when the program runs again.
