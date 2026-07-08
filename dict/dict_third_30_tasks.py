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

#8 Усі рядкові значення перевести у верхній регістр.
def all_string_values_upper(dictionary):
    for key, value in dictionary.items():
        if type(value) == str:
            dictionary[key] = value.upper()
    return dictionary
print(all_string_values_upper({
    "name" : "Anna",
    "age" : 20,
    "city" : "Kyiv"
}))

#9 Повертає словник без числових значень.
def remove_numeric_values(dictionary):
    new_dict = {}
    for key,value in dictionary.items():
        if not isinstance(value, (int, float)):
            new_dict[key] = value
    return new_dict
print(remove_numeric_values({
    "name" : "Anna",
    "age" : 20,
    "city" : "Kyiv"
}))

#10 Повертає словник лише з числовими значеннями.
def only_numeric_values(dictionary):
    new_dict = dict()
    for key, value in dictionary.items():
        if isinstance(value,(int, float)):
            new_dict[key] = value
    return new_dict
print(only_numeric_values({
    "name" : "Anna",
    "age" : 20,
    "city" : "Kyiv"
}))
    
#11 Знайди всіх студентів із максимальною оцінкою. (Не одного.)
def students_with_max_marks(dictionary):
    max_value = max(dictionary.values())
    res_list = []
    for key, value in dictionary.items():
        if value == max_value:
            res_list.append(key)
    return res_list
print(students_with_max_marks({

    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))