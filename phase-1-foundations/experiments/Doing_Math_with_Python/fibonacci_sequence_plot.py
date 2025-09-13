#Ratio between consecutive fibonacci numbers
import matplotlib.pyplot as plt

def fibonacci(v):
    # Generate Fibonacci numbers
    f = [1,1]
    
    while len(f) < v:
          f.append(f[-1] + f[-2])

    print(f"Shows upto {v} Fibonnaci numbers: ") 
    print("-----------------------------------")

    x = []
    print(f)
    x.append(f)

    ratio = [f[x+1]/f[x] for x in range(len(f)-1)]
    
    plt.figure(figsize=(10, 6))
    plt.plot(ratio, color="g")
    plt.axhline(y=1.618, color="gray", linestyle="-")  # Golden ratio line
    plt.title("Ratio between consecutive Fibonacci numbers")
    plt.xlabel("No.")
    plt.ylabel("Ratio")
    plt.ylim(1, 2.2)  # Set y-axis range similar to your image
    plt.grid(True)
    plt.show()

    

if __name__ == "__main__":
    print("--------------------------------------------")
    print("*** The fibonnaci sequence with a graph ***")
    print("--------------------------------------------")

    while True:
        try:
            v = int(input("Number of sequences (1 - 100) : "))
            print("--------------------------------------------")
            fibonacci(v)
            
            print("--------------------------------")
            choice = input("Do you want to continue (y/n) : ")
            print("--------------------------------")
            if choice.upper() != "Y" or choice.lower() != "y":
               print("Graph plotted !! ... Goodbye")
               print("------------------------")
               break
    
        except ValueError:
            print("Invalid!! Enter a number")


    