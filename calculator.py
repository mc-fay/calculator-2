"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

# while tokens[0] != 'q':
while True:
    equation = input("Enter your equation > ") #ex "+ 1 3"
    tokens = equation.split(' ') # ex ['+', '1', '3']
    print("TOKENS: ", tokens)

    if tokens[0] != 'q':
        tokens[1] = float(tokens[1])

    if len(tokens) == 3:
        tokens[2] = float(tokens[2])

    if tokens[0] == 'q':
        break

    if tokens[0] == '+':
        result = add(tokens[1], tokens[2])
        print(result)

    if tokens[0] == '-':
        result = subtract(tokens[1], tokens[2])
        print(result)

    if tokens[0] == '*':
        result = multiply(tokens[1], tokens[2])
        print(result)

    if tokens[0] == '/':
        result = divide(tokens[1], tokens[2])
        print(result)

    if tokens[0] == 'square':
        result = square(tokens[1])
        print(result)

    if tokens[0] == 'cube':    
        result = cube(tokens[1])
        print(result)

    if tokens[0] == 'pow':
        result = power(tokens[1], tokens[2])
        print(result)

    if tokens[0] == 'mod':
        result = mod(tokens[1], tokens[2])
        print(result)
