print("Remove Negative Numbers")
print("Create a new list containing only non-negative numbers.")

numbers = [4, -2, 7, -5, 8, -1]
positive = []
for i in numbers:
    if i > 0:
        positive.append(i)
print(positive)        