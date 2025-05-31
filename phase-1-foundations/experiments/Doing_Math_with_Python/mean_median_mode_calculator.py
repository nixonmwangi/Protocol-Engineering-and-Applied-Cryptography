from collections import Counter   # Import Counter to count frequencies

# ---------------- MEAN FUNCTION ----------------
def mean(values):
    # Handle case where list is empty
    if not values:
       return None
        
    # Mean = sum of values ÷ number of values
    m = (sum(values)) / (len(values))
    print(f"Mean    : {m:.2f}")   # Print mean rounded to 2 decimals


# ---------------- MEDIAN FUNCTION ----------------
def median(values):
    # Handle case where list is empty
    if not values:
        return None

    # Sort the values to find the middle
    values = sorted(values)   
    
    # If odd number of items, take the middle one
    if len(values) % 2 != 0:
        l = len(values) // 2
        v = values[l]
        print(f"Median  : {v}")
    else:
        # If even number of items, take average of two middle values
        l = len(values) // 2
        l2 = l - 1
        v1 = values[l]
        v2 = values[l2]
        v = (v1 + v2) / 2
        print(f"Median  : {v}")


# ---------------- FREQUENCY FUNCTION ----------------
def frequency(values):
    # Handle empty list
    if not values:
        return None
    
    # Use Counter to count frequencies
    v = Counter(values)    
    
    # Find the mode (most common value)
    m = v.most_common(1)   # Returns list like [(value, count)]
    mode = m[0][0]         # Extract the value (first element of tuple)
    print(f"Mode    : {mode}")
    print("-----------------------") 
    
    # Get full frequency table
    c = v.most_common()
   
    print("*** Frequency Table ***")
    print("------------------------")
    print("Number  |  Frequency")
    print("------  |  ---------")

    # Print each value with its count
    for value, count in c:
        # <7 means left-align values within 7 spaces
        print(f"{value:<7} |  {count}")

    print("-------------------------")   


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    print("---------------------------------------------------")
    print("*** Calculate Mean, Median, Mode and Frequency ***")
    print("---------------------------------------------------")
    print("press q or enter to exit")
    print("-------------------------")

    values = []   # Store user inputs

    while True:
        number = input("Enter value :  ")

        # Exit condition (empty or q)
        if number == "" or number == "q":
            print("-----------")
            print("   Done  ")
            break
            
        try:
            # Try converting input to integer
            num = int(number)
            values.append(num)

        except ValueError:
            try: 
                # If not int, try converting to float
                num = float(number)
                values.append(num)

            except ValueError:
                # If not a number at all, show error
                print("Not a valid number, try again")

    # After loop ends → calculate stats
    print("-----------")
    mean(values)
    print("-----------")
    median(values)
    print("-------------------")
    frequency(values)
