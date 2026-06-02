print("Intro to lambda")
message = lambda: print("Hello here")
message()
print("-----*-----*-----*-----*-----*-----")
square = lambda n: n * n
print(f"Square of 4 = {square(4)}")
print(f"Square of 5 = {square(5)}")
print("-----*-----*-----*-----*-----*-----")
sum = lambda a,b: a + b
print(f"Sum = {sum(4, 5)}")
print(f"Sum = {sum(6, 5)}")
print("-----*-----*-----*-----*-----*-----")
def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")

do_operation(5, 4, lambda a, b: a + b)    
do_operation(5, 4, lambda a, b: a * b) 
print("-----*-----*-----*-----*-----*-----")
def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a-b
    else: return lambda a, b: a * b

operation = select_operation(1)
print(f"Operation sum = {operation(10, 6)}")
operation = select_operation(1)
print(f"Operation subs = {operation(10, 6)}")
operation = select_operation(1)
print(f"Operation multi = {operation(10, 6)}")