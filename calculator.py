from math import *

info = input("Would you like information? : ")
if info == "yes":
    print("+ = add")
    print("- = subtract")
    print("* = multiplication")
    print("/ = division")
    print("pow/power/p = raise to power")

while True:
    num1 = input("Enter your first number: ")
    if num1 == "stop":
        break
    num1 = float(num1)
    op = input("Enter your operator: ")
    num2 = float(input("Enter your second number: "))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "pow" or "power" or "p":
        print(pow(num1, num2))
    else:
        print("Something went wrong please try again")

print("Code finished")




