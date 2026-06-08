print("1.-----------------------------------------------------")
numbers = [1, 2, 3, 4, 5]
i = len(numbers) - 1
reversed_list = []
while i >= 0:
    reversed_list.append(numbers[i])
    i = i - 1
print(reversed_list)   

numbers = [1, 2, 3, 4, 5]
reversed_numbers = [] 
for i in range(len(numbers)-1, -1, -1):
    reversed_numbers.append(numbers[i])
print(reversed_numbers)

numbers = [1, 2, 3, 4, 5]
rever_num = numbers[::-1]
print(rever_num)

print("2.-----------------------------------------------------")
words = ["apple", "banana", "apple", "orange", "apple", "banana"]
new_dic = {}
for word in words:
    if word not in new_dic.keys():
        new_dic[word] = 1
    else:
        new_dic[word] = new_dic[word] + 1
print(new_dic)

print("3.-----------------------------------------------------")
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = []
i1 = 0
i2 = 0
while i1 < len(list1) and i2 < len(list2):
    if list1[i1] <= list2[i2]:
        result.append(list1[i1])
        i1 = i1 + 1
    else:
        result.append(list2[i2])
        i2 = i2 + 1
if i1 < len(list1):
    for j in range(i1, len(list1)):
        result.append(list1[j])
if i2 < len(list2):
    for j in range (i2, len(list2)): 
        result.append(list2[j])     
print(result)    

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
c = sorted(a+b)
print(f"Sorted: {c}")

print("4.-----------------------------------------------------")
print("A list contains numbers from 1 to 100, but one number is missing. Find the missing number efficiently.")
def find_missing(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    min = numbers[0]     
    for i in numbers:
        if i < min:
            max = i   
    missing = []
    for num in range(min + 1, max):
        if num not in numbers:
            missing.append(num)
    return missing        

numbers = [1, 2, 3, 20]
print(find_missing(numbers))

print("5.-----------------------------------------------------")

print("6.-----------------------------------------------------")

print("7.-----------------------------------------------------")

print("8.-----------------------------------------------------")

print("9.-----------------------------------------------------")

print("10.-----------------------------------------------------")