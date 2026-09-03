print("1.--------------------------------------------------")
# Слова з максимальною частотою
# Поверни всі слова, які зустрічаються найбільше разів.
def words_with_max_frequency(text):
    words = text.split()
    max_count = 0
    dict_words = {}
    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1
    for key,value in dict_words.items():
        if value > max_count:
            max_count = value
    res = []
    for key,value in dict_words.items():
        if value == max_count:
            res.append(key)
    return res
print(words_with_max_frequency("cat dog cat bird dog"))

print("2.------------------------------------------------")
# Найкоротше слово серед тих, що повторюються
# Слово повинно зустрічатися хоча б двічі. Серед таких слів знайди найкоротше.
# Без min().
def shortest_repeated_word(text): 
    words = text.split()
    dict_words = {} 
    for word in words:
        dict_words[word] = dict_words.get(word, 0)+1
    shortest = ""
    len_shortest = float("inf")
    for key,value in dict_words.items():
        if len(key) < len_shortest and  value >= 2:
            len_shortest = len(key)
            shortest = key
    return shortest
print(shortest_repeated_word("Apple Ant Ant Amazing Amazing Ball Book Banana Cat"))

print("3.-------------------------------------------------")
# Найдовше слово серед унікальних
# Слово повинно зустрічатися рівно один раз. Без max().
def longest_unique_word(text):
    words = text.split()
    dict_words = {} 
    for word in words:
        dict_words[word] = dict_words.get(word, 0)+1
    res = []
    for key, value in dict_words.items():
        if value == 1:
            res.append(key) 
    max_word = ""
    max_word_len = 0
    for word in res:
        if len(word) > max_word_len:
            max_word_len = len(word)
            max_word = word
    return max_word
print(longest_unique_word("Apple Ant Ant Amazing Amazing Ball Book Banana Cat"))

print("4.--------------------------------------------------")
#Групування за кількістю голосних
def group_by_vowels(text):
    words = text.split()
    group_dict = {}
    vows = ["a","e","i","o","u"]
    for word in words:
        count_vows = sum(1 for char in word if char in vows)
        if count_vows in group_dict:
            group_dict[count_vows].append(word)
        else:
            group_dict[count_vows] = [word]
    return group_dict
print(group_by_vowels("cat dog apple house elephant"))

#Or
def group_by_vowels(text):
    words = text.split()
    group_dict = {}
    vows = ["a","e","i","o","u"]
    
    for word in words:
        n_word = word.strip(",.!?:;")
        count_vows = sum(1 for char in n_word.lower() if char in vows)
        if count_vows in group_dict:
            group_dict[count_vows].append(n_word)
        else:
            group_dict[count_vows] = [n_word]
    return group_dict
print(group_by_vowels("cat dog apple house elephant"))

print("5.-----------------------------------------------------")
# Найдовше слово в кожній групі за першою літерою. Без max().
def longest_word_by_first_letter(text):
    words = text.split()
    gr_dict = {}
    for word in words:
        if word[0] in gr_dict:
            gr_dict[word[0]].append(word)
        else:
            gr_dict[word[0]] = [word]
    #return gr_dict
    res = {}
    for key, value in gr_dict.items():
        largest = ""
        for word in value:
            if len(word) > len(largest):
                largest = word

        res[key] = largest
    return res
print(longest_word_by_first_letter("Apple Ant Amazing Ball Book Banana Cat"))

print("6.----------------------------------------------------")
# Всі слова з максимальною довжиною
def words_with_max_length(text):
    words = text.split()
    w_dict = {}
    for word in words:
        if len(word) in w_dict:
            w_dict[len(word)].append(word) 
        else:
            w_dict[len(word)] = [word] 
    print(w_dict)
    max_len = 0
    for key,value in w_dict.items():
        if key > max_len:
            max_len = key
    return w_dict[max_len]

print(words_with_max_length("cat house world elephant owl"))
#OR
def words_with_max_length2(text):
    words = text.split()
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    res = []
    for word in words:
        if len(word) == max_len:
            res.append(word)
    return res
print(words_with_max_length2("cat house world crocodile owl"))

print("7.-------------------------------------------------")
# Поверни літеру, з якої починається найбільше слів. Регістр ігнорувати. Без max().
def most_common_first_letter(text):
    words = text.split()
    w_dict = {}
    for word in words:
        if word[0] in w_dict:
            w_dict[word[0].lower()] += 1
        else:
            w_dict[word[0].lower()] = 1
    max_count = 0
    max_char = ""
    for key, value in w_dict.items():
        if value > max_count:
            max_count = value
            max_char = key
    return max_char
