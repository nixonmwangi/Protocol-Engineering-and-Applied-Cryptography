import argparse
import cmd
import shlex
import json
import os
from datetime import datetime, timedelta
from colorama import init, Fore, Style
init(autoreset=True)
import csv
from openpyxl import Workbook
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt
import pandas as pd  # For XLSX support

DATA_FILE = "expenditure.json"

class Expenditure(cmd.Cmd):
    intro = Fore.CYAN + (
        " ----------------------------------- \n"
        "|     Expenditure Tracker Cli       |\n"
        " ----------------------------------- \n"
        "| Daily | Weekly | Monthly | Yearly |\n"
        " ----------------------------------- \n"
        "|   Plots graph and saves expenses  |\n"
        " ----------------------------------- \n"
        "                                  \n"
        "            commands              \n"
        "           **********             \n"
        "-> use 'add' to record an expense             \n"
        "-> use 'edit' to update an expense details    \n"
        "-> use 'list' to see all expenses             \n"
        "-> use 'plot' to plot expense graph           \n"
        "-> use 'summary' to view all expense totals   \n"
        "-> use 'help' to show all commands            \n"
        "-> use 'delete' to delete expense by Id='1'   \n"
        "-> use 'exit' to exit program                 \n"
        "--------------------------------------------  \n"
    )
    prompt = Fore.RED + "exp -> " + Style.RESET_ALL

    def __init__(self):
        super().__init__()
        self.file_path = DATA_FILE
        self.expenses = self.load_expenses(self.file_path)

    def load_expenses(self, file_path=None):
        file_path = file_path or self.file_path
        ext = os.path.splitext(file_path)[1].lower()
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([], f, indent=4)
            print(f"Created new file : {file_path}")
            return []
        try:
            if ext == ".json":
                with open(file_path, "r") as f:
                    data = json.load(f)
            elif ext == ".csv":
                with open(file_path, "r") as f:
                    reader = csv.DictReader(f)
                    data = [
                        {"amount": float(row["amount"]), "category": row["category"], "date": row["date"]}
                        for row in reader
                    ]
            elif ext == ".xlsx":
                df = pd.read_excel(file_path)
                data = [
                    {"amount": float(row["Amount"]), "category": row["Category"], "date": row["Date"]}
                    for _, row in df.iterrows()
                ]
            else:
                print(f"❌ Unsupported file type: {ext}")
                return []
            print(f"✅ Loaded {len(data)} expense(s) from {file_path}")
            return data
        except Exception as e:
            print(f"❌ Error loading file: {e}")
            return []

    def save_expenses(self):
        with open(self.file_path, "w") as f:
            json.dump(self.expenses, f, indent=4)

    def do_load(self, line):
        parser = argparse.ArgumentParser(
            prog="load",
            description="Load expenses from a file (json, csv, xlsx). Usage: load <filename>"
        )
        parser.add_argument("filename", nargs="?", help="File to load (json, csv, xlsx)")
        try:
            args = parser.parse_args(shlex.split(line))
            if not args.filename:
              print("Usage: load <filename>\nLoads expenses from a file (json, csv, xlsx) in the current directory or given path.")
              return
            self.file_path = args.filename
            self.expenses = self.load_expenses(args.filename)
        except SystemExit:
            pass
    
    def do_add(self, line):
        parser = argparse.ArgumentParser(prog="add")
        parser.add_argument("--amount", type=float, required=True)
        parser.add_argument("--category", required=True)
        parser.add_argument("--date", help="Date of expense (YYYY-MM-DD HH:MM)")
        try:
            args = parser.parse_args(shlex.split(line))
            date_value = args.date if args.date else datetime.today().strftime("%Y-%m-%d %H:%M")
            self.expenses.append({"amount": args.amount, "category": args.category, "date": date_value})
            self.save_expenses()
            print("-------------------------------------------------")
            print(f"✅ Added expense: {args.amount} in {args.category} on {date_value}")
            print(f"✅ saved in {self.file_path}")
            print("-------------------------------------------------")
        except SystemExit:
            pass

    def do_list(self, line):
        parser = argparse.ArgumentParser(prog="list")
        parser.add_argument("--day")
        parser.add_argument("--week", type=int)
        parser.add_argument("--month", type=int)
        parser.add_argument("--year", type=int)
        parser.add_argument("--category")
        try:
            args = parser.parse_args(shlex.split(line))
            self.list_expense(args.day, args.week, args.month, args.year, args.category)
        except SystemExit:
            pass

    def list_expense(self, day=None, week=None, month=None, year=None, category=None):
        records = []
        for e in self.expenses:
            try:
                dt = datetime.strptime(e["date"], "%Y-%m-%d %H:%M")
                records.append((e, dt))
            except ValueError:
                continue
        if day:
            day_obj = datetime.strptime(day, "%Y-%m-%d").date()
            records = [(e, dt) for (e, dt) in records if dt.date() == day_obj]
        if year:
            records = [(e, dt) for (e, dt) in records if dt.year == year]
        if month:
            records = [(e, dt) for (e, dt) in records if dt.month == month]
        if week:
            records = [(e, dt) for (e, dt) in records if dt.isocalendar()[1] == week]
        if category:
            records = [(e, dt) for (e, dt) in records if e["category"].lower() == category.lower()]
        if not records:
            print("---------------------")
            print("❌ No expenses found.")
            print("---------------------")
            return
        print("\n             *** Expenses ***   ")
        print("----------------------------------------------------")
        print(f"{'Id':<4} {'Date':<12} {'Time':<6}  {'Category':<15} {'Amount':>8}")
        print("---- ------------ ------ ------------       --------")
        for i, (exp, dt) in enumerate(records, start=1):
            print(f"{i:<4} {dt:%Y-%m-%d}   {dt:%H:%M}   {exp['category']:<15} {exp['amount']:>8.2f}")
        print("----------------------------------------------------")

    def do_summary(self, line):
        parser = argparse.ArgumentParser(prog="summary")
        parser.add_argument("--year", type=int)
        parser.add_argument("--month", type=int)
        parser.add_argument("--week", type=int)
        parser.add_argument("--day")
        parser.add_argument("--category")
        try:
            args = parser.parse_args(shlex.split(line))
            self.summary(args.day, args.year, args.month, args.week, args.category)
        except SystemExit:
            pass

    def summary(self, day=None, year=None, month=None, week=None, category=None):
        records = []
        for e in self.expenses:
            try:
                dt = datetime.strptime(e["date"], "%Y-%m-%d %H:%M")
            except ValueError:
                continue
            records.append((e, dt))
        if day:
            day_object = datetime.strptime(day, "%Y-%m-%d").date()
            records = [(e, dt) for (e, dt) in records if dt.date() == day_object]
        if year:
            records = [(e, dt) for (e, dt) in records if dt.year == year]
        if month:
            records = [(e, dt) for (e, dt) in records if dt.month == month]
        if week:
            records = [(e, dt) for (e, dt) in records if dt.isocalendar()[1] == week]
        if category:
            records = [(e, dt) for (e, dt) in records if e["category"].lower() == category.lower()]
        if not records:
            print("❌ No expenses found under that filter.")
            return
        total = sum(e["amount"] for e, dt in records)
        categories = {}
        for e, dt in records:
            categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]
        print("---------------------------------")
        print("\n    *** Expense Summary ***   ")
        print("---------------------------------")
        print(f"Total spent: {total:.2f}\n")
        print("By category:")
        for cat, amt in categories.items():
            percent = (amt / total) * 100
            print(f"  - {cat:<12} {amt:.2f}  ({percent:.1f}%)")
            print("---------------------------------")

    def do_edit(self, line):
        parser = argparse.ArgumentParser(prog="edit")
        parser.add_argument("index", type=int)
        parser.add_argument("--amount", type=float)
        parser.add_argument("--category")
        parser.add_argument("--date")
        try:
            args = parser.parse_args(shlex.split(line))
            self.edit_expense(args.index, args.amount, args.category, args.date)
        except SystemExit:
            pass

    def edit_expense(self, index, amount=None, category=None, date=None):
        if index < 1 or index > len(self.expenses):
            print(f"❌ Invalid expense ID: {index}")
            return
        exp = self.expenses[index - 1]
        if amount is not None:
            exp["amount"] = amount
        if category:
            exp["category"] = category
        if date:
            try:
                datetime.strptime(date, "%Y-%m-%d %H:%M")
                exp["date"] = date
            except ValueError:
                print("❌ Invalid date format. Use YYYY-MM-DD HH:MM")
                return
        self.save_expenses()
        print("--------------------------------------------------------")
        print(f"✅ Updated expense {index}: {exp['amount']} in {exp['category']} on {exp['date']}")
        print(f"✅ Edited in {self.file_path}")
        print("--------------------------------------------------------")

    def do_delete(self, line):
        parser = argparse.ArgumentParser(prog="delete")
        parser.add_argument("index", type=int)
        try:
            args = parser.parse_args(shlex.split(line))
            self.delete_expense(args.index)
        except SystemExit:
            pass

    def delete_expense(self, index):
        if index < 1 or index > len(self.expenses):
            print(f"❌ Invalid expense ID: {index}")
            return
        exp = self.expenses.pop(index - 1)
        self.save_expenses()
        print("--------------------------------------------------------")
        print(f"✅ Deleted expense {index}: {exp['amount']} in {exp['category']} on {exp['date']}")
        print(f"✅ Deleted in {self.file_path}")
        print("--------------------------------------------------------")

    def do_plot(self, line):
        parser = argparse.ArgumentParser(prog="plot")
        parser.add_argument("--day")
        parser.add_argument("--week", type=int)
        parser.add_argument("--month", type=int)
        parser.add_argument("--year", type=int)
        try:
            args = parser.parse_args(shlex.split(line))
            self.plot_expenses(args.day, args.week, args.month, args.year)
        except SystemExit:
            pass

    def plot_expenses(self, day=None, week=None, month=None, year=None):
        filtered = self.expenses[:]
        for e in filtered:
            e["datetime_object"] = datetime.strptime(e["date"], "%Y-%m-%d %H:%M")
        if day:
            day_object = datetime.strptime(day, "%Y-%m-%d").date()
            filtered = [e for e in filtered if e["datetime_object"].date() == day_object]
        if week:
            filtered = [e for e in filtered if e["datetime_object"].isocalendar()[1] == week]
        if month:
            filtered = [e for e in filtered if e["datetime_object"].month == month]
        if year:
            filtered = [e for e in filtered if e["datetime_object"].year == year]
        if not filtered:
            print("❌ No expenses to plot for this filter.")
            return
        totals = {}
        for e in filtered:
            totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
        categories = list(totals.keys())
        amounts = list(totals.values())
        plt.figure(figsize=(8, 5))
        plt.bar(categories, amounts, color='skyblue')
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.title("Expenses per Category")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        for e in filtered:
            del e["datetime_object"]

    def do_export(self, line):
        parser = argparse.ArgumentParser(prog="export")
        parser.add_argument("--format", choices=["json", "csv", "xlsx", "pdf", "png"], required=True)
        parser.add_argument("--filename", default="Expenses Report")
        parser.add_argument("--day")
        parser.add_argument("--week", type=int)
        parser.add_argument("--month", type=int)
        parser.add_argument("--year", type=int)
        try:
            args = parser.parse_args(shlex.split(line))
            filters = {
                "day": args.day,
                "week": args.week,
                "month": args.month,
                "year": args.year
            }
            self.exportFile(args.format, args.filename, filters)
        except SystemExit:
            pass

    def exportFile(self, fmt, filename, filters):
        title = "Expenses Report"
        records = []
        for e in self.expenses:
            try:
                dt = datetime.strptime(e["date"], "%Y-%m-%d %H:%M")
            except ValueError:
                continue
            records.append((e, dt))
        if filters.get("day"):
            day_obj = datetime.strptime(filters["day"], "%Y-%m-%d").date()
            records = [(e, dt) for (e, dt) in records if dt.date() == day_obj]
        if filters.get("year"):
            records = [(e, dt) for (e, dt) in records if dt.year == filters["year"]]
        if filters.get("month"):
            records = [(e, dt) for (e, dt) in records if dt.month == filters["month"]]
        if filters.get("week"):
            records = [(e, dt) for (e, dt) in records if dt.isocalendar()[1] == filters["week"]]
        if not records:
            print("❌ No expenses to export.")
            return
        if fmt == "json":
            with open(f"{filename}.json", "w") as f:
                json.dump([e for e, dt in records], f, indent=4)
            print(f"✅ Exported to {filename}.json")
        elif fmt == "csv":
            with open(f"{filename}.csv", "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["date", "category", "amount"])
                writer.writeheader()
                for e, dt in records:
                    writer.writerow(e)
            print(f"✅ Exported to {filename}.csv")
        elif fmt == "xlsx":
            wb = Workbook()
            ws = wb.active
            ws.title = title
            ws.append(["Date", "Category", "Amount"])
            for e, dt in records:
                ws.append([e["date"], e["category"], e["amount"]])
            wb.save(f"{filename}.xlsx")
            print(f"✅ Exported to {filename}.xlsx")
        elif fmt == "pdf":
            doc = SimpleDocTemplate(f"{filename}.pdf")
            styles = getSampleStyleSheet()
            story = [Paragraph(title, styles["Title"])]
            data = [["Date", "Category", "Amount"]] + [[e["date"], e["category"], e["amount"]] for e, dt in records]
            table = Table(data)
            table.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,0), colors.grey),
                ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
                ("ALIGN", (0,0), (-1,-1), "CENTER"),
                ("GRID", (0,0), (-1,-1), 1, colors.black)
            ]))
            story.append(table)
            doc.build(story)
            print(f"✅ Exported to {filename}.pdf")
        elif fmt == "png":
            totals = {}
            for e, dt in records:
                totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
            categories = list(totals.keys())
            amounts = list(totals.values())
            plt.figure(figsize=(8, 5))
            plt.bar(categories, amounts, color="skyblue")
            plt.title(title)
            plt.xlabel("Category")
            plt.ylabel("Amount")
            plt.tight_layout()
            plt.savefig(f"{filename}.png")
            plt.close()
            print(f"✅ Exported to {filename}.png")
        else:
            print(f"❌ Unsupported format: {fmt}")

    def do_help(self, line):
        commands = {
            "add": "Add a new expense. Example: add --amount 100 --category Food [--date YYYY-MM-DD HH:MM]",
            "list": "List expenses with optional filters. Example: list --day 2025-09-16",
            "summary": "Show summary of expenses. Example: summary --month 9 --year 2025",
            "plot": "Plot expenses per category. Example: plot --week 37",
            "edit": "Edit an expense by index. Example: edit 2 --amount 200",
            "delete": "Delete an expense by index. Example: delete 3",
            "exit": "Exit the shell. Example: exit",
            "help": "Show this help menu. Example: help",
        }
        if line:
            cmd_help = commands.get(line, None)
            if cmd_help:
                print(f"{line}: {cmd_help}")
            else:
                print(f"No help available for '{line}'")
        else:
            print("\nAvailable commands:\n")
            for cmd, desc in commands.items():
                print(f"{cmd:<8} - {desc}")
            print("\nType 'help <command>' to see details for a specific command.\n")

    def do_exit(self, line):
        print("Exited program!")
        return True

if __name__ == "__main__":
    Expenditure().cmdloop()