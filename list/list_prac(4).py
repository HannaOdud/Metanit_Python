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

#here is problem
'''print("8. Sort the words according to their last letter. Hint: Use the key parameter. ")
words = ["banana", "apple", "kiwi", "orange"]
for word in words:
    words.sort(word[-1])
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

print("12. Convert Strings to Integers  Use map() to convert every element into an integer. Print the resulting list.")
numbers = ["12", "8", "25", "30"]