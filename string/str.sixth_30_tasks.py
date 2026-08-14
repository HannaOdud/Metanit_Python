#mini-вправа для закріплення прапорця.


def contains_vowel(word):
    char = word.split()
    vows = ["a","e","i","o","u"]

    has_vowel = False
    for char in word:
        if char in vows:
            has_vowel = True
    return has_vowel
print(contains_vowel("ca2t"))

print(" 1.----------------------------------------------------------")
# Повернути список слів, довжина яких парна.
def list_even_word(text):
    words = text.split()
    res = []
    for word in words:
        if len(word) % 2 == 0:
            res.append(word)
    return res
print(list_even_word("Apple Amazing Ant Book Banana Ball"))

print("2.------------------------------------------------------------")
#Повернути список слів, довжина яких непарна.
def list_odd_word(text):
    words = text.split()
    res = []
    for word in words:
        if len(word) % 2 == 1:
            res.append(word)
    return res
print(list_odd_word("Apple Amazing Ant Book Banana Ball"))

print("3.-----------------------------------------------------------")
# слово → перша літера
def dict_word_first(text):
    words = text.split()
    res = {}
    for word in words:
        res[word] = word[0]
    return res
print(dict_word_first("Apple Amazing Ant Book Banana Ball"))

print("4.-----------------------------------------------------------")
# слово → остання літера
def dict_word_last(text):
    words = text.split()
    res = {}
    for word in words:
        res[word] = word[-1]
    return res
print(dict_word_last("Apple Amazing Ant Book Banana Ball"))

print("5.-----------------------------------------------------------")
# Повернути список слів, у яких перша і остання літера однакові.
def word_first_equal_last(text):
    words = text.split()
    res = []
    for word in words:
        if word[0] == word[-1]:
            res.append(word)
    return res
print(word_first_equal_last("level apple Anna radar test"))

print("6.-----------------------------------------------------------")
# Повернути список слів, довжина яких від 5 до 8 символів включно.
def len_char(text):
    words = text.split()
    res = []
    for word in words:
         if len(word) >= 5 and len(word) <= 8: 
            res.append(word)
    return res
print(len_char("cat elephant programming apple"))

