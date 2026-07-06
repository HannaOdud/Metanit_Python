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
    #OR
    if "publisher" in book:
        print("Є")
    else:
        print("Немає")


#6  Виведи всі ключі через цикл.
for key in book.keys():
    print (key)

#7 Виведи всі значення через цикл.
for  value in book.values():
    print(value)

#8 Виведи всі пари у форматі
for key, value in book.items():
    print(f"{key} --> {value})
    #print(key, "-->", value)

#9 Отримай значення "publisher" через get().
print(book.get("publisher"))

#10 Отримай "publisher" через get(), але якщо ключа немає — поверни "Unknown".
print(book.get("publisher", "Unknown")) '''

'''#11 Порахуй суму всіх оцінок.
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
min_score = float("inf")           #min_score = next(iter(scores.values()))
for value in scores.values():
    if value < min_score:
        min_score = value
print(min_score)

#14 Знайди ім'я студента з найбільшою оцінкою.
max_score = float("-inf")
best_student = None
for key,value in scores.items():
    if value > max_score:
        max_score = value
        best_student = key
print(max_score)
print(best_student)'''

#15 Виведи всіх студентів, у кого оцінка 90 і більше.
scores = {
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76
}
for key, value in scores.items():
    if value >= 90:
        print(f"{key}: {value}")

#16 Порахуй, скільки студентів мають оцінку нижче 80.
count = 0
for key, value in scores.items():
    if value < 80:
        count = count + 1
print(count)  

#17 Заміні оцінку Івана на 100.
scores["Ivan"] = 100
print(scores)
 
#18 Додай нового студента.
scores["Yana"] = 98
print(scores)

#19 Видали Олега.
del scores["Oleh"]
print(scores)

#20 Перевір, чи є студент "Petro".
print("Petro" in scores)