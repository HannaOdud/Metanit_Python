# 1.Напиши функцію: Повертає словник, де:
def letter_count(text):
    dict_count = {}
    for char in text:
        if char in dict_count:
            dict_count[char] += 1
        else:
            dict_count[char] = 1
    return dict_count
print(letter_count("hello")) 

#2. 
def word_count(text):
    count_dict = {}
    list_text = text.split()
    for word in list_text:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict
print(word_count("cat dog cat bird dog dog"))

#3 Об'єднай два словники
dict1 = {
    "a": 1,
    "b": 2
}

dict2 = {
    "c": 3,
    "d": 4
}
def merge_dicts(dict1, dict2):
    dict_res = dict1.copy()
    dict_res.update(dict2)
    return dict_res
print(merge_dicts(dict1, dict2))

#4 Інвертуй словник
def invert(dictionary):
    res_dict = {}
    for key, value in dictionary.items():
            res_dict[value] = key
    return res_dict
print(invert({"a": 1,
    "b": 2,
    "c": 3}))

#5 Видали всі значення None
def del_none(dictionary):
    dict_list = list(dictionary.keys())
    for key in dict_list:
        if dictionary[key] is None:
            del dictionary[key]
    return dictionary
print(del_none({
    "name": "Anna",
    "age": None,
    "city": "Kyiv"
}))

#6 Знайди найдовше слово. Без max().
def longest_word(words):
    longest = ""
    for i in words:
        if len(i) > len(longest):
            longest = i
    return longest
print(longest_word(["sun", "elephant", "cat"]))

#7 Знайди найкоротше слово. Без min().
def smallest_word(words):
    smallest = words[0]
    for i in words:
        if len(i) < len(smallest):
            smallest = i
    return smallest
print(smallest_word(["sun", "elephant", "cat"]))

#8 Видали дублікати
def del_duplicat(list):
    no_duplic = []
    for i in list:
        if i not in no_duplic:
            no_duplic.append(i)
    return no_duplic
print(del_duplicat([1,2,3,2,4,1,5]))

#9 Поверни всі парні числа
def even_num(list):
    even_list = []
    for i in list:
        if i%2 == 0:
            even_list.append(i)
    return even_list
print(even_num([1,2,3,4,5,6]))    

#10 Поверни всі слова довші за 5 символів.
products = {
    "apple": 30,
    "banana": 25,
    "orange": 40,
    "kiwi": 80,
    "pear": 40
}
def longer_then_5_symbol(products):
    res_dict = {}
    for key,value in products.items():
        if len(key) > 5:
            res_dict[key] = value
    return res_dict
print(longer_then_5_symbol(products))

#OR

def longer_then_5_symbol(products):
    res_list = []
    for key in products:
        if len(key) > 5:
            res_list.append(key)
    return res_list
print(longer_then_5_symbol(products))

#11 Поверни список усіх товарів, які коштують 40 грн.
def list_of_products(products):
    res_list = []
    for key,value in products.items():
        if value == 40:
            res_list.append(key)
    return res_list
print(list_of_products(products))

#12 Порахуй, скільки товарів коштують дорожче 50 грн
def count_products(products):
    count = 0
    for value in products.values():
        if value > 50:
            count += 1
    return count
print(count_products(products))

#13 Поверни словник, де залишилися лише товари дорожчі за 30 грн.
def dict_of_product_more_30(products):
    prod_dict = {}
    for key,value in products.items():
        if value > 30:
            prod_dict[key] = value
    return prod_dict
print(dict_of_product_more_30(products))

#14 Створи словник, у якому ціна кожного товару зменшена на 20%.
def price_down_20(products):
    price_down_dict = {}
    for key, value in products.items():
        price_down_dict[key] = value * 0.8
    return price_down_dict
print(price_down_20(products))

#15 Поверни назву найдешевшого товару без min().
def cheapest_product(products):
    cheapest = float("inf")
    cheapest_name = ""
    for key, value in products.items():
        if value < cheapest:
            cheapest = value
            cheapest_name = key 
    return cheapest_name
print(cheapest_product(products))