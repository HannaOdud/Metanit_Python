'''#1
book = {
    "title": "Harry Potter",
    "author": "J. K. Rowling",
    "year": 1997
}
print(book["author"])

#2 Додай ключ:
book["pages"] = 320
print(book)

#3 Зміни рік видання на 1998.
book["year"] = 1998
print(book)

#4 Видали ключ "pages".
del book["pages"]
print(book)

#5 Перевір, чи є ключ "publisher".
print(book.get("publisher", "No such key"))

#6  Виведи всі ключі через цикл.
for key in book.keys():
    print (key)

#7 Виведи всі значення через цикл.
for key, value in book.items():
    print(key, value)

#8 Виведи всі пари у форматі
for key, value in book.items():
    print(key, value)

#9 Отримай значення "publisher" через get().
print(book.get("publisher"))

#10 Отримай "publisher" через get(), але якщо ключа немає — поверни "Unknown".
print(book.get("publisher", "Unknown")) '''

#11 Порахуй суму всіх оцінок.
scores = {
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76
}
total = 0
for value in scores.values():
    total = total + value
print(total)
    
#12 Обчисли середню оцінку.
total1 = 0
avg_score = 0
for value in scores.values():
    total1 = total1 + value
    avg_score = total1 /  len(scores.values())         #len([value for value in scores])             
print(avg_score)

#13 Знайди найменшу оцінку.
min_score = value
for value in scores.values():
    if value < min_score:
        min_score = value
print(min_score)

#14 Знайди ім'я студента з найбільшою оцінкою.
max_score = value
for key,value in scores.items():
    if value > max_score:
        max_score = value
print(max_score)
