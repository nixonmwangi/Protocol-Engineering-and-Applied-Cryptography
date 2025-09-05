import matplotlib.pyplot as  plt 

def daily():
    categories = [
       "Food", 
       "Transportation", 
       "Groceries",  
       "Maintenance", 
       "Miscellaneous",  
       "Gas",
    ]
    daily_cost = []
    print("---------------------------------------------------")
    
    for cat in categories:
        while True:
            try:
               amount = float(input(f"{cat} cost: "))
               daily_cost.append(amount)
               print("--------------------")
               break
            except ValueError:
               print("Invalid input, please enter a number.") 
    print("***Total Daily Cost***")
    print("---------------------") 
    print(f"Total expenditure : {sum(daily_cost)}")
    print("--------------------")

    plt.bar(categories, daily_cost)
    plt.title("Daily Expenditure")
    plt.xlabel("Categories")
    plt.ylabel("Cost")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()
    
        
def weekly():
    categories = [
    "Food", 
    "Transportation", 
    "Maintenance",
    "Groceries", 
    "Entertainment", 
    "Shopping",    
    "Miscellaneous",
    "Night outs",  
    ]
    weekly_cost = []
    print("---------------------------------------------------")
    for cat in categories:
        while True:
            try:
               amount = float(input(f"{cat} cost: "))
               weekly_cost.append(amount)
               print("--------------------")
               break
            except ValueError:
               print("Invalid input, please enter a number.")
    print("***Total Weekly Cost***")
    print("---------------------") 
    print(f"Total expenditure : {sum(weekly_cost)}")
    print("--------------------")

    plt.bar(categories, weekly_cost)
    plt.title("Weekly Expenditure")
    plt.xlabel("Categories")
    plt.ylabel("Cost")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()
    
def monthly():
    categories = [
    "Food",    
    "Transportation", 
    "Internet", 
    "Groceries", 
    "Health", 
    "Entertainment", 
    "Maintenance", 
    "Others", 
    "Power-Bill", 
    "Health and Medical"   
    "Gas", 
    "Water", 
    "Rent", 
    "Insurance", 
    "Housing",
    "contributions",
    "Miscellaneous",   
    ]
    monthly_cost = []
    print("---------------------------------------------------")
    for cat in categories:
        while True:
            try:
               amount = float(input(f"{cat} cost: "))
               monthly_cost.append(amount)
               print("--------------------")
               break
            except ValueError:
               print("Invalid input, please enter a number.")       
    print("***Total Monthly Cost***")
    print("---------------------") 
    print(f"Total expenditure : {sum(monthly_cost)}")
    print("--------------------")

    plt.bar(categories, monthly_cost)
    plt.title("Monthly Expenditure")
    plt.xlabel("Categories")
    plt.ylabel("Cost")
    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.show()

def expenditure():
         print("---------------------------------------------------")
         print("   ***Track Daily/Weekly/Monthly Expenditure****   ")
         print("---------------------------------------------------")
         print("Food, Transportation, Internet, Groceries, Health ")
         print("Entertainment, Transportation,  Maintenance, Others")
         print("Food, Power-Bill, Gas, Water, Rent, Insurance, Housing, etc")
         print("---------------------------------------------------")
         

         while True:
            choice = input("Daily (1) | Weekly (2) | Monthly (3) | Exit (q/any) : ")

            try:
                if choice == "1":
                   daily()
                elif choice == "2":
                   weekly()
                elif choice == "3":
                   monthly()
                else:
                   print("Exiting program ... Goodbye")
                   break
            except ValueError:
                   print("Exiting program ... Goodbye")
 
if __name__ == "__main__":
     expenditure()
                 
            
             
         
          