'''print("1. Create a copy of the list using copy().  Add 20 to the copied list only. Print both lists")
numbers = [5, 10, 15]
new_l = numbers.copy()
new_l.append(20) 
print(f"New: {new_l}")
print(numbers)

new_2 = new_l[:]
new_2.append(25)
print(new_2)'''

'''print("2. Find the Second Occurrence")
print("Use index() with the start parameter to find the second occurrence of b")
letters = ["a", "b", "c", "b", "d"]
first = letters.index("b")
second = letters.index("b", first + 1)
print(letters[:second])
print(first)
print(second) ''' 

'''print("3. Sort in Descending Order")
scores = [82, 95, 71, 88, 90]
scores.sort(reverse=True)
print(scores)'''


'''print("4. Sort the words by their length using the key parameter.")
words = ["elephant", "cat", "giraffe", "dog", "lion"]
words.sort(key = len)
print(words)'''

'''print("5. Extend a List. Add all elements from odd to even.")
even = [2, 4, 6]
odd = [1, 3, 5]
even.extend(odd)
print(even)'''

'''print("6. Remove All Occurrences of 2. Use a loop together with remove(). ")
numbers = [2, 4, 2, 6, 2, 8]
for n in numbers:
    if n == 2:
       numbers.remove(n)
print(numbers)'''

'''print("7. Remove the element at index 2 using pop(). Print the removed value.")
colors = ["red", "green", "blue", "yellow"]
colors.pop(2)
print(colors)'''


'''print("8. Convert the string into a list of characters using list()")
text = "Python"
print(list(text))'''

'''print("9. Reverse Without Changing the Original")
numbers = [10, 20, 30, 40]
n = numbers.copy()
n.reverse()
print(n)'''

'''print("10. Nested Lists. Create the following list:")
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(matrix[0])
print(matrix[-1])
print(matrix[1][1])'''

'''print("11. Print the sum of each row. ")
matrix = [
    [4, 6],
    [10, 5],
    [8, 7]
]
for i in range(len(matrix)):
    print(sum(matrix[i]))'''

'''print("12. Convert Strings to Integers. Use map() and list() to convert all elements into integers. ")
numbers = ["10", "20", "30", "40"]
res = map(int, numbers)
print(res)
print(list(res))'''

'''print("13. Use filter() to create a new list containing only even numbers. ")
numbers = [3, 8, 10, 5, 12, 7]
def is_even(num):
    return num % 2 == 0
f = filter(is_even,numbers)
print(list(f))'''

'''print("14. Sort the words alphabetically without considering uppercase and lowercase letters. ")
words = ["Banana", "apple", "Orange", "grape"]
sorted_words = sorted(words, key = str.lower)
print(sorted_words)'''

'''print("15. Find the index of 20 starting from index 2.")
numbers = [10, 20, 30, 20, 40, 20]
print(numbers.index(20, 2))'''

'''print("16. Working with Nested Lists")
students = [
    ["Alice", 91],
    ["Bob", 78],
    ["Charlie", 85]
]
print(students[1][1])
print(students[2][0])'''

'''print("17. Add a New Row using append().")
matrix = [
    [1, 2],
    [3, 4]
]
matrix.append([5, 6])
print(matrix)'''

'''print("18. Convert the tuple into a list. ")
numbers = (5, 10, 15, 20)
t = list(numbers)
print(t)
print(numbers)'''

'''print("19. Mixed Sorting")
cities = ["Rome", "Amsterdam", "Oslo", "Cairo", "Paris"]
c1 = sorted(cities) #alf
print(c1)
c2 = sorted(cities, key = len)
print(c2)
c3 = sorted(cities, reverse=True)
print(c3)'''

'''print("20. Combined Challenge")
numbers = [14, 7, 25, 7, 18, 7]
c = numbers.copy()
numbers.remove(7)

print(numbers)'''

print("Bonus challenge.")
employees = [
    ["Alice", "HR", 3200],
    ["Bob", "IT", 4100],
    ["Mharlie", "Sales", 3700],
    ["Diana", "IT", 4500]
]
for em in employees:  
    print(em[0])

s_D =employees[3][2]
print(s_D)
employees.append(["Lana", "Nurse", 3500])
print(employees)
c1 = sorted(employees) #alfabet
print(c1)
c2 = sorted(employees, key=lambda employee: employee[2])
print(c2)

print("Print only employees whose salary is greater than 4000 (using filter())")
high_s = filter(lambda em: em[2]>4000, employees)
for em in high_s:
    print(em)
print("Create a list containing only employee names (using map())")
name = list(map(lambda em: em[0],employees))
print(name)