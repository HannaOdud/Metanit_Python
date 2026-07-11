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

#OR 
def all_keys_upper(dictionary):
    result = []
    for key in dictionary:
        result.append(key.upper())
    return result



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

#12 Знайди всіх студентів із мінімальною оцінкою.
def students_with_min_marks(dictionary):
    min_marks_students = min(dictionary.values())
    res_list = []
    for key, value in dictionary.items():
        if value == min_marks_students:
            res_list.append(key)
    return res_list
print(students_with_min_marks({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))

#13 Порахуй, скільки студентів мають оцінку вище середньої.
def count_student_with_higher_avg_marks(dictionary):
    count = 0
    avg_marks = sum(dictionary.values())/len(dictionary.keys())
    for key, value in dictionary.items():
        if value > avg_marks:
            count = count + 1
    return count
print(count_student_with_higher_avg_marks({
      "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))

#14 Порахуй, скільки студентів мають оцінку нижче середньої.
def count_student_with_lower_avg_marks(dictionary):
    count = 0
    avg_marks = sum(dictionary.values())/len(dictionary.keys())
    for key, value in dictionary.items():
        if value < avg_marks:
            count = count + 1
    return count
print(count_student_with_lower_avg_marks({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))

#15 Виведи студентів у алфавітному порядку.
def print_student_in_ordered_form(dictionary):
    new_list = []
    for key in dictionary.keys():
        new_list.append(key)
    return sorted(new_list)
print(print_student_in_ordered_form({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))

#16 Виведи оцінки у порядку зростання.
def print_students_marks_in_asc_order(dictionary):
    new_list = []
    for value in dictionary.values():
        new_list.append(value)
    return sorted(new_list, reverse=False)
print(print_students_marks_in_asc_order({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))

#17 Знайди другу найбільшу оцінку.
def second_largest_mark(dictionary):
    largest = float("-inf")
    second_largest = float("-inf")
    for value in dictionary.values():
        if value > largest:
            second_largest = largest
            largest = value
        elif value > second_largest and value < largest:
            second_largest = value
    return second_largest
print(second_largest_mark({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))

#18 Знайди другу найменшу оцінку.
def second_lowest_mark(dictionary):
    lowest = float("inf") 
    second_lowest = float("inf")
    for value in dictionary.values():
        if value < lowest:
            second_lowest = lowest
            lowest = value
        elif value < second_lowest and value > lowest:
            second_lowest = value
    return second_lowest
print(second_lowest_mark({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))

#19 Порахуй кількість різних оцінок.
def count_different_marks(dictionary):
    new_list = []
    for value in dictionary.values():
        if value not in new_list:
            new_list.append(value)
    return len(new_list)
print(count_different_marks({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))

#20 Створи новий словник, у якому залишаться лише студенти, які мають оцінку 90 і більше.
def students_with_90_scores(dictionary):
    new_dict = {}
    for key,value in dictionary.items():
        if value >= 90:
            new_dict[key] = value
    return new_dict        
print(students_with_90_scores({
    "Anna": 95,
    "Ivan": 81,
    "Olena": 90,
    "Oleh": 76,
    "Petro": 95
}))

#21 Є словник. Порахуй загальну вартість усіх товарів.
products = {
    "apple": 30,
    "banana": 25,
    "orange": 40,
    "kiwi": 80
}
def total_price_of_product(dictionary):
    return sum(dictionary.values())
print(total_price_of_product(products))

#22 Знайди найдешевший товар.Повернути назву.
def print_name_of_cheapest_product(dictionary):
    min_value = float("inf") 
    min_key = ""
    for key, value in dictionary.items(): 
        if value < min_value:
            min_value = value
            min_key = key 
    return min_key
print(print_name_of_cheapest_product(products))

#23 
def print_name_of_the_most_expensive_product(dictionary):
    max_value = float("-inf")
    max_key = ""
    for key, value in dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
print(print_name_of_the_most_expensive_product(products))

#24 Порахуй середню ціну.
def count_avg_price(dictionary):
    return sum(dictionary.values())/len(dictionary.values())
print(count_avg_price(products))

#25 Створи словник, де ціна збільшена на 10%.
def print_rised_new_dict(dictionary):
    new_dict = dict()
    for key, value in dictionary.items():
        new_dict[key] = value * 1.1
    return new_dict
print(print_rised_new_dict(products)) 

#26 Створи словник, де всі ціни менше 40 грн.
def print_new_dict_with_price_less_40(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        if value < 40:
            new_dict[key] = value
    return new_dict
print(print_new_dict_with_price_less_40(products))

#27 Порахуй кількість товарів дорожчих за середню ціну.
def count_products_expensive_ave_price(dictionnary):
    count = 0
    avg = sum(dictionnary.values())/len(dictionnary)
    for value in dictionnary.values():
        if value > avg:
            count += 1
    return count
print(count_products_expensive_ave_price(products))

#28 Напиши функцію. Повертає True або False.
def product_exists(products, name):
    if name in products:
        return True
    else:
        return False
print(product_exists( products,"orange"))

#OR 
def product_exists(products, name):
    return name in products
print(product_exists( products,"orange"))

#29
def price_exists(products, price):
    return price in products.values()
print(price_exists(products, 40))

#30 Напиши функцію, яка повертає назву товару і його ціну.
def most_expensive_product(products):
    max_val =  max(products.values()) 
    new_dict = dict()
    for key, value in products.items():
        if value >= max_val:
            new_dict[key] = value
    return new_dict
    
print(most_expensive_product(products))
def most_expensive_product(products):
    max_val =  max(products.values()) 
    max_key = ""
    res = []
    for key, value in products.items():
        if value == max_val:
            res.append(key)
            res.append(value)
    return tuple(res)
print(most_expensive_product(products))