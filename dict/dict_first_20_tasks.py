'''#1
#person = dict()
person = {
"name": "Anna",
"age": "30",
"city": "Kyiv"
}
print(person["name"])

#2
person["country"] = "Ukraine"
#3
person["age"] = 29
#4
del person["city"]
print(person)
#5 
#print(person["phone"])
print(person.get("phone"))
print(person.get("phone", "No phone"))'''

#6
'''cars = {
    "brand": "BMW",
    "model": "X5",
    "year": 2025
}
for key in cars:
    print(key)
    #OR
for key in cars.keys():
    print(key)
#7
print(cars.values())

#8
print(cars.items())

#9
print(cars.get("color"))

#10
print(cars.get("color", "Unknown"))'''

#11 Обчисли середню оцінку.
'''student = {
    "name": "Anna",
    "math": 95,
    "english": 88,
    "history": 91
}
st_val = student.values()
sum = 0
count = 0
for v in st_val:
    if type(v) == int:
        sum = sum + v
        count = count + 1
avg = sum / count
print(round(avg,2) )       

#12 and 13 Порахуй кількість значень.Порахуй кількість ключів.Без len().
count_value = student.values()
count_v = 0
for val in count_value:
    count_v = count_v + 1
print(count_v)
#OR
c_v = 0
for value in student.values():
    c_v = c_v + 1
print(c_v)

#14 Виведи тільки ключі,значення яких є числами.
for key, value in student.items():
    if type(value) == int:
        print(key)

#15 Виведи тільки рядкові значення.
for key,value in student.items():
    if type(value) == str:
        print(value) '''

#16 Створи словник телефонної книги.
phone_book = {
    "Ivan": 12345,
    "Olena":56789,
    "Anna": 14589
}
print(phone_book.get("Olena"))

#17 Замініть номер Івана.
phone_book["Ivan"] = 13456

#18 Додай нового користувача.
phone_book["Oleh"]= 14567
print(phone_book) 

#19 Видали Анну.
del phone_book["Anna"]
print(phone_book)

#20 Знайди найдорожчий фрукт. Не використовуй max().
prices = {
    "apple": 30,
    "banana": 25,
    "orange": 40,
    "kiwi": 80
}
max_val = float("-inf")
max_key = None
for key, value in prices.items():
    if value > max_val:
        max_val = value
        max_key = key
print(max_key)