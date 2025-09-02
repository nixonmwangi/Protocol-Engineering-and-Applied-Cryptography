'''
Multiplication table of any number 1 - 15
'''
def math_table():

    x = input("Please enter a number to get multiplication table 1 - 15: ")
    try:
        x = float(x)
        if x > 0 and x.is_integer or float:
            for i in range(1, 16):
                result = x * i
                print(f"{x} x {i} = {round(result, 2)}")
    except ValueError:
        print("Please input a valid number!")
    

if  __name__ == "__main__":
    math_table()


