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
    if word not in new_dic.keys:
        new_dic[word] = 1
    else:
        new_dic[word] = new_dic[word] + 1

print(new_dic)



print("3.-----------------------------------------------------")

print("4.-----------------------------------------------------")

print("5.-----------------------------------------------------")

print("6.-----------------------------------------------------")

print("7.-----------------------------------------------------")

print("8.-----------------------------------------------------")

print("9.-----------------------------------------------------")

print("10.-----------------------------------------------------")