'''
calculator that can perform the basic mathematical operations on
two fractions. 
'''
from  fractions import Fraction

def function_calc(f1, f2, p):
    if p == 1:
        print(f"{f1} + {f2} = {f1 + f2}")
        
    if p == 2:
        print(f"{f1} - {f2} = {f1 - f2}") 
        
    if p == 3:
        print(f"{f1} x {f2} = {f1 * f2}")
        
    if p == 4:
        print(f"{f1} / {f2} = {f1 / f2}")           
    
if __name__ =="__main__":
    print(" ------------------------------ ")
    print(" Let's calculate your fractions ")  
    print(" ------------------------------ ")
    
    while True:
        try:
            f1 = Fraction(input("Enter your first fraction  : "))
            print(" ------------------------------ ")
            f2 = Fraction(input("Enter your second fraction : "))
            print(" ------------------------------ ")
            p = int(input("Enter operation Add(1), Subtract(2), multiply(3), divide(4) : "))
            
            function_calc(f1, f2, p)
            
        except ValueError:
           print("Invalid choice or fraction")
        
        
        choice = input("Do you want to exit (y/n) : ") 
    
        if choice.upper == "Y" or choice.lower() == 'y':
          break
    
      