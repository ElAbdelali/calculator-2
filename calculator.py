"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

queue = True

while queue:
    token = input("input an equation or press q to quit(seperate the operators and operands by a space)")
    token_list = token.split(' ')
    
    if token == 'q':
        print("Thank you for using the calculator!") 
        queue = False
    elif token_list[0] == 'square':
        print(float(token_list[1]) ** float(token_list[2]))
    elif token_list[0] == "cube":
        print(float(token_list[1]) + float(token_list[2]))
    elif token_list[0] == 'power':
        print(float(token_list[1]) ** float(token_list[2]))
    elif token_list[0] == "%":
        print(float(token_list[1]) + float(token_list[2]))
    elif token_list[0] == '/':
        print(float(token_list[1]) ** float(token_list[2]))
    elif token_list[0] == "*":
        print(float(token_list[1]) + float(token_list[2]))
    elif token_list[0] == '+':
        print(float(token_list[1]) ** float(token_list[2]))
    elif token_list[0] == "-":
        print(float(token_list[1]) + float(token_list[2]))
