print("Count Increasing Pairs")
print("Count how many adjacent pairs satisfy:")
numbers = [1,4,3,5,6]
count = 0
for i in range(len(numbers)-1):

    if numbers[i] < numbers[i+1]:
        count = count + 1
print(count)        