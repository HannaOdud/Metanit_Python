print("Find Local Maximums")
print("A local maximum is greater than both neighboring elements.")
numbers = [2, 5, 3, 8, 6, 9, 4]
great_num = []
for i in range(1,len(numbers)-1):
    if numbers[i] > numbers[i+1] and numbers[i] > numbers[i-1]:
        great_num.append(numbers[i])
print(great_num)