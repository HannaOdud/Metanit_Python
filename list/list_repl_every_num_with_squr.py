print("Replace Every Number with Its Square")
print("Modify the original list so that every number becomes its square.")

numbers = [1,2,3,4,5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * numbers[i]
print(numbers)    