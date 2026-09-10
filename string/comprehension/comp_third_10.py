print("1.-----------")
numbers = [3, 8, 11, 14, 17, 20, 23, 26, 30]
sq = [num**2 for num in numbers if num % 2 == 0]
print(sq)

print("2.-----------")
words = [
    "Python",
    "python ",
    " PYTHON",
    "Java",
    "java ",
    "C++",
    "Python"
]
new = {word.lower().strip(",.!?:; ") for word in words}
print(new)

print("3-----------")
students = {
    "Anna": 85,
    "John": 62,
    "Mike": 91,
    "Kate": 74,
    "Tom": 55,
    "Lisa": 88
}
res = {key:value for key,value in students.items() if value > 79} 
print(res)

print("4.-------------")
text = """
Python is powerful.
Python is popular.
Python is easy to learn.
"""
words = text.split()
print(words)
res = {word.lower().strip(",.!?:; ") for word in words}
print(res)

print("5.------------")
words = [
    "cat",
    "python",
    "developer",
    "code",
    "algorithm",
    "AI"
] 
res = { word:len(word) for word in words if len(word)>5 }
print(res)
#res = { key: len(key) for key in words if len(key) > 5}

print("6.------------")
groups = [
    [3, 8, 11],
    [14, 17, 20],
    [23, 26, 29]
]
res = [el for inner_list in groups for el in inner_list if el % 2 == 0]
print(res)


print("7.-----------")
products = {
    "laptop": 1200,
    "phone": 800,
    "mouse": 25,
    "keyboard": 70,
    "monitor": 300,
    "tablet": 600
}
new = {product:price for product,price in products.items() if price < 700}
print(new)
res = sorted(new, key = lambda product:new[product])
print(res)

print("8.------------")
words = [
    "apple",
    "banana",
    "apple",
    "kiwi",
    "banana",
    "apple",
    "orange",
    "kiwi",
    "banana"
]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0)+1
res = [key for key,value in freq.items() if value > 1]
print(res)


print("9.------------")
words = [
    "apple",
    "banana",
    "apple",
    "kiwi",
    "banana",
    "orange",
    "kiwi"
]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0)+1
ls = []
for word in words:
    if freq[word] == 1:
        ls.append(word)
        break
print(ls[0])

print("10.-------------")
words = [
    "Python",
    "python",
    "JAVA",
    "java",
    "python",
    "C++",
    "Java",
    "c++",
    "ruby"
]
norm = [word.lower().strip(",.!?:; ") for word in words]
print(norm)

#step2
freq = {}
for word in norm:
    freq[word] = freq.get(word, 0)+1

#step3
repeated = {key for key,value in freq.items() if value > 1}
print(repeated)

#step4
srt = sorted(repeated, key=lambda word:freq[word])
print(srt)

#step5
res = []
for word in norm:
    if freq[word] == 1:
        res.append(word)
        break
print(res[0])

