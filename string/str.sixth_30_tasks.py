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



 