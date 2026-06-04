print("1.Create a list containing five favorite fruits and print the entire list.")
fruits = ["banana", "coconut", "apple","strawberries","kiwi"]
print(fruits)

print("2.Access List Elements(first/last) ")
numbers = [10, 20, 30, 40, 50]
num_f = print(numbers[0])
num_l = print(numbers[len(numbers)-1])

print("3.Modify a list")
colors = ['red', 'blue', 'green']
index = colors.index("blue")
colors[index] = "yellow"
print(colors)

print("4. Add and Remove Elements")
animals = ['cat', 'dog', 'rabbit']
animals.append("hamster") 
animals.remove("dog")
print(animals)

print("5. Find List Information")
scores = [78, 92, 85, 67, 99, 88]
print(len(scores))
print(max(scores))
print(min(scores))

print("6. Sum Even Numbers. Calculate and print the sum of all even numbers in the list.")
numbers = [3, 8, 12, 5, 7, 10, 15]
sum = 0
for i in numbers:
    if i % 2 == 0:
        sum = sum + i
print(sum)

print("7. Create a New List with List Comprehension")
numbers = [1, 2, 3, 4, 5]
new_list = []
for i in numbers:
    act = i * i 
    new_list.append(act)
print(new_list)    

print("8. Remove Duplicates. Create a new list containing only unique values while preserving the original order.")
'''numbers = [1, 2, 2, 3, 4, 4, 5, 1]
my_set = set(numbers)
my_list = list(my_set)
print(my_list)'''

numbers = [1, 2, 2, 3, 4, 4, 5, 1]  
new_list = []
for num in numbers:
    if num not in new_list:
        new_list.append(num)
print(new_list)

print("9. Find the Second Largest Number. Find the second largest distinct number without using sort(). ")
numbers = [12, 45, 7, 34, 89, 89, 23]
max_num = max(numbers)

for num in numbers:
    if num == max_num:
        numbers.remove(num)
sec_max = max(numbers)
print(sec_max)