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