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

'''print("13. Use map() to add 20% tax to each price.")
prices = [100, 250, 80, 150]
def addTax(p):
    return (20 / 100) * p + p
res = list(map(addTax, prices))
print(res)'''

'''prices = [100, 250, 80, 150]
res = list(map(lambda p: p + p * (20/100), prices))
print(res)'''

'''print("14. Use filter() to keep only words with more than 5 letters.")
words = ["apple", "computer", "pen", "notebook", "car"]
res = list(filter(lambda w: len(w)>5, words))
print(res)'''

'''print("15. Use map() to convert each temperature to Fahrenheit.")
temperatures = [0, 10, 20, 30]
res = list(map(lambda t: t * 1.8 + 32, temperatures))
print(res)'''

'''print("16. Use filter() to keep only numbers divisible by 3.")
numbers = [6, 8, 9, 12, 14, 18, 20]
res = list(filter(lambda n: n%3 == 0, numbers ))
print(res)'''

'''print("17. Use filter() to remove all empty strings.")
words = ["apple", "", "banana", "", "orange"]
res = list(filter(lambda w: len(w)!=0, words))
print(res)'''

'''print("18. Use map() to create a list containing only the first letter of each word.")
words = ["Python", "Java", "C++", "JavaScript"]
res = list(map(lambda w: w[0], words))
print(res)'''

'''print("19. Use filter() to keep only even numbers. Use map() to multiply each remaining number by 10.")
numbers = [3, 8, 15, 20, 7, 12]
res1 = list(filter(lambda n: n%2==0, numbers))
print(res1)
res2 = list(map(lambda n: n*10, res1))
print(res2)'''

'''print("20. Use filter() to keep only names with more than 4 letters. Use map() to capitalize each remaining name.")
print("Sort the final list alphabetically. Print the result.")
names = ["wlice", "Bob", "charlie", "Eve", "daniel"]
res1 = list(filter(lambda n: len(n)>4, names))
print(f"Names with more then 3 letters: {res1}")
res2 = list(map(lambda n: n.title(), res1))
print(res2)
res2.sort()
print(res2)'''
