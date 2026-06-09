print("Create a new list where all even numbers come first and all odd numbers come after them.")
'''numbers = [7, 2, 9, 4, 1, 8, 6, 3]
new_list = []
for n in numbers:
    if n % 2 == 0:
        new_list.append(n)
print(new_list) 
for num in numbers: 
    if num % 2 != 0:
        new_list.append(num)
print(new_list)  '''

'''numbers = [7, 2, 9, 4, 1, 8, 6, 3]
list1 = []
f_list = []
t_list = []
for n in numbers:
    if n % 2 == 0:
        list1.append(n)
print(list1) 
list2 = []
for n in numbers:
    if n % 2 != 0:
        list2.append(n)
print(list2)
f_list = list1 + list2
print(f_list)
list1.extend(list2)
print(f"Extended: {list1}")'''

numbers = [7, 2, 9, 4, 1, 8, 6, 3]
even = []
odd = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
even.extend(odd)
print(even)        
