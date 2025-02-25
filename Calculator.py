num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
add = num2 + num1
div = num1 / num2
mul = num1 * num2
sub = num1 - num2
um = input("Addition, Subtraction, Multiplication, or Division: ")
if um == "addition":
    print(f"{num1} + {num2} = {add}")
elif um == "Addition":
    print(f"{num1} + {num2} = {add}")
elif um == "subtraction":
    print(f"{num1} - {num2} = {sub}")
elif um == "Subtraction":
    print(f"{num1} - {num2} = {sub}")
elif um == "multiplication":
    print(f"{num1} x {num2} = {mul}")
elif um == "Multiplication":
    print(f"{num1} x {num2} = {mul}")
elif um == "division":
    print(f"{num1} ÷ {num2} = {div}")
elif um == "Division":
    print(f"{num1} ÷ {num2} = {div}")
