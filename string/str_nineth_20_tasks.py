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
        if char not in char_repeated and char != " ":
            return char
    return None
print(first_unique_char("cat cat apple elephant"))

print("11.----------------------------------------------")
# Перший символ, який зустрічається двічі. Враховуй порядок появи символів.
def first_repeated_char(text):
    char_appeared = []
    for char in text:
        if char in char_appeared:
            return char
        char_appeared.append(char)
    return None
print(first_repeated_char("abcdab"))

#OR
def first_repeated_char2(text):
    seen = set()
    for char in text:
        if char in seen:
            return char
        seen.add(char)
    return None
print(first_repeated_char2("abcdab"))

print("12.-----------------------------------------------")
# Найчастіша літера без урахування регістру
# A і a повинні рахуватися як одна літера.
# Пробіли, цифри та розділові знаки не рахувати.
# Без max().
def most_common_letter(text):
    dict_count = {}
    for char in text:
        if char.lower() in dict_count and char.isalpha():
            dict_count[char.lower()] += 1
        elif char.isalpha():
            dict_count[char.lower()] = 1 
    #return dict_count
    max_count = 0
    max_char =""
    for key,value in dict_count.items():
        if value > max_count:
            max_count = value
            max_char = key
    return max_char
print(most_common_letter("cat cat apple ellllllephant"))

print("13.-------------------------------------------")
# Слова, які є паліндромами та мають максимальну довжину 
# повернути всі найдовші паліндроми.
def longest_palindromes(text):
    words = text.split()
    pallindromes = []
    for word in words:
        if word == word[::-1]:
            pallindromes.append(word)
    max_len = 0
    res = []
    for word in pallindromes:
        if len(word) > max_len:
            max_len = len(word)
    for word in pallindromes:
        if len(word) == max_len:
            res.append(word)
    return res
print(longest_palindromes("level sos ahahaha radar cccc cat civic"))

print("14.---------------------------------------------")
# Слова з однаковою кількістю голосних
# Тобто ключ — кількість голосних, значення — список слів.
def group_by_vowel_count(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    res = {}
    for word in words:
        count = sum(1 for char in word if char in vows)
        if count in res:
            res[count].append(word)
        else:
            res[count] = [word]
    return res
print(group_by_vowel_count("cat dog apple house"))

print("15.---------------------------------------------")
# Частота першої літери
def first_letter_frequency(text):
    words = text.split()
    res = {}
    for word in words:
        if word[0].lower() in res:
            res[word[0].lower()] += 1
        else:
            res[word[0].lower()] = 1
    return res             
print(first_letter_frequency("Apple Ant Banana Ball Cat"))

print("16.--------------------------------------------") 
# Слова тільки з унікальних літер
# Повертає слова, де жодна літера не повторюється.
# Apple не підходить, cat — підходить.
# Регістр ігнорувати.
def all_unique_letter_words(text):
    words = text.split()
    res = []
    for word in words:
        if len(word.lower()) == len(set(word.lower())):
            res.append(word)
    return res
print(all_unique_letter_words("dog apple bird dog"))

print("17.-------------------------------------------")
# Слова, які зустрічаються в обох текстах, без повторень
def common_unique_words(text1, text2):
    words1 = set(text1.split())
    words2 = set(text2.split())
    res = words1.intersection(words2)
    return res
text1 = "cat dog cat bird"
text2 = "dog apple bird dog"
print(common_unique_words(text1, text2))

#OR
def common_unique_words2(text1, text2):
    words1 = text1.split()
    words2 = text2.split()
    res = set()
    for word in words1:
        if word in words2:
            res.add(word)
    return res
text1 = "cat dog cat bird"
text2 = "dog apple bird dog"
print(common_unique_words2(text1, text2))

print("18.--------------------------------------------")
# Слова тільки в одному тексті, без повторень
def unique_words_between_texts(text1, text2):
    words1 = text1.split()
    words2 = text2.split()
    res = set()
    for word in words1:
        if word not in words2:
            res.add(word)
    for word in words2:
        if word not in words1:
            res.add(word)
    return res
text1 = "cat dog bird"
text2 = "dog apple bird"
print(unique_words_between_texts(text1, text2))

print("19.---------------------------------------------")
# Міні-аналіз речення
def text_summary(text):
    words = text.split()
    #unique words
    uniq_w = len(set(words))
    # longest_word
    longest = max(words, key=len)
    #shortest
    shortest = min(words, key=len)
    #most_common
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word,0)+1
    most_common_w = ""
    most_common = 0
    for key,value in words_dict.items():
        if value > most_common:
            most_common = value
            most_common_w = key
    #palindomes
    pal = []        
    for word in words:
        if word == word[::-1]:
            pal.append(word)
    res = {
        "words": len(words),
        "unique_words": uniq_w,
        "longest_word": longest,
        "shortest_word": shortest,
        "most_common_word": most_common_w,
        "palindromes": pal
    }
    return res
print(text_summary("level sos ahahaha radar cat cccc cat civic"))

print("20.--------------------------------------------")
# Велика Level 3 задача
def advanced_text_analysis(text):
    words = text.split()
    #most_common
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word,0)+1
    most_common_w = ""
    most_common = 0
    for key,value in words_dict.items():
        if value > most_common:
            most_common = value
            most_common_w = key
    #longest
    longest = max(words, key=len)
    #shortest
    shortest = min(words, key=len)
    #palindomes
    pal = []        
    for word in words:
        if word == word[::-1]:
            pal.append(word)
    #words with digits
    with_digit =[]
    for word in words:
        for char in word:
            if char.isdigit():
                with_digit.append(word)
                break
    #words with max_vows
    vows = ["a","e","i","o","u"]
    max_count = 0
    for word in words:
        count = sum(1 for char in word if char in vows)
        if count > max_count:
            max_count = count
    max_words = []
    for word in words:
        count = sum(1 for char in word if char in vows)
        if max_count == count:
            max_words.append(word)
    #first_letter_groups
    char_group = {}
    for word in words:
        if word[0] in char_group:
            char_group[word[0]].append(word)
        else:
            char_group[word[0]] = [word]
    #word_len
    word_len = {}
    for word in words:
        if len(word) in word_len:
            word_len[len(word)] += 1
        else:
             word_len[len(word)] = 1


    res = {
        "word_count": len(words),
        "unique_word_count": len(set(words)),
        "most_common_word": most_common_w,
        "longest_word": longest,
        "shortest_word": shortest,
        "palindromes": pal,
        "words_with_digits": with_digit,
        "words_with_max_vowels": max_words,
        "first_letter_groups": char_group,
        "word_lengths": word_len
    }
    return res
print(advanced_text_analysis("level sos ahahaha radar c2at cccc cat civic"))