print("1.---------------------")
# Створи через list comprehension список квадратів усіх чисел.
numbers = [1, 2, 3, 4, 5, 6]
squares = [number ** 2 for number in numbers]
print(squares)

print("2.--------------------")
numbers = [3, 8, 11, 14, 17, 20, 23, 26]
evens = [number for number in numbers if number%2 == 0]
print(evens)

print("3.-------------------")
words = ["cat", "python", "book", "developer"]
lengths = [len(word) for word in words]
print(lengths)

print("4.-------------------")
words = ["apple", "cat", "banana", "dog", "python"]
res = [word.upper() for word in words if len(word) > 4]
print(res)

print("5.-------------------")
words = ["apple", "banana", "apple", "kiwi", "banana", "orange"]
res = {len(word) for word in words} 
print(res)

print("6.-------------------")
words = ["cat", "house", "python", "developer"]
res = {word: len(word) for word in words}
print(res)

print("7.------------------")
numbers = [4, 7, 10, 13, 16, 19, 22]
res = {number: number**2 for number in numbers if number%2 == 0}
print(res)

print("8.-----------------")
text = "Python is a powerful programming language"
words = text.split()
res = [word for word in words if len(word) > 4]
print(res)

print("9.-----------------")
squares_gen = (number**2 for number in range(1,11))
print(next(squares_gen))
print(next(squares_gen))
print(next(squares_gen))
print(next(squares_gen))


print("10.----------------")
words = [
    "apple",
    "banana",
    "apple",
    "kiwi",
    "banana",
    "orange",
    "kiwi"
]
set_comp = {word for word in words if len(word) >= 5}
print(set_comp)
dict_comp = {word:len(word) for word in words}
print(dict_comp)

