print("Калькулятор")
def calculator(a, b, operation):
    if operation == "+":
        print(add(a, b))
    elif operation == "-":
        print(subtract(a,b))
    elif operation == "*":
        print (multiply(a,b))
    elif operation == "/":
        print( divide(a, b))
    else: print ("Wrong operation!")
def add(a,b):
    return a + b
def subtract(a,b):
    return (a - b)
def multiply(a, b):
    return a * b
def divide (a, b):
    return a / b

calculator(2, 5, "*")