import numpy as np
from sympy import lambdify, symbols, Interval
from typing import Callable

def get_user_function():
    while True:
        try:
            expression = input("Enter a mathematical function f(x): ")
            # Create a lambda function using lambdify
            x = symbols('x')
            user_function = lambdify(x, expression, 'sympy')
            return user_function
        except Exception as e:
            print(f"Error: {e}. Please enter a valid mathematical function.")

def get_user_input(message, input_type=float, min_value=None, max_value=None):
    while True:
        try:
            user_input = input_type(input(f"{message}: "))
            if (min_value is not None and user_input < min_value) or (max_value is not None and user_input > max_value):
                raise ValueError(f"Input must be between {min_value} and {max_value}.")
            return user_input
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid input.")

def bissection_method(f:Callable) -> None:
    precision = get_user_input("Precision", float, min_value=0.000000000001)
    a = get_user_input("a", float)
    b = get_user_input("b", float)
    interval = Interval(a,b)
    img:float = 0
    p:float = b - a
    center:float = 0
    i:int = 0
    x = symbols('x')
    #TODO : Continuity Check
    
    #**Increase Check
    increasing_function = f(b) - f(a)
    if increasing_function <= 0:
        print(f"The function is not increasing in the interval [{a}, {b}].")
        return
    #**Logic
    while (p > precision):
        if f(a)*f(b) < 0:
            center:float = (a + b) / 2
            if f(center) > 0 :
                b = center
                center:float = (a + b) / 2
                print(f"{i} ) << Right Shift [{a},{b}] | x = {center} | f(x) = {f(center)} ")
                i+=1
            if f(center) < 0:
                a = center
                center:float = (a + b) / 2
                print(f"{i} ) >> Left Shift [{a},{b}] | x = {center} | f(x) = {f(center)} ")
                i+=1
        else:
            print(f"Their is no solution in the interval [{a},{b}].")
            return
        p = b - a
    print(f"\nmidpoint : {center}\nf({center}) = {f(center)}")

#TODO : Methode de Newton-Raphson

if __name__ == "__main__":
    #!test
    f = get_user_function()
    bissection_method(f)