print(most_common_first_letter("cat house world crocodile owl"))

print("8.-------------------------------------------------")
# Поверни літеру, Найчастіша остання літера. Регістр ігнорувати. Без max().
def most_common_last_letter(text):
    words = text.split()
    w_dict = {}
    for word in words:
        if word[-1].lower() in w_dict:
            w_dict[word[-1]] += 1
        else:
            w_dict[word[-1]] = 1
    max_count = 0
    max_char = ""
    for key, value in w_dict.items():
        if value > max_count:
            max_count = value
            max_char = key
    return max_char
print(most_common_last_letter("cat house world crocodile owl"))


print("9.-----------------------------------------------")
# Слова з найбільшою кількістю різних літер
# Поверни всі слова, які мають максимальну кількість різних літер. Регістр ігнорувати.
def words_with_most_unique_letters(text):
    words = text.split()
    max_count = 0
    res = []
    for word in words:
        if len(set(word.lower())) > max_count:
            max_count = len(set(word.lower()))
    for word in words:
        if max_count == len(set(word.lower())):
            res.append(word.lower())
    return res
print(words_with_most_unique_letters("cat house world crocodile owl"))

print("10.------------------------------------------------")
# Знайди найкоротше слово-паліндром. Без min().
def shortest_palindrome(text):
    words = text.split()
    res = []
    for word in words:
        if word == word[::-1]:
            res.append(word)
    min_pall_len = float("inf")
    min_pall = ""
    for word in res:
        if len(word) < min_pall_len:
            min_pall_len = len(word)
            min_pall = word
    return min_pall 
print(shortest_palindrome("cat sos radar level house world crocodile owl"))


print("11.-----------------------------------------------")
# Поверни слово, яке містить найбільше цифр. Без max().
def words_with_most_digits(text):
    words = text.split()
    max_count = 0
    max_word = ""
    for word in words:
        count = sum(1 for char in word if char.isdigit())
        if count > max_count:
            max_count = count
            max_word = word
    return max_word
print(words_with_most_digits("cat2 ab123 dog7"))

print("12.-----------------------------------------------")
# Слова з цифрами — всі максимальні
# Поверни всі слова, які містять максимальну кількість цифр.
def all_words_with_most_digits(text):
    words = text.split()
    max_count = 0
    res = []
    for word in words:
        count = sum(1 for char in word if char.isdigit())
        if count > max_count:
            max_count = count
    for word in words:
        count = sum(1 for char in word if char.isdigit())
        if max_count == count:
            res.append(word)
    return res
print(all_words_with_most_digits("cat2 ab123 dog7 owl456 duck789"))

