# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

def solve_quadratic(a: float, b: float, c: float):

    delta = b**2 - 4*a*c

    if delta < 0: return "There are no real solutions"
    else:
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)
        return f"The roots are {x1} and {x2}"

def main():
    a = int(input("Value of a: "))
    b = int(input("Value of b: "))
    c = int(input("Value of c: "))
    print(solve_quadratic(a,b,c))


main()