"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
equation = input("Enter your equation > ") #ex "+ 1 3"
tokens = equation.split(' ') # ex ['add', '1', '3']

