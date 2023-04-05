"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

queue = True

while queue:
    token = input('Please enter either [square, cube, power, %, /, *, +, -] followed by values seperated by spaces or press q to quit: ')
    token_list = token.split(' ')
    
    if token == 'q':
        print("Thank you for using the calculator!") 
        queue = False
    elif token_list[0] == 'square':
        print(square(float(token_list[1])))
    elif token_list[0] == "cube":
        print(cube(float(token_list[1])))
    elif token_list[0] == 'power':
        print(power(float(token_list[1], float(token_list[2]))))
    elif token_list[0] == "%":
        print(mod(float(token_list[1]), float(token_list[2])))
    elif token_list[0] == '/':
        print(divide(float(token_list[1]), float(token_list[2])))
    elif token_list[0] == "*":
        print(multiply(float(token_list[1]), float(token_list[2])))
    elif token_list[0] == '+':
        print(add(float(token_list[1]), float(token_list[2])))
    elif token_list[0] == "-":
        print(subtract(float(token_list[1]), float(token_list[2])))
    else:
        continue
