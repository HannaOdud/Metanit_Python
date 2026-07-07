#1 Напиши функцію. Повертає кількість ключів. Без len().
def count_keys(dictionary):
    count = 0
    for key in dictionary.keys():
        count += 1
    return count
print(count_keys({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))

#2 Напиши функцію. Повертає кількість значень.Без len().
def count_values(dictionary):
    count = 0
    for value in dictionary.values():
        count += 1
    return count
print(count_values({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))

#3 Напиши функцію. Повертає перший ключ словника.
def first_key(dictionary):
    return next(iter(dictionary))
print(first_key({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))

#4 Напиши функцію. Повертає перше значення.
def first_value(dictionary):
    return next(iter(dictionary.values()))
print(first_value({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))

#5 Напиши функцію. Повертає останній ключ.
def last_key(dictionary):
    return list(dictionary.keys())[-1]
print(last_key({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 65
}))

#6 Напиши функцію. Повертає останнє значення.
def last_value(dictionary): 
    return list(dictionary.values())[-1]
print(last_value({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 65
}))

#7 Повертає новий список, у якому всі ключі записані великими літерами.
def all_keys_upper(dictionary):
    new_dict = dict()
    for key,value in dictionary.items():
        new_dict[key.upper()] = value
    return new_dict
print(all_keys_upper({
     "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 65
}))