from sympy import Symbol, sympify
from sympy.plotting import plot
from sympy.core.sympify import SympifyError


def graph(expr1, expr2):
    x = Symbol('x')
    p = plot(expr1, expr2, (x, -20, 20), legend=True, show=False, title="Graph of Two Expressions in Terms of x")
    p[0].line_color = 'b'
    p[0].label = str(expr1)
    p[1].line_color = 'r'
    p[1].label = str(expr2)
    p.show()

if __name__ == "__main__":

    while True:
     try: 
        print("----------------------------------------------------")
        print("*** Graph Two Expressions (y in terms of x) ***")
        print("----------------------------------------------------")
        expr1 = sympify(input('Enter your first  expression in terms of x : '))
        print("--------------------------------------------")
        expr2 = sympify(input('Enter your second expression in terms of x : '))
        print("--------------------------------------------")
        graph(expr1, expr2)
        break 

     except (SympifyError, SyntaxError, ValueError):
        print("Invalid input, try again")
