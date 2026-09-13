print("1.--------------")
products = {
    "laptop": 1200,
    "phone": 800,
    "mouse": 25,
    "keyboard": 70,
    "monitor": 300
}
res = [key for key,value in products.items() if max(products, key=products.get)]
print(res[0])

print("2.-------------")
products = {
    "laptop": 1200,
    "phone": 800,
    "mouse": 25,
    "keyboard": 70,
    "monitor": 300,
    "tablet": 600
}
res = [key for key,value in sorted(products.items(), reverse=True, key=lambda item: item[1])]
print(res[0:3])
#{k: v for k, v in sorted(freq.items(), reverse=True, key=lambda item: item[1])}

print("3.-------------")
students = {
    "Anna": 85,
    "John": 62,
    "Mike": 91,
    "Kate": 74,
    "Tom": 55
}
res = [key for key,value in sorted(students.items(), reverse=True, key=lambda item: item[1])]
print(res)

print("4.-------------")
words = [
    "cat",
    "python",
    "developer",
    "code",
    "AI",
    "algorithm"
]
res = [word for word in sorted(words, key = len)]
print(res)

print("5.---------------")
prices = [
    1200,
    800,
    25,
    800,
    300,
    1200,
    600
]
set_price = set(prices)
uniq_prices = list(set_price)
res = [price for price in sorted(uniq_prices, reverse=True)]
print(res[1])

print("6.---------------")
students = {
    "Anna": 85,
    "John": 90,
    "Mike": 85,
    "Kate": 90,
    "Tom": 70
}
res = [key for key,value in sorted(students.items(), key=lambda item: item[1], reverse=True)]
print(res)

print("7.-----------------")
words = [
    "python",
    "java",
    "python",
    "c++",
    "java",
    "ruby",
    "python",
    "java"
] 
fq = {}
for word in words:
    fq[word] = fq.get(word, 0)+1
max_fq = max(fq.values())
print(max_fq)
res = [key for key,value in fq.items() if value == max_fq]
print(res)

print("8.-------------------")
students = {
    "Anna": [85, 90, 78],
    "John": [60, 72, 65],
    "Mike": [95, 88, 92],
    "Kate": [70, 75, 80],
    "Lisa": [90, 90, 85]
}
st_avg = {key: sum(value)/len(value) for key,value in students.items()}
print(st_avg)
res = [key for key,value in st_avg.items() if value == max(st_avg.values())]
print(res)

print("9.-----------------")
words = [
    "cat",
    "dog",
    "apple",
    "book",
    "banana",
    "car",
    "orange",
    "sun"
]
len_words = {}
for word in words:
    if len(word) in len_words:
        len_words[len(word)].append(word)
    else:
        len_words[len(word)] = [word]
print(len_words)
sorted_items = sorted(len_words.items(), key=lambda item:len(item[1]),reverse=True)
res = [key for key,value in sorted_items] 
print(res)

print("10.------------------")




#special = {key:value for key,value in products.items() if value < 700}
#print(special)
#res = [key for key,value in sorted(special,reverse = True)]