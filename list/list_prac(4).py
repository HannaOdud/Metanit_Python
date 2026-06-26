#Python Lists Practice – Advanced List Methods
'''print("1. Copy a list")
#Create a copy of the list using copy().
#Add "yellow" to the copied list only.
#Print both lists.
colors = ["red", "green", "blue"]
c = colors.copy()
c.append("yellow")
print(colors)
print(c)'''

'''print("2. Independent Copy. Create a list of five numbers.Make a copy. Remove one number from the copied list.Show that the original list remains unchanged. ")
num = [1, 2, 3, 4, 5]
num2 = num[:]
num2.remove(2)
print(num)
print(num2)
    #OR
num3 = num.copy()
num3.remove(1)
print(num3)
print(num)  '''

'''print("3. Find the Second Occurrence. Use index(value, start) to find the second occurrence of 'dog'. ")
animals = ["cat", "dog", "bird", "dog", "rabbit"]
d_i = animals.index("dog", 2)
print(d_i)'''

'''print("4. Find the Next Duplicate. Find the second occurrence of 4.")
numbers = [8, 4, 6, 4, 2, 4]
f_o = numbers.index(4)
s_o = numbers.index(4, f_o + 1)
print(s_o)'''

'''print("5. Sort the list from highest to lowest. ")
scores = [78, 95, 81, 67, 88]
scores.sort(reverse=True)
print(scores)'''

'''print("6. Sort the list in reverse alphabetical order.")
fruits = ["apple", "banana", "orange", "kiwi"]
fruits.sort(reverse=True)
print(fruits)'''

'''print("7. Sort the list by the length of each word.")
words = ["table", "pen", "notebook", "book", "computer"]
words.sort(key=len)
print(words)'''

'''print("8. Sort the words according to their last letter. Hint: Use the key parameter. ")
words = ["banana", "apple", "kiwi", "orange"]
words.sort(key=lambda word: word[-1])
print(words)
#OR
def last_let(word):
    return word[-1]
words.sort(key=last_let)
print(words)'''

'''print("9.Use reversed() to print the numbers in reverse order. Do not modify the original list.")
numbers = [10, 20, 30, 40, 50]
n = list(reversed(numbers)) #list()
print(n)'''

'''print("10. Convert to a List")
text = "Programming"
l = list(text)
print(l)'''

'''print("11. Convert the tuple into a list. Add another number to the new list.")
data = (5, 10, 15, 20)
d_l = list(data)
d_l.append(25)
print(d_l)'''

'''print("12. Convert Strings to Integers  Use map() to convert every element into an integer. Print the resulting list.")
numbers = ["12", "8", "25", "30"]
res = list(map(lambda el: int(el) , numbers))
print(res)'''

'''print("13. Use map() to create a new list with all names in uppercase. ")
names = ["alice", "bob", "charlie"]
res = list(map( lambda name: name.upper(), names ))
print(res)'''

'''names = ["alice", "bob", "charlie"]
def toUpper(name):
    return name.upper()
res = list(map(toUpper, names))
print (res)'''

'''print("14. Use map() to create a new list containing the square of every number.")
numbers = [2, 4, 6, 8]
res = list(map(lambda num: num*num, numbers))
print(res)'''

'''print("15. Use filter() to create a list containing only even numbers.")
numbers = [3, 6, 9, 12, 15, 18]
res = list (filter(lambda num: num % 2 == 0, numbers))
print(res)'''

'''numbers = [3, 6, 9, 12, 15, 18]
def is_even(num):
    return num % 2 == 0
res = list(filter(is_even, numbers))
print(res)'''

'''print("16. Use filter() to keep only words with more than five letters.")
words = ["pen", "computer", "book", "notebook", "cat"]
def is_five_letter(word):
    return len(word) >= 5
res = list(filter(is_five_letter, words))
print(res)'''
'''words = ["pen", "computer", "book", "notebook", "cat"]
res = list(filter(lambda word: len(word)>= 5, words))
print(res)'''

'''print("17. Nested Lists")
matrix = [
    [5, 8],
    [10, 15],
    [20, 25]
]
print(f"the first row: {matrix[0]}")
print(f"the second row: {matrix[1]}")
print(f"the number 25: {matrix[2][1]}")'''

'''print("18. Student Records")
students = [
    ["Alice", 85],
    ["Bob", 91],
    ["Charlie", 78]
]
print(f"Bob: {students[1][1]}")
print(f"Name: {students[2][0]}")'''

'''print("19. Update a Nested List. Change the price of 'Mouse' to 30")
products = [
    ["Laptop", 1200],
    ["Mouse", 25],
    ["Keyboard", 75]
]
products[1][1] = 30
print(products)'''

print("20. Mixed chalenge")
numbers = ["15", "8", "23", "42", "7", "18"]
int_num = list(map(lambda num: int(num), numbers ))
print(int_num)
int_num.sort(reverse=True)
print(int_num)
less_20 = list(filter(lambda num: num < 20, int_num))
print(less_20)
less_20.reverse()
print(less_20)
copy_less_20 = less_20.copy()
print(copy_less_20)