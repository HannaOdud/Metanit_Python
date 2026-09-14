print("1.---------------------------------")
# Знайди назву найдешевшого товару.
products = {
    "laptop": 1200,
    "phone": 800,
    "mouse": 25,
    "keyboard": 70,
    "monitor": 300,
    "tablet": 600
}
res = min(products, key=products.get)
print(res)
#OR
res2 = [key for key,value in sorted(products.items(), key=lambda item:item[1])]
print(res2[0])

print("2.-------------------------------")
products = {
    "laptop": 1200,
    "phone": 800,
    "mouse": 25,
    "keyboard": 70,
    "monitor": 300,
    "tablet": 600,
    "webcam": 50
}
res = [key for key,value in sorted(products.items(), key=lambda item: item[1])]
print(res[0:3])

print("3.------------------------------")
scores = [
    85,
    92,
    76,
    92,
    88,
    95,
    85,
    95
]
no_duplicate = list(set(scores))
print(no_duplicate)
sort_sco = sorted(no_duplicate, reverse=True)
print(sort_sco)
print(sort_sco[1])
#OR
res = [item for item in sorted(no_duplicate, reverse=True) ]
print(res[1])

print("4.--------------------------------")
words = [
    "cat",
    "python",
    "dog",
    "algorithm",
    "book",
    "code",
    "AI",
    "banana"
]
print(words)
#res = [word for word in sorted(words, key=len)]
res = sorted(words, key=lambda item:(-len(item),item))
print(res)

print("5.-----------------------------")
numbers = [
    5,
    8,
    3,
    7,
    8,
    2,
    3,
    5
]
repeated = []
checked = []
for num in numbers:
    if num in checked:
        repeated.append(num)
        break
    else:
        checked.append(num)
print(repeated[0])