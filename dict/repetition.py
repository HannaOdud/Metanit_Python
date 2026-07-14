#1 Напиши функцію:Повертає словник, де:
def letter_count(text):
    count_dict = {}
    for char in text:
        if char in count_dict:
            count_dict[char] = count_dict[char] + 1
        else:
            count_dict[char] = 1
    return count_dict

print(letter_count("hello"))

#2 Порахуй слова
def word_count(text):
    count_word_dict = {}
    for word in text.split():
        if word in count_word_dict:
            count_word_dict[word] += 1
        else:
            count_word_dict[word] = 1
    return count_word_dict
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
    res = dict1.copy()
    res.update(dict2) 
    return res
print(merge_dicts(dict1, dict2))

#4 Інвертуй словник
def invert_dict(items):
    res_dict = {}
    for key,value in items.items():
        res_dict[value] = key
    return res_dict
print(invert_dict({
    "a": 1,
    "b": 2,
    "c": 3
}))

#5 Видали всі значення None
def delet_none(items):
    res_dict = {}
    for key, value in items.items(): 
        res_dict[key] = value
        if res_dict[key] == None:
            del res_dict[key]
    return res_dict
print(delet_none({
    "name": "Anna",
    "age": None,
    "city": "Kyiv"
})) 

# OR

def delet_none(items):
    res_dict = {}
    for key, value in items.items(): 
        if value is not None:
            res_dict[key] = value
    return res_dict
print(delet_none({
    "name": "Anna",
    "age": None,
    "city": "Kyiv"
})) 

#6 Знайди найдовше слово
def longest_word(words):
    longest = ""
    for char in words:
        if len(char) > len(longest):
            longest = char
    return longest
print(longest_word(["sun", "elephant", "cat"]))

#7 Знайди найкоротше слово
def shortest_word(words):
    shortest = words[0]
    for char in words:
        if len(char) < len(shortest):
            shortest = char
    return shortest
print(shortest_word(["sun", "elephant", "cat"]))

#8 Видали дублікати
def dubl_del(numbers):
    res_list =[]
    for num in numbers:
        if num not in res_list:
            res_list.append(num)
    return res_list
print(dubl_del([1,2,3,2,4,1,5]))

#OR
def dubl_del(numbers):
    return list(set(numbers))
print(dubl_del([1,2,3,2,4,1,5]))

#9 Поверни всі парні числа
def print_even_num(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)
    return new_list
print(print_even_num([1,2,3,4,5,6]))

#10
#11
#12
#13
#14
#15
#16 Перевір анаграму
def is_anagram(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
print(is_anagram("listen","silent"))
print(is_anagram("listen","sillnt"))

#17 Знайди перший символ, що повторюється
def first_repeated_symbol(word):
    res_list = []
    for char in word:
        if char in res_list:
            return char
        else:
            res_list.append(char)
print(first_repeated_symbol("programming"))

#18 Знайди всі унікальні символи
def unique_char(word):
    char_dict = {}
    for char in word:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    unique_list = []
    for key,value in char_dict.items():
        if value== 1:
            unique_list.append(key) 
    return unique_list
print(unique_char("banana"))

#19 Порахуй голосні та приголосні
def count_vowels_consonants(word):
    con = 0
    vow = 0
    res = {"vow":0, "con":0}
    for char in word:
        if (char == 'a' or char == 'e' or char == 'i'  or char == 'o' or char == 'u'):
            res["vow"] = res["vow"] + 1

        else:
             con += 1
             res["con"] = res["con"] + 1
    return res
print(count_vowels_consonants("listen"))

#OR 
def count_vowels_consonants(word):
    con = 0
    vow = 0
    for char in word:
        if char in "aeiou":
            vow = vow + 1
        else:
            con = con + 1
    res_dict  = {
        "vowels": vow,
        "consonants": con
    }
    return res_dict
print(count_vowels_consonants("listen"))

#20 Є список словників: Напиши функцію яка поверне список імен усіх студентів із найвищою оцінкою:
students = [
    {"name": "Anna", "score": 95},
    {"name": "Ivan", "score": 81},
    {"name": "Olena", "score": 90},
    {"name": "Petro", "score": 95}
]
def best_students(students):
    res_list = []
    max_score = 0
    for dict in students:
        if dict["score"] > max_score:
            max_score = dict["score"] 
    for dict in students:
        if dict["score"] == max_score:
            res_list.append(dict["name"])
    return res_list
print(best_students(students))
