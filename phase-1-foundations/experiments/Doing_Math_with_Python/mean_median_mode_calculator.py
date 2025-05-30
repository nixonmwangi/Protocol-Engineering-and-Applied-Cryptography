def mean(values):
        
        m = (sum(values))/(len(values))
        print(f"Mean : {m:.2f}") 

def median(values):
    if int((len(values)) % 2) != 0:
        l = int((len(values))/2)
        v = values[l]
        print(f"Median : {v}")
    else:
        l = int((len(values))/2)
        l2 = l - 1
        v1 = (values[l])
        v2 = (values[l2])
        v = (v1+v2)/2
        
        print(f"Median : {v}")
        



if __name__ == "__main__":
    print("---------------------------------------")
    print("*** Calculate Mean, Median and Mode ***")
    print("---------------------------------------")
    print("press q or enter to exit")
    print("-------------------------")

    values = []


    while True:

        number = input("Enter value :  ")

        if number == "" or number == "q":
            print("-----------")
            print("Done")
            break
            
            
        try:
        
           num = int(number)
           values.append(num)

        except ValueError:
            
            try: 
                num = float(number)
                values.append(num)

            except ValueError:
                 print("Not a valid number, try again")
    print("-----------")
    mean(values)
    print("-----------")
    median(values)
    print("-----------")
    print(f"Values : {values}")
        