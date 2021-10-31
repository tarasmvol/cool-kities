import cmath
from cmath import sqrt
def solve_quadric_equation(a, b, c):
    try:
        x2 = (-b+sqrt(b**2-4*a*c))/(2*a)
        x1 = (-b-sqrt(b**2-4*a*c))/(2*a)
    except ZeroDivisionError:
        return "Zero Division Error"
    except TypeError:
        return "Could not convert string to float"
    else:
        return f"The solution are x1={x1} and x2={x2}"