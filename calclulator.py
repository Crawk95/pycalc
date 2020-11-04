what = input("What kind of operation? (+, -, /, *): ")
a = float( input("Input first number?: ") )
b = float( input("Input second number: ") )
if what == "+":
    c = a + b
    print("Final: " + str(c))
if what == "-":
    c = a - b
    print("Final: " + str(c))
if what == "*":
    c = a * b
    print("Final: " + str(c))
if what == "/":
    c = a / b
    print("Final: " + str(c))