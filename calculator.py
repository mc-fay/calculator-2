"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
equation = input("Enter your equation > ") #ex "+ 1 3"
tokens = equation.split(' ') # ex ['add', '1', '3']
if tokens[0] == 'q':
    2 + 1
if tokens[0] == '+':
    add(tokens[1], tokens[2])
if tokens[0] == '-':
    subtract(tokens[1], tokens[2])
if tokens[0] == '*':
    multiply(tokens[1], tokens[2])
if tokens[0] == '/':
    divide(tokens[1], tokens[2])
if tokens[0] == 'square':
    square(tokens[1], tokens[2])
if tokens[0] == 'cube':
    cube(tokens[1], tokens[2])
if tokens[0] == 'pow':
    power(tokens[1], tokens[2])
if tokens[0] == 'mod':
    mod(tokens[1], tokens[2])