print("13.------------------------------------------------")
# Слова, у яких кількість голосних більша за середню
# Спочатку знайди середню кількість голосних на слово, потім поверни слова,
#  які мають більше голосних за це середнє значення.
def words_above_average_vowels(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    sum_vows = 0
    res = []
    for word in words:
        count_vows = sum(1 for char in word if char in vows)
        sum_vows += count_vows
    avg = sum_vows/len(words)
    for word in words:
        count_vows = sum(1 for char in word if char in vows)
        if count_vows > avg:
            res.append(word)
    return res
print(words_above_average_vowels("cat sos radar level house world crocodile owl"))

print("14.-------------------------------------------------")
# Слова з максимальною кількістю приголосних
def max_consonant_words(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    max_cons = 0
    res = []
    for word in words:
        count_cons = sum(1 for char in word.lower() if char not in vows and char.isalpha())
        if count_cons> max_cons:
            max_cons = count_cons 
    for word in words:
        count_cons = sum(1 for char in word.lower() if char not in vows and char.isalpha())
        if count_cons == max_cons:
            res.append(word)
    return res
print(max_consonant_words("cat sos radar level house world crocodile owl"))
#OR
def max_consonant_words2(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    max_cons = 0
    res = []
    for word in words:
        count_cons = sum(1 for char in word.lower() if char not in vows and char.isalpha())
        if count_cons > max_cons:
            max_cons = count_cons 
            res = [word]
        elif count_cons == max_cons:
            res.append(word)
    return res
print(max_consonant_words2("cat sos radar level house world crocodile crocodile owl"))

print("15.-----------------------------------------------------")
# Перше слово, яке повторюється
# Тобто повернути слово в той момент, коли воно вперше зустрілося вдруге.
def first_repeated_word(text):
    words = text.split()
    checked = []
    repeated = []
    for word in words:
        if word.lower() in checked:
           repeated.append(word.lower())
        checked.append(word.lower())
    return repeated[0]
print(first_repeated_word("cat dog bird cat apple dog"))

#OR
def first_repeated_word1(text):
    words = text.split()
    checked = []

    for word in words:
        clean_word = word.lower().strip(",.!&:;")
        if clean_word in checked:
           return word
        checked.append(clean_word)
    return None
print(first_repeated_word1("cat dog bird cat apple dog"))

#OR
def first_repeated_word2(text):
    words = text.split()
    seen = set()
    for word in words:
        clean_word = word.lower().strip(",.!?:;")
        if clean_word in seen:
            return word
        else:
            seen.add(clean_word) 
print(first_repeated_word2("cat dog bird cat apple dog"))

print("16.------------------------------------------------")
# Перше слово, яке зустрічається лише один раз
def first_unique_word(text):
    words = text.split()
    checked = []
    repeated = []
    for word in words:
        if word in checked:
            repeated.append(word)
        checked.append(word)
    for word in words:
        if word not in repeated:
            return word
print(first_unique_word("cat dog cat bird dog apple"))

print("17.----------------------------------------------")
# Слова, які мають однакову довжину з першим словом
def same_length_as_first(text):
    words = text.split()
    res = []
    first_w = words[0]
    for word in words:
        if len(word) == len(first_w):
            res.append(word)
    return res       
print(same_length_as_first("cat dog house apple fox"))

print("18.---------------------------------------------")
# Слова, які починаються тією самою літерою, що й останнє слово
# останнє слово — "cat", його перша літера "c".
# Повернути всі слова, що починаються з "c".
def same_first_as_last_word(text):
    words = text.split()
    res = []
    last_word = words[-1]
    for word in words:
        if last_word[0] == word[0]:
            res.append(word)
    return res
print(same_first_as_last_word("apple cobra carrot dog ant cat"))

print("19.--------------------------------------------")
# Слова, які містять усі голосні
# Повернути слова, у яких присутні: a, e, i, o, u
def words_with_all_vowels(text):
    words = text.split()
    res = []
    vows = ["a","e","i","o","u"]
    for word in words:
        are_all_vows = True
        for char in vows:
            if char not in word:
                are_all_vows = False
        if are_all_vows == True:
            res.append(word) 
    return res  
print(words_with_all_vowels("apuiople cobra carrot dog ant cat"))

print("20.-------------------------------------------")
# Комбінована Level 3
def analyze_words(text):
    words = text.split()
    #most_common_word
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0)+1
    max_val = 0
    max_val_word = ""
    for key,value in word_dict.items():
        if value > max_val:
            max_val = value
            max_val_word = key
    #longest_unique_word
    res = []
    for key,value in word_dict.items():
        if value == 1:
            res.append(word)
    lon_un_w = max(res, key=len)
    #palindromes
    pal = []
    for word in words:
        if word == word[::-1]:
            pal.append(word)
    #words_with_digits
    has_digit = []
    for word in words:
        for char in word:
            if char.isdigit():
                has_digit.append(word)
                break
    # words_with_most_vowels
    max_vows = 0
    vows = ["a","e","i","o","u"]
    res = []
    for word in words:
        count = sum(1 for char in word if char in vows)
        if count > max_vows:
            max_vows = count
    for word in words:
        count = sum(1 for char in word if char in vows)
        if count == max_vows:
            res.append(key)
    # first_letter_groups
    fl_group = {}
    for word in words:
        if word[0] in fl_group:
            fl_group[word[0]].append(word)
        else:
            fl_group[word[0]] = [word]

    res = {
        "word_count": len(words),
        "unique_word_count": len(set(words)),
        "most_common_word": max_val_word,
        "longest_word": max(words, key=len),
        "shortest_word": min(words, key=len),
        "longest_unique_word": lon_un_w,
        "palindromes": pal,
        "words_with_digits": has_digit,
        "words_with_most_vowels": res,
        "first_letter_groups": fl_group
    }
    return res
print(analyze_words("apuiople cobra cobra sos level radar carrot dog dog do1g an22t cat"))