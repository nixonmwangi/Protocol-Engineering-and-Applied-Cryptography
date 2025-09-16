# Expenditure tracker
# cli tool that help track your daily, weekly and monthly expenditure

import argparse
import json
import os 
import shlex
import cmd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


file = "expenditure.json"
expenses = []

#Functions


# Check file if exists or create it 

def file():

     try: 

        with open("expenditure.json", "r") as f:
            print("File exists : Expenditure.json  ")

     except FileNotFoundError:

        with open("./expenditure.json", "w") as f:
            f.write("Expenditure File")
            print("File created: Expenditure.json")
        
        

# Help arguments

def help(args):
    print("help expense")
    
# Adding expenses

def add_expense(amount, category, date):
    expenses.append({"amount": amount, "category": category, "date": date})
    print("-------------------------------------------------")
    print(f"✅ Added expense: {amount} in {category} on {date}")
    print("-------------------------------------------------")  

# List expenses   

def list_expense(expenses, day=None, week=None, month=None, year=None, category=None):
    """List expenses with optional filters (day/week/month/year/category)."""

    # Convert to (expense, datetime) pairs safely
    records = []
    for e in expenses:
        try:
            dt = datetime.strptime(e["date"], "%Y-%m-%d %H:%M")
            records.append((e, dt))
        except ValueError:
            continue  # skip invalid dates

    # Apply filters directly
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

    # Handle empty results
    if not records:
        print("---------------------")
        print("❌ No expenses found.")
        print("---------------------")
        return

    # Print table header
    print("\n             *** Expenses ***   ")
    print("----------------------------------------------------")
    print(f"{'Id':<4} {'Date':<12} {'Time':<6}  {'Category':<15} {'Amount':>8}")
    print("---- ------------ ------ ------------       --------")

    # Print each row
    for i, (exp, dt) in enumerate(records, start=1):
        
        print(f"{i:<4} {dt:%Y-%m-%d}   {dt:%H:%M}   {exp['category']:<15} {exp['amount']:>8.2f}")
    print("----------------------------------------------------")


# Summarise expense

def summary(expenses, day=None, year=None, month=None, week=None, category=None):
    """Show summary of expenses (total + per category + percentages)."""

    records = []

    for e in expenses:
        try:
            dt = datetime.strptime(e["date"], "%Y-%m-%d %H:%M")
            
        except ValueError:
            continue
        records.append((e, dt))

    # Filters

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


    # Totals

    total = sum(e["amount"] for e, dt in records)
    categories = {}

    for e, dt in records:
        categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]


    # Print
    print("---------------------------------")
    print("\n    *** Expense Summary ***   ")
    print("---------------------------------")
    print(f"Total spent: {total:.2f}\n")
    print("By category:")
    for cat, amt in categories.items():
        percent = (amt / total) * 100
        print(f"  - {cat:<12} {amt:.2f}  ({percent:.1f}%)")   
        print("---------------------------------")
        



# Edit expense    

def edit_expense(index, amount=None, category=None, date=None):

    if index < 1 or index > len(expenses):
        print(f"❌ Invalid expense ID: {index}")
        return

    exp = expenses[index - 1]  # 1-based indexing

    # Update fields if provided

    if amount is not None:
        exp["amount"] = amount

    if category:
        exp["category"] = category

    if date:
        try:
        # Vakidate format
            datetime.strptime(date, "%Y-%m-%d %H:%M")
            exp["date"] = date

        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD HH:MM")
            return
    print("--------------------------------------------------------")
    print(f"✅ Updated expense {index}: {exp['amount']} in {exp['category']} on {exp['date']}")       
    print("--------------------------------------------------------")
            

# Delete expenses

def delete_expense(index):
    """Delete an expense from the global expenses list."""

    if index < 0 or index > len(expenses):
        print(f"❌ Invalid expense ID: {index}")
        return

    exp =  expenses.pop(index - 1)
    
    print("--------------------------------------------------------")
    print(f"✅ Deleted expense {index}: {exp['amount']} in {exp['category']} on {exp['date']}")
    print("--------------------------------------------------------")    
    

# Plot expense graph    

def plot_expenses(expenses, day=None, week=None, month=None, year=None):
    
    """Plot total expenses per category with optional filters."""
    
    # Filter expenses similar to list_expense()
    filtered = expenses[:]

    # Convert dates to datetime objects

    for e in filtered:
        e["datetime_object"] = datetime.strptime(e["date"], "%Y-%m-%d %H:%M")

    if day:
        day_object = datetime.strptime(day, "%Y-%m-%d").date()
        filtered = [e for e in filtered if e["datetime_object"].date() == day_object]

    if week:
        filtered = [e for e in filtered if e["datetime-object"].isocalender()[1] == week]

    if month:
        filtered = [e for e in filtered if e["datetime_object"].month == month]
        
    if year:
        filtered = [e for e in filtered if e["datetime_object"].year == year]

    if not filtered:
        print("❌ No expenses to plot for this filter.")
        return   
        
    # Aggregate totals per category
    totals = {}
    for e in filtered:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    
    # Plot
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
    
    # Cleanup
    for e in filtered:
        del e["datetime_object"]    

    

    

    


