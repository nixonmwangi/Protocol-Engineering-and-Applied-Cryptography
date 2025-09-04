'''
Multiplication table of any number
'''
def math_table():
    """
    Prompts the user to enter a number and a multiple, then prints the multiplication table
    for that number up to the specified multiple. Continues until the user chooses to exit.
    """
    while True:
        try:
            # Ask user for the base number (can be float)
            x = float(input("Please enter a number to get multiplication table : "))
            # Ask user for the number of multiples (must be integer)
            m = int(input("which multiple : "))
            # Validate inputs
            if x == 0.0 or m == 0:
                print("Enter a valid number")
            else:
                # Print multiplication table up to m

                for i in range(1, m + 1):
                    result = x * i
                    print(f"{x} x {i} = {round(result, 2)}")
                # Ask if user wants to continue
                cont = input("Do you want to continue (y/n): ")
                if cont.lower() != "y":
                    break
        except ValueError:
            # Handle invalid input
            print("Enter a valid number!")

if __name__ == "__main__":
    # Run the multiplication table function if script is executed directly
    math_table()