print("7.---------------------------------------------------------")
# Повернути слово, у якому найбільше голосних. Без max().
def max_vow_word(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    max_vow_len = 0
    max_vow_word = ""

    for word in words:
        inner_total_vow = 0
        for char in word:
            if char in vows:
                inner_total_vow += 1
        if inner_total_vow > max_vow_len:
            max_vow_len = inner_total_vow
            max_vow_word = word
    return max_vow_word
print(max_vow_word("cat elephant programming apple"))

print("8.---------------------------------------------------------") 
# Повернути слово, у якому найменше голосних. Без min().
def min_vow_word(text):
    words = text.split()
    vows = ["a","e","i","o","u"]

    min_vow_len = float("inf")
    min_vow_word = ""

    for word in words:
        inner_vow_count = 0
        for char in word:
            if char in vows:
                inner_vow_count += 1

        if inner_vow_count < min_vow_len:
            min_vow_len = inner_vow_count
            min_vow_word = word
    return min_vow_word
print(min_vow_word("cat elephant programming apple"))

print("9.-------------------------------------------------------")
# Повернути список слів, які містять хоча б одну цифру.
def has_digit(text):
    words = text.split()
    res =[]
    
    for word in words:
        has_digit = False
        for char in word:
            if char.isdigit():
                has_digit = True
                break
        if has_digit:
            res.append(word)
    return res
print(has_digit("level2 apple top Anna 3 radaaar test"))

#OR
def has_digit2(text):
    words = text.split()
    res =[]
    
    for word in words:
      if any(char.isdigit() for char in word):
          res.append(word)
    return res
print(has_digit2("apple cat2 hello Python3 dog"))

print("10.-----------------------------------------------------")
# Повернути список слів, які не містять цифр.
def has_alpha(text):
    words = text.split()
    res = []
    for word in words:
        if not any(char.isdigit() for char in word):
            res.append(word)
    return res
print(has_alpha("apple cat2 hello Python3 dog"))

print("11.---------------------------------------------------")
# Порахувати, скільки слів починаються з голосної.
def count_first_char(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    words_fist_char_vow = 0
    for word in words:
        if word[0].lower() in vows:
                words_fist_char_vow += 1
    return words_fist_char_vow

print(count_first_char("apple apple apple cat2 hello Python3 apple dog"))

#OR
def count_first_char2(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
          
    return sum(word[0].lower() in vows for word in words)

print(count_first_char2(" Eva Apple cat2 hello Python3 apple dog"))

print("12.----------------------------------------------------")
# Порахувати, скільки слів закінчуються голосною.
def last_char_vows(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    return sum(word[-1].lower() in vows for word in words)
print(last_char_vows(" Eva Apple cat2 hello Python3 apple dog"))
#Or
def last_char_vows2(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    count = 0
    for word in words:
        if word[-1].lower() in vows:
            count += 1
    return count
print(last_char_vows2(" Eva Apple cat2 hello Python3  dog"))

print("13.-----------------------------------------------------")
# Повернути список слів, які починаються і закінчуються голосною.
def first_and_last(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    res = []
    for word in words:
        if word[0].lower() in vows and word[-1].lower() in vows:
            res.append(word)
    return res
print(first_and_last("Eva Apple cat2 hello Python3  dog"))

print("14.-----------------------------------------------------")
# Повернути словник: слово → кількість голосних
def dict_with_vows(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    res = {}
    for word in words:
        res[word] = sum(1 for char in word.lower() if char in vows )
    return res
print(dict_with_vows("cat apple elephant"))

print("15.---------------------------------------------------")
# Повернути словник: слово → кількість приголосних. Цифри та пробіли не рахувати як приголосні.
def dict_with_cons(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    res = {}
    for word in words:
        res[word] = sum(1 for char in word.lower() if char not in vows)
    return res
print(dict_with_cons("cat apple elephant"))

print("16.--------------------------------------------------")
# Замінити кожну голосну на "*".
def replace_vow1(text):
    vows = ["a","e","i","o","u"]
    new_char = []
    for char in text:
        if char in vows:
            new_char.append("*")
        else:
            new_char.append(char)
    return "".join(new_char)   
print(replace_vow1("cat apple elephant"))

#OR
def replace_vow2(text):
    vows = "aeiouAEIOU"
    for v in vows:
        text = text.replace(v, "*")
    return text
print(replace_vow2("cat apple elephant"))

print("17.-----------------------------------------------------")
# Порахувати кількість слів, у яких більше голосних, ніж приголосних.
def vows_or_cons(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    res =[]
    for word in words:
        count_vow = 0
        count_con = 0
        for char in word:
            if char in vows:
                count_vow += 1
            if char not in vows:
                count_con += 1
        if count_vow > count_con:
            res.append(word)
    return len(res)
print(vows_or_cons("cat apple elephant asasasa"))     

print("18.-------------------------------------------------------")
# Порахувати кількість слів, у яких однакова кількість голосних і приголосних.
def vows_equal_cons(text):
    words = text.split()
    vows = ["a","e","i","o","u"] 
    res = []
    for word in words:
        total_vows = 0
        total_cons = 0
        for char in word.lower():
            if char in vows:
                total_vows += 1
            if char not in vows:
                total_cons += 1
        if total_vows == total_cons:
            res.append(word)
    return len(res)
print(vows_equal_cons("cat apple elephant asasas Anna"))

# OR
def vows_equal_con2(text):
    words = text.split()
    vows = ["a","e","i","o","u"] 
    res = []
    for word in words:
        total_vows = sum(1 for char in word.lower() if char in vows )
        total_cons = sum(1 for char in word.lower() if char not in vows)
        if total_vows == total_cons:
            res.append(word)
    return len(res)
print(vows_equal_con2("cat apple elephant Anna"))

print("19.--------------------------------------------------------------")
# Повернути True або False залежно від того, чи всі літери в рядку маленькі.
# перевіряй символи через .isalpha() та .isupper().
def check_if_small(text):

    for char in text:
        if char.isalpha() and not char.isupper():
            return True
     
    return False
print(check_if_small("cat apple elephant Anna"))
 
# Or
def check_if_small2(text):
       return text.islower()
print(check_if_small2("cat apple elephant Anna"))

print("20.-------------------------------------------------------------")
# Повернути список слів, які написані з великої літери. 
def capital_letter(text):
    words = text.split()
    res =[]
    for word in words:
        if word[0].isupper():
            res.append(word)
    return res
print(capital_letter("I love Python And Kyiv"))

print("21.------------------------------------------------------------")
# Повернути найдовше слово, яке містить не менше двох голосних. Без max().
def max_vow_word(text):
    words = text.split()
    vows = ["a","e","i","o","u"] 
    max_len_word = 0
    max_word = ""
    for word in words:
        count_vows = 0
        for char in word:
            if char in vows:
                count_vows += 1
        if len(word) > max_len_word and count_vows > 2:
            max_len_word = len(word)
            max_word = word
    return max_word
print(max_vow_word("cat apple elephant Anna"))

#Or

def max_vow_word(text):
    words = text.split()
    vows = ["a","e","i","o","u"] 
    max_word = ""
    for word in words:
        count_vows = 0
        for char in word:
            if char in vows:
                count_vows += 1
        if len(word) > len(max_word) and count_vows > 2:
            max_word = word
    return max_word
print(max_vow_word("cat apple elephant Anna"))

print("22.--------------------------------------------------")
# Повернути найкоротше слово, яке містить цифру. Без min().
def min_vow_word(text):
    words = text.split()
    min_word = words[0]
    for word in words:
        if any(char.isdigit() for char in word):
            if len(word) < len(min_word):
                min_word = word
    return min_word
print(min_vow_word("c2at apple eleph2ant Anna"))

print("23.---------------------------------------------------")
# Порахувати кількість різних слів у реченні.
def count_diff_words(text):
    words = text.split()
    res = []
    for word in words:
        if word not in res:
            res.append(word)
    return len(res)
print(count_diff_words("cat dog cat bird dog"))

#oR
def count_diff_words2(text):
    words = text.split()
    return len(set(words))
print(count_diff_words2("cat dog cat bird dog"))

print("24.--------------------------------------------------")
# Повернути список слів без повторень, але зберегти їхній початковий порядок.
def list_no_repetition(text):
    words = text.split()
    res = []
    for word in words:
        if word not in res:
            res.append(word)
    return len(res)
print(list_no_repetition("cat dog cat bird dog"))

print("25.--------------------------------------------------")
# довжина слова → кількість таких слів
def dict_len_count(text):
    words = text.split()
    res = {}
    for word in words:
        if len(word) in res:
            res[len(word)] += 1
        else:
            res[len(word)] = 1
    return res
print(dict_len_count("cat dog cat bird dog"))

print("26.---------------------------------------------------")
# Повернути слово, яке має найбільшу кількість різних літер. Без max().
def max_diff_letter(text):
    words = text.split()
    max_word_len = 0
    max_word = ""
    for word in words:
        unique_letter = len(set(word))
        if unique_letter > max_word_len:
            max_word_len = unique_letter
            max_word = word
    return max_word
print(max_diff_letter("c2at apple eleph2ant Anna"))

print("27.------------------------------------------------------")
# Повернути список слів, у яких жодна літера не повторюється.
def no_repeat(text):
    words = text.split()
    res = []
    for word in words:
        if len(word) == len(set(word.lower())):
            res.append()
    return res
print(no_repeat("cat dog apple lamp"))

print("28.------------------------------ -----------------------")
# Повернути список слів, у яких є хоча б одна повторювана літера.
def one_repeat(text):
    words = text.split()
    res = []
    for word in words:
        if len(word) > len(set(word.lower())):
            res.append()
    return res
print(one_repeat("cat dog apple lamp"))

print("29.------------------------------------------------------")
# Повернути словник: перша літера → кількість слів
def first_letter_dict(text):
    words = text.split()
    res = {}
    for word in words:
        if word[0].lower() in res:
            res[word[0].lower()] += 1
        else:
            res[word[0].lower()] = 1
    return res
print(first_letter_dict("cat dog apple lamp"))

#Or

def first_letter_dict2(text):
    words = text.split()
    res = {}
    for word in words:
        res[word[0].lower()] = res.get(word[0].lower(), 0) +1
    return res
print(first_letter_dict2("cat dog apple lamp"))

print("30.---------------------------------------------------------")
# Міні-комбінована задача
# 
def analyze_words(text):
    pass


{
    "words": ...,
    "unique_words": ...,
    "longest_word": ...,
    "shortest_word": ...,
    "words_with_digits": ...,
    "palindromes": ...
}
print(analyze_words("level cat Apple2 radar dog"))
