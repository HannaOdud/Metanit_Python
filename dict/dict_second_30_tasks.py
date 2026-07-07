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

'''#15 Виведи всіх студентів, у кого оцінка 90 і більше.
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
print("Petro" in scores)'''

#21 
def print_dictionary(dictionary):
    return dictionary
print(print_dictionary({
    "name" : "Anna",
    "age" : 20,
    "city" : "Kyiv"}))

#22
def count_string_values(dictionary):
    count = 0
    for value in dictionary.values():
        if type(value) == int or type(value) == float:
            count = count + 1
    return count
print(count_string_values({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76
}))

#23 Напиши функцію. Повертає кількість рядків.
def count_string_values(dictionary):
    count = 0
    for value in dictionary.values():
        if type(value) == str:
            count += 1
    return count
print(count_string_values({
    "name" : "Anna",
    "age" : 20,
    "city" : "Kyiv"
}))

#24 Напиши функцію. Повертає суму всіх числових значень.
def total_numeric_values(dictionary):
    total = 0
    for value in dictionary.values():
        if type(value) == int or type(value) == float:
            total = total + value #total += value
    return total
print(total_numeric_values({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76
}))        

#25 Напиши функцію. Повертає найдовший ключ. Без max().
def longest_key(dictionary):
    max_key = ""
    for key in dictionary.keys():
        if len(key) > len(max_key):
            max_key = key
    return max_key
print(longest_key({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76
}))

#26 Напиши функцію. Повертає найдовше рядкове значення.
def longest_value(dictionary):
    max_value = ""
    for value in dictionary.values():
        if type(value) == str:
            if len(value) > len(max_value):
                max_value = value
    return max_value
print(longest_value({
    "name" : "Anna",
    "age" : 20,
    "city" : "Kyiv"
}))

#27 Напиши функцію. Повертає True або False.
def key_exists(dictionary, key):
    if key in dictionary:
        return True
    else: 
        return False
print(key_exists({
    "name" : "Anna",
    "age" : 20,
    "city" : "Kyiv"
}, "name" ))

#28 Напиши функцію. Повертає True, якщо таке значення існує.
def value_exists(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False
print(value_exists({
    "name" : "Anna",
    "age" : 20,
    "city" : "Kyiv"
}, "Kyiv" ))    

#29 Напиши функцію. Повертає кількість парних чисел серед значень.
def count_even_values(dictionary):
    count = 0
    for value in dictionary.values():
        if type(value) == int:
            if value % 2 == 0:
                count = count + 1
    return count        
print(count_even_values({
    "name" : "Anna",
    "age" : 20,
    "city" : "Kyiv"
}))

#30 Напиши функцію. яка міняє місцями ключі та значення.
def invert_dictionary(dictionary):
    new_dict = dict()
    for key, value in dictionary.items():
        new_dict[value] = key
    return new_dict
print(invert_dictionary({
    "name" : "Anna",
    "age" : 20,
    "city" : "Kyiv"
}))


