# Solve Quadratic expression and create quadratic graph
import matplotlib.pyplot as plt
import numpy as np




def quad_calc(a, b, c):
    x_1 = float(-b - ((b**2 - 4*a*c)**0.5)) / (2*a)
    x_2 = float(-b + ((b**2 - 4*a*c)**0.5)) / (2*a)

    y_1 = (a * (x_1**2)) + (b * x_1) + (c)
    y_2 = (a * (x_2**2)) + (b * x_2) + (c)

    while True:
        print("-----------------------")
        print(f"x1 value : {x_1:.2f}")
        print(f"x2 value : {x_2:.2f}")
        print(f"y1 value : {y_1:.2f}")
        print(f"y2 value : {y_2:.2f}")
        print("---------------------")
        
        choice = input("Do you want to exit (y/n) : ") 
    
        if choice.upper() == "Y" or choice.lower() == 'y':
           print("------------------------------------------------")
           print("Thanks for using the program! See you next time 🙂")
           print("------------------------------------------------")
           break
            
        program()
            

        

def quad():  
    
    print("Solve Quadratic expression")
    print("---------------------------------------------")
    print("Expression : y = ax^2 + bx + c ")
    print("--------------------------------")
    a = float(input(" Value of a : "))
    b = float(input(" Value of b : "))
    c = float(input(" Value of c : "))

    quad_calc(a, b, c)

def graph():  
    print("Graph Quadratic expression")
    print("---------------------------------------------")
    print("Expression : y = ax^2 + bx + c ")
    print("--------------------------------")
    a = float(input(" Value of a : "))
    b = float(input(" Value of b : "))
    c = float(input(" Value of c : "))

    d = x_value()
    y = [a * x**2 + b * x + c for x in d]

    # convert to numpy arrays for easier min/max
    d = np.array(d)
    y = np.array(y)

    for x_v, y_v in zip(d, y):
        print(f"x value : {x_v}  y value: {y_v}")

    print("Thanks for using the program! See you next time 🙂")

    fig, ax = plt.subplots(figsize=(8,6))
    
    ax.plot(d, y, marker="o", label="y = ax² + bx + c", linestyle="--",)
    ax.grid(True)
    ax.figure(figsize=(4,4))

    # Move axes to cross at origin
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Auto set axis limits
    ax.set_xlim(d.min(), d.max())
    ax.set_ylim(y.min(), y.max())

    ax.set_xlabel("x values")
    ax.set_ylabel("y values")
    ax.set_title("Quadratic Graph: y = ax^2 + bx + c")
    ax.legend()
    ax.show()
        
    
def x_value(): 
    print("-------------------------")
    x = int(input(" How many values of x : "))
    print("-------------------------")
    x_array = []

    for v in range (1, x + 1):
        x_values = float(input(f"Value of x{v} : "))
        print("-------------------")
        x_array.append(x_values)   
        
    return (x_array)

def program():
    print("-----------------------------------------------------")
    
    print("Solve Quadratic expression and create quadratic graph")
    print("-----------------------------------------------------")

    try:
        choice = input("Solve expression enter (1)| Plot quadratic graph enter (2) | Quit press any key : ")
        print("------------------------------------------------------------------------------------------------")
        if choice.isdigit():  # check if input is a number
            choice = int(choice)  # convert to int
            if choice == 1:
                quad()
            elif choice == 2:
                graph()
            else:
                print("Exiting program...")
        else:
            print("Exiting program...")
    except:
        print("Exiting program...")
        print("----------------------------")


if __name__ == "__main__":
    program()
        
        
           
