num = int(input("Write your num: "))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(f"Factorial: {fact}")