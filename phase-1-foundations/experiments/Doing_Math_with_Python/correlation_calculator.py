def correlation(set_1, set_2):
    # Mean
    # set 1 

    m1 = sum(set_1)/(len(set_1))

    # set 2

    m2 = sum(set_2)/(len(set_2))

    # deviation of set 1 (not squared yet))

    v1 = [x - m1 for x in set_1]
    
    # deviation of set2 (not squared yet))

    v2 = [y - m2 for y in set_2]
        
    # Numerator = sum of (dev1 * dev2)
    
    numerator = sum(n1 * n2 for n1, n2 in zip(v1, v2))

    # Denominator = sqrt(sum(dev1^2) * sum(dev2^2))

    denominator = (sum(d ** 2 for d in v1) * sum(d ** 2 for d in v2)) ** 0.5

    return numerator/denominator
    

    
    
   
    

if __name__ == "__main__":
    print("*--------------------------------------*")
    print("*** Find the Correlation Coefficient ***")
    print("*--------------------------------------*")
    print("Press Enter or 'q' to exit")
    print("--------------------------")
    print("Both sets should have same number of values")
    print("--------------------------------------------")
    
    

    set_1 = []
    set_2 = []
    count_1 = 1 
    count_2 = 1

    print("*** First set values ***")
    print("------------------------")

    while True:

        s_1 = input(f"Value {count_1} (press Enter/q to stop) : ")

        if s_1 == "" or s_1.lower() == "q":
           break 

        try:
            s1 = float(s_1)
            set_1.append(s1)
            count_1 += 1

        except ValueError:
            
            print("Invalid... Try again")
            continue
            
    print("-------------------------")
    print("*** Second set values ***")
    print("-------------------------")
    while True:  

        s_2 = input(f"Value {count_2} (press Enter/q to stop) : ")

        if s_2 == "" or s_2.lower() == "q":
           break
        
        try:
           s2 = float(s_2)
           set_2.append(s2)
           count_2 += 1

        except ValueError:
            
            print("Invalid... Try again")
            continue       

    if len(set_1) != len(set_2):
        print("Error: Both sets must have the same number of values!")
         
    else:
        print("---------------------------------") 
        print("Both sets collected successfully!")
        print("---------------------------------")
        
        c = correlation(set_1, set_2)
        
        print(f"The coefficient correlation : {c:.2f}")
        print("------------------------------------")

        
       

            
            

    