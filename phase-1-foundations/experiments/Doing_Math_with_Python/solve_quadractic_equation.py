'''
Solving quadratic equation with different value:
'''

def quad_math(a, b, c):
    try:
        d = (b**2 - (4*a*c))**0.5
        e = (-b - d)/(2*a)
        f = (-b + d)/(2*a)

        print(f"Answer x1 = {e:.2f}")
        print(f"Answer x2 = {f:.2f}")

    except ValueError:
        print("Please input a valid number") 

if __name__ == "__main__":

    try:
   
       input("Put you quadractic values a, b and c ")
       a = input("Enter a : ")
       b = input("Enter b : ")
       c = input("Enter c : ")
   
       quad_math(float(a), float(b), float(c))

    except ValueError:
        print("Please input a valid number")