class Expenditure(cmd.Cmd):
    
    intro = (
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
        "-> use 'edit' to update an expense details  \n"
        "-> use 'list' to see all expenses             \n"
        "-> use 'plot' to plot expense graph           \n"
        "-> use 'summary' to view all expense totals   \n"
        "-> use 'help' to show all commands            \n"
        "-> use 'delete' to delete expense by Id='1'   \n"
        "--------------------------------------------  \n"    
        
    )

    prompt = "exp -> "

    def do_add(self, line):
        """Add a new expense. Usage: add --amount 100 --category food [--date YYYY-MM-DD]"""
        parser = argparse.ArgumentParser(prog="add")
        parser.add_argument("--amount", type=float, required=True)
        parser.add_argument("--category", required=True)
        parser.add_argument("--date", help="Date of expense (YYYY-MM-DD)")

        try:
            args = parser.parse_args(shlex.split(line))
            date_value = args.date if args.date else datetime.today().strftime("%Y-%m-%d %H:%M")
            add_expense(args.amount, args.category, date_value)
            

        except SystemExit:
            pass
            
    def do_list(self, line):

         """
         List expenses. Usage:
            list                -> show all
            list --day          -> show today's expenses
            list --week         -> show this week's expenses
            list --month        -> show this month's expenses
            list --year         -> show this year's expenses
         """
         
         parser = argparse.ArgumentParser(prog="list")
         parser.add_argument("--day", help="Filter by specific date (YYYY-MM-DD)")
         parser.add_argument("--week", type=int, help="Filter by ISO week number (1-52)")
         parser.add_argument("--month", type=int, help="Filter by month (1-12)")
         parser.add_argument("--year", type=int, help="Filter by year (e.g 2025)")
         parser.add_argument("--category")

         try:

             args = parser.parse_args(shlex.split(line))  
             list_expense(expenses, args.day, args.week, args.month, args.year, category=args.category)

         except SystemExit:
             pass


    def do_summary(self, line):

        """ Show expense summary. Usage: summary [--year YYYY] [--month M] [--week W] [--day D YYYY-MM-DD] [--category ]"""

        parser = argparse.ArgumentParser(prog="summary")
        parser.add_argument("--year", type=int, help="Filter by year (e.g 2025)")
        parser.add_argument("--month", type=int, help="Filter by month (1-12)")
        parser.add_argument("--week", type=int, help="Filter by ISO week (1-52)")
        parser.add_argument("--day", help="Filter by specific date (YYYY-MM-DD)")
        parser.add_argument("--category")


        try:
            args = parser.parse_args(shlex.split(line))
            summary(expenses, day=args.day, year=args.year, month=args.month, week=args.week, category=args.category)

        except SystemExit:
            pass

    def do_edit(self, line):
        """Edit an existing expense. Usage: edit INDEX [--amount X] [--category Y] [--date 'YYYY-MM-DD HH:MM']"""
        
        parser = argparse.ArgumentParser(prog="edit")
        parser.add_argument("index", type=int, help="Expense Id to edit (as shown in list)")
        parser.add_argument("--amount", type=float, help="New amount")
        parser.add_argument("--category", help="expense category")
        parser.add_argument("--date", help="New date (YYYY-MM-DD HH:MM)")

        try:
            args = parser.parse_args(shlex.split(line))
            edit_expense(index=args.index, amount=args.amount, category=args.category, date=args.date)

        except SystemExit:
            pass

    def do_delete(self, line):
         """Delete an expense. Usage: delete INDEX"""

         parser = argparse.ArgumentParser(prog="delete")
         parser.add_argument("index", type=int, help="Expense Id to delete (required)")

         try:
             args = parser.parse_args(shlex.split(line))
             delete_expense(index=args.index)
             
         except SystemExit:
             pass

    def do_plot(self, line):
         """Plot expenses. Optional filters: --day, --week, --month, --year"""
         parser = argparse.ArgumentParser(prog="plot")
         parser.add_argument("--day", help="Filter by specific date (YYYY-MM-DD)")
         parser.add_argument("--week", type=int, help="Filter by ISO week number (1-52)")
         parser.add_argument("--month", type=int, help="Filter by month (1-12)")
         parser.add_argument("--year", type=int, help="Filter by year (e.g. 2025)")

         try:
            args = parser.parse_args(shlex.split(line))
            plot_expenses(expenses, day=args.day, week=args.week, month=args.month, year=args.year)
         except SystemExit:
            pass

            

            
        
      
        
        
# main  

if __name__ == "__main__":
    Expenditure().cmdloop()
  
    
    