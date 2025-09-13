#calculate the Range, Variance and Standard Deviation
def range(values):
    if not values:
        return None
        
    lowest = min(values)
    highest = max(values)

    delta = highest - lowest

    return delta, highest, lowest

def variation(values):
    if not values:
        return None
    #Mean

    l = len(values)
    s = sum(values)
    mean = (s/l)
    print("-------------")
    print(f"Mean: {mean}")
    print("-------------")

    #Differences
    diff = []

    for v in values:
        d = mean - v
        diff.append(d)

    #Variance

    squared_diff = []

    for d in diff:
        squared_diff.append(d**2)

    variance = float(sum(squared_diff)/len(values))
   
    #Standard variance

    std = variance**0.5

    return variance, std

        
        
    

if __name__ == "__main__":
    print("-----------------------------------------------------------------------------------")
    print("**Calculate the Range, Variance, Standard deviation and  Coefficient correlation**")
    print("-----------------------------------------------------------------------------------")
    print("Press Enter or 'q' to finish input")
    print("-----------------------------------")

    values = []

    while True:
        
        v = input("Enter value : ")
        print("---------------")

        if v == "" or v.lower() == "q":
            print("Done")
            print("------")
            break

        try:
            value = int(v)
            values.append(value)

        except ValueError:
            try:
                value = float(v)
                values.append(value)

            except:
                print("Invalid input, please enter a number")
                continue

    delta, highest, lowest = range(values)
    variance, std = variation(values)
    print("--------------------------------------------------------")
    print(f"The Range is {delta} with highest value {highest} and lowest values {lowest}")
    print("--------------------------------------------------------")
    print(f"Variance           : {variance:.2f}")
    print("--------------------------------------")
    print(f"Standard deviation : {std:.2f}")
    print("--------------------------------------")
            
        

        