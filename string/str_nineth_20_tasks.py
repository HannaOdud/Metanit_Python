#Level 3

print("1.--------------------------------------------")
# Найчастіше слово без max() Повертає слово, яке зустрічається найбільше разів.
def most_common_word(text):
    words = text.split()
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0)+1
    #return words_count
    max_common_word = ""
    max_common_count = 0
    for key,value in words_count.items():
        if value > max_common_count:
            max_common_count = value
            max_common_word = key
    return max_common_word
print(most_common_word("cat dog cat bird dog cat"))

print("2.--------------------------------------------")
# Усі слова з максимальною частотою
# Підказка: спочатку знайди максимальну частоту, потім зроби другий прохід.
def words_with_max_frequency(text):
    words = text.split()
    words_count = {}
    res = []
    for word in words:
        words_count[word] = words_count.get(word, 0)+1
    #return words_count
    max_common_count = 0
    for key,value in words_count.items():
        if value > max_common_count:
            max_common_count = value
    for key,value in words_count.items():
        if value == max_common_count:
            res.append(key)
    return res
print(words_with_max_frequency("cat dog cat bird dog"))

print("3.--------------------------------------------")
# Найдовше слово серед тих, що повторюються
# Тобто слово повинно зустрічатися мінімум двічі, а серед таких потрібно знайти найдовше.
def longest_repeated_word(text):
    words = text.split()
    words_count = {}
    res = []
    for word in words:
        words_count[word] = words_count.get(word, 0)+1
    #return words_count
    for key,value in words_count.items():
            if value >= 2:
                res.append(key)
    longest = max(res, key=len)
    return longest
print(longest_repeated_word("cat dog bird cat rabbit bird dog"))

#OR
def longest_repeated_word2(text):
    words = text.split()
    words_count = {}
    res = []
    for word in words:
        words_count[word] = words_count.get(word, 0)+1
    #return words_count
    for key,value in words_count.items():
            if value >= 2:
                res.append(key)
    longest = ""
    len_longest = 0
    for word in res:
        if len(word) > len_longest:
            len_longest = len(word)
            longest = word
    return longest
print(longest_repeated_word2("cat dog bird cat rabbit bird dog"))

#OR
def longest_repeated_word3(text):
    words = text.split()
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0)+1
    #return words_count
    longest = ""
    for key,value in words_count.items():
            if value >= 2 and len(key) > len(longest):
                longest = key   
    return longest
print(longest_repeated_word3("cat dog bird cat rabbit bird dog"))


print("4.---------------------------------------------")
# Коротше за середнє. Повертає список слів, довжина яких менша за середню довжину всіх слів.
def shorter_than_average(text): 
    words = text.split()
    sum_len = 0
    for word in words:
        sum_len += len(word)
    avg = sum_len /len(words)
    res = []
    for word in words:
        if len(word) < avg:
            res.append(word)
    return res
print(shorter_than_average("cat dog bird cat rabbit bird dog"))  

print("5.---------------------------------------------")  
# Групування слів за останньою літерою
def group_by_last_letter(text):
    words = text.split()
    word_dict = {}
    for word in words:
        if word[-1] in word_dict:
            word_dict[word[-1]].append(word)
        else:
            word_dict[word[-1]] = [word]
    return word_dict
print(group_by_last_letter("cat cat dog apple banana"))

print("6.----------------------------------------------")
# Найдовше слово в кожній групі
# Згрупуй слова за довжиною, а потім для кожної довжини залиш найдовше слово.
# Тут ти маєш подумати, що станеться, якщо в групі вже є слово тієї самої довжини.
def longest_by_length_group(text): 
    words = text.split()
    len_dict = {}
    res_dict = {}
    for word in words:
        if len(word) in len_dict:
            len_dict[len(word)].append(word)
        else:
            len_dict[len(word)] = [word]
    for key,value in len_dict.items():
        res_dict[key] = max(value, key=len)
    return res_dict
print(longest_by_length_group("cat dog apple banana"))

print("7.-------------------------------------------------") 
# Кількість голосних у кожному слові
def vowel_statistics(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    dict_count_vows = {}
    for word in words:
       dict_count_vows[word] = sum(1 for char in word.lower() if char in vows)
    return dict_count_vows

print(vowel_statistics("cat cat apple elephant"))

print("8.-----------------------------------------------")
# Усі слова з максимальною кількістю приголосних
def words_with_max_consonants(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    max_cons = 0
    res = []
    for word in words:
        count = 0
        for char in word:
            if char.lower().isalpha() and char not in vows:
                count += 1
        if count > max_cons:
            max_cons = count
    for word in words:
        count = 0
        for char in word:
            if char.lower().isalpha() and char not in vows:
                count += 1
        if count == max_cons:
            res.append(word)
    return res
print(words_with_max_consonants("cat dog bird cat rabbit bird dog"))

print("9.-----------------------------------------------------")
# Найкоротше слово з максимальною кількістю голосних
# Спочатку знайди максимальну кількість голосних, а потім серед цих слів вибери найкоротше.
def shortest_with_max_vowels(text): 
    words = text.split()
    vows = ["a","e","i","o","u"]
    res = []
    max_count = 0
    for word in words:
        count = sum(1 for char in word if char.lower() in vows)
        if count > max_count:
            max_count = count
    for word in words:
        count = sum(1 for char in word if char.lower() in vows)
        if count == max_count:
            res.append(word)
    shortest = min(res, key=len)
    return shortest
print(shortest_with_max_vowels("cat cat apple elephant"))

print("10.--------------------------------------------------")
# Перший неповторюваний символ
#Потрібно ігнорувати пробіли.
# Якщо унікального символу немає — повернути None.
def first_unique_char(text):
    char_appeared = []
    char_repeated = []
    for char in text:
        if char in char_appeared:
            char_repeated.append(char)
        char_appeared.append(char)
    for char in text:
        if char not in char_repeated:
            return char
print(first_unique_char("cat cat apple elephant"))

        
