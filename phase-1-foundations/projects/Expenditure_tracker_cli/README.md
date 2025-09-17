# Expenditure Tracker CLI

A professional command-line tool for tracking, analyzing, and exporting your personal or business expenses.  
Supports daily, weekly, monthly, yearly, and all-time views, with powerful filtering, plotting graph, and export features.

---

## Features

- **Add, Edit, Delete Expenses:** Manage your expense records easily.
- **List & Filter:** View expenses by day, week, month, year, or category.
- **Summary:** See total spending and category breakdowns.
- **Plot:** Visualize expenses per category using graphs.
- **Export:** Save filtered expenses to JSON, CSV, XLSX, PDF, or PNG.
- **Multi-format Import:** Load expenses from JSON, CSV, or XLSX files.
- **Interactive CLI:** User-friendly shell with color-coded prompts and help.

---

## Requirements

- Python 3.8+
- [colorama](https://pypi.org/project/colorama/)
- [openpyxl](https://pypi.org/project/openpyxl/)
- [reportlab](https://pypi.org/project/reportlab/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [pandas](https://pypi.org/project/pandas/)


Install dependencies:
```sh
pip install colorama openpyxl reportlab matplotlib pandas
```

---
### Installation

It is recommended to use a Python virtual environment to manage dependencies:

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install colorama openpyxl reportlab matplotlib pandas
```

Then, clone the repository and run the CLI tool:

```sh
git clone https://github.com/username/expenditure-tracker-cli.git
cd expenditure-tracker-cli
pip install -r requirements.txt
python expenditure_tracker_cli.py
```

### Main Commands

| Command   | Description & Example |
|-----------|-----------------------|
| `add`     | Add a new expense.<br>Example: `add --amount 100 --category Food [--date YYYY-MM-DD HH:MM]` |
| `edit`    | Edit an expense by index.<br>Example: `edit 2 --amount 200` |
| `delete`  | Delete an expense by index.<br>Example: `delete 3` |
| `list`    | List expenses with filters.<br>Example: `list --day 2025-09-16` |
| `summary` | Show summary of expenses.<br>Example: `summary --month 9 --year 2025` |
| `plot`    | Plot expenses per category.<br>Example: `plot --week 37` |
| `load`    | Load expenses from a file.<br>Example: `load expenditure.json` |
| `export`  | Export expenses to a file.<br>Example: `export --format csv --filename my_report` |
| `help`    | Show help menu.<br>Example: `help` or `help add` |
| `exit`    | Exit the program.<br>Example: `exit` |

---

## How to Use

1. **Add Expenses:**  
   Use the `add` command to record new expenses.

2. **List & Filter:**  
   Use the `list` command with filters (`--day`, `--month`, etc.) to view specific expenses.

3. **Edit/Delete:**  
   Use `edit` or `delete` with the expense index from the list.

4. **Summary & Plot:**  
   Use `summary` and `plot` to analyze your spending.

5. **Export Data:**  
   Use `export` to save your expenses in various formats for reporting or backup.

6. **Load External Files:**  
   Use `load <filename>` to switch between different expense files.

7. **Get Help:**  
   Type `help` or `help <command>` for usage instructions.

---

## Notes

- All expenses are saved in the currently loaded file.
- Supported file formats for loading from client: `.json`, `.csv`, `.xlsx`
- Supported export formats: `.json`, `.csv`, `.xlsx`, `.pdf`, `.png`
- Date format: `YYYY-MM-DD HH:MM` (e.g., `2025-09-17 14:30`)
- For best results, keep your expense files in the same directory or provide the full path.

---

## Example Output

Here is an example of adding and listing expenses:

```sh
> add --amount 50 --category Groceries --date 2025-09-17 18:00
Expense added: Groceries | 2025-09-17 18:00 | $50.00

> add --amount 20 --category Transport --date 2025-09-17 09:00
Expense added: Transport | 2025-09-17 09:00 | $20.00

> list --day 2025-09-17
Index | Category   | Date                | Amount
-----------------------------------------------------
1     | Groceries  | 2025-09-17 18:00    | $50.00
2     | Transport  | 2025-09-17 09:00    | $20.00
-----------------------------------------------------
Total: $70.00
```


## License

MIT License

---

## Author

Developed by Nixon Mwangi  
Protocol Engineering and Applied Cryptography
