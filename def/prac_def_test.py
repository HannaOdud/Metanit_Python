print('Practice test func')

def do_operation(a, b, operation):
    result = operation(a,b)
    print(f"result = {result}")

def sum(a, b): return a + b
def multiply(a, b): return a * b

do_operation(5, 4, sum)
do_operation(5, 4, multiply)

print("Practice test func")
def sum(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a,b): return a * b

def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else: return multiply

operation = select_operation(1)
print(f"Operation: sum = {operation(2,6)}")
operation = select_operation(2)
print(f"Operation: subs = {operation(2,6)}")
operation = select_operation(3)
print(f"Operation: multi = {operation(2,6)}")
