'''print("1. Delete the third element using del.")
numbers = [5, 10, 15, 20, 25]
del numbers[2]
print(numbers)'''


'''print("2. Delete the last three elements using slicing with del.")
letters = ["A", "B", "C", "D", "E", "F"]
del letters[-3:]
print(letters)'''

'''print("3. Create a new list containing all elements using the + operator. ")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

#1
list1 = list1 + list2
print(list1)

#2 
list1.extend(list2)
print(list1)'''

'''print("4.Create a list containing Python three times using the * operator.")
ls = ["Python"]
n_ls = ls * 3
print(n_ls)'''

'''print("5. Check whether banana is in the list. ")
fruits = ["apple", "banana", "orange"]
for f in fruits:
    if f == "banana":
        print(f)'''

'''fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    if fruits[i] == "banana":
        print(fruits[i])'''

'''print("6. Check whether yellow is not in the list. ")
colors = ["red", "blue", "green"]
if "yellow" not in colors:
    print(True)'''

'''print("7. List Slicing")
numbers = [10,20,30,40,50,60]
first_three = numbers[:3]
print(first_three)
last_two = numbers[-2:]
print(last_two)
every_two = numbers[0: -1: 2]
print(every_two)'''

'''print("8. Reversing with Slicing")
print("Without using reverse(), print the list in reverse order.")
numbers = [1,2,3,4,5]
rev = numbers[::-1]
print(rev)'''

'''print("9. Replace the last two elements with: 100,200]  ")
numbers = [1,2,3,4,5]
numbers[-2:] = [100,200]
print(numbers)'''

'''print("10. Assignment vs Copy ")
a = [1,2,3]
b = a
b.append(4)
print(a)
print(b)'''

'''print(" 11.Copy Using Slicing ")
a = [1,2,3]
b = a[:]
b.append(4)
print(a)
print(b)'''

'''print(" 12.Find the total using sum() ")
numbers = [5,10,15,20]
s = sum(numbers)
print(s)'''

'''print(" 13. Use any() to determine whether the list contains at least one non-zero value. ")
values = [0,0,3,0]
v = any(values)
print(v)'''

'''print("15. Enumerate ")
animals = ["cat","dog","rabbit"]
a = enumerate(animals)
print(list(a))'''

'''print("16. Use zip() to print each student's name and score. ")
names = ["Alice","Bob","Charlie"]
scores = [85,92,78]
n = zip(names, scores)
print(list(n))'''

'''print("17. list comprehension")
print("Create a new list containing the squares of numbers from 1 to 10 using a list comprehension.")
numbers = [ x **2 for x in range(1, 11)]
print(numbers)'''

'''print("18. Create a new list containing only numbers greater than 5. ")
numbers = [3,8,1,10,6,5]
n = [x for x in numbers if x > 5]
print(n)'''

'''print("19. Create a new list where every word is uppercase using a list comprehension.")
words = ["python","java","c++","go"]
n = [word.upper() for word in words]
print(n)'''

print("20. Mixed Challenge")
numbers = [4,8,15,16,23,42]
del numbers[0]
print(numbers)
numbers = numbers + [50, 60]
print(numbers)
if 23 in numbers:
    print (True)
is_23_present = 23 in numbers
print(is_23_present)
print(numbers[::2])
s = sum(numbers)
print(s)
new_l = [i*2 for i in numbers]
print(numbers)
print(new_l)