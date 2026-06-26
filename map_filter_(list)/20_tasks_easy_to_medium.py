#Python Practice – map() and filter()

'''print("1. Use map() to create a new list where every number is multiplied by 2.")
numbers = [2, 4, 6, 8]
new_num = list(map(lambda num: num * 2, numbers))
print(new_num)'''

'''print("2. Use map() to add 10 to every number.")
numbers = [5, 12, 20, 7]
res = list(map(lambda n: n + 10, numbers))
print(res)'''

'''print("3. Use map() to convert every number into a string.")
numbers = [1, 2, 3, 4, 5]
res = list(map(lambda n: str(n), numbers))
print(res)'''

'''print("4. Use map() to convert all names to uppercase.")
names = ["alice", "bob", "charlie"]
res = list(map(lambda n: n.upper(), names))
print(res)'''

'''print("5. Use map() to create a list containing the length of each word.")
words = ["apple", "pear", "banana", "kiwi"]
res = list(map(lambda w: len(w), words))
print(res)'''

'''print("6. Use map() to create a list of squares.")
numbers = [3, 5, 7, 9]
res = list(map(lambda n: n*n, numbers))
print(res)'''

'''print("7.  Use filter() to keep only even numbers.")
numbers = [2, 5, 8, 11, 14, 17]
res = list(filter(lambda n: n%2==0, numbers))
print(res)'''

'''print("8. Use filter() to keep only odd numbers.")
numbers = [4, 7, 9, 10, 13, 16]
res = list(filter(lambda n: n%2!=0, numbers))
print(res)'''

'''print("9. Use filter() to keep only numbers greater than 20.")
numbers = [12, 25, 7, 30, 18, 45]
res = list(filter(lambda n: n>20, numbers))
print(res)'''

'''print("10. Use filter() to keep only words with 3 letters.")
words = ["cat", "elephant", "dog", "notebook", "pen"]
res = list(filter(lambda w:len(w)==3, words))
print(res)'''

'''print("11. Use filter() to create a list containing only positive numbers.")
numbers = [-5, 10, -3, 8, -1, 12]
res = list(filter(lambda n: n >= 1, numbers))
print(res)'''

'''print("12. Use map() to capitalize the first letter of every name.")
names = ["john", "emma", "lucas", "sophia"]
def cap_first(w):
    w = w.title()
    return w
res = list(map(cap_first, names))
print(res)'''

'''names = ["john", "emma", "lucas", "sophia"]
res = list(map(lambda w: w.title(), names))
print(res)'''

print("13. ")


