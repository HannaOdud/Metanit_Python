print("Replace Every Even Number with Zero")
numbers = [1,2,3,4,5,6]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = 0
print(numbers)        