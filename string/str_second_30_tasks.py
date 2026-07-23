'''#1 Повертає кількість літер у рядку (ігноруючи цифри, пробіли та розділові знаки).
def count_letters(text):
    count = 0
    for char in text:
        if char.isalpha():
            count +=1
    return count
print(count_letters(" I_12345I_!#O"))

#2 Повертає кількість цифр.
def count_digits(text):
    count = 0
    for char in text:
        if char.isdigit():
            count +=1
    return count
print(count_digits(" I_12345I_!#O"))

#3 Повертає кількість пробілів без count().
def count_spaces(text):
    count = 0
    for char in text:
        if char == " ":
            count += 1
    return count
print(count_spaces(" I_12345I_!#O"))

#4 Повертає рядок без цифр.
def remove_digits(text):
    res = ""
    for item in text:
        if not item.isalpha():
            res += item
    return res
print( remove_digits("ab12cd34"))


def remove_digits(text):
    res = ""
    for item in text:  
        if not item.isdigit():
            res += item
    return res
print( remove_digits("ab-12 cd!"))

#5 Повертає лише цифри.
def only_digits(text):
    res = ""
    for item in text:
        if item.isdigit():
            res += item
    return res
print(only_digits("My phone 12345"))

# 6 Повертає кількість слів без використання split().
def count_words(text):
    count = 0
    text = text.strip()
    for item in text:
        if item == " ":
            count = count +1
    return count+1
print(count_words(" My phone is 12345"))

def count_words(text):
    res = ""
    text = text.strip()
    for i in range(len(text)):
        if text[i] != " " or text[i-1] != " ":
            res += text[i]
    count = 0
    for item in res:
        if item == " ":
            count += 1
    return count
print(count_words(" hello here, dont look like a stingy scrooge"))
    


#7 Повертає перше слово без split().
def first_word(text):
    res = ""
    text = text.strip()
    for item in text:
        if item == " ":
            return res
        res = res + item
    return res
print(first_word(" My phone 12345"))

#8 Повертає останнє слово без split().
def last_word(text):
    text = text.strip()
    new_text = text[::-1]
    res = ""
    for item in new_text:
        if item == " ":
            break
        res = res + item
    return res[::-1]
  
print(last_word(" My phone 12345"))

def last_word2(text):
    l_in = text.rfind(" ")
    l_el = text[l_in+1:]
    return l_el
print(last_word2(" My phone 1234567890"))

#9 
def reverse_words(text):
    text = text.strip().split()
    new_text = text[::-1]
    return " ".join(new_text)
print(reverse_words("I love Python"))
    
#10 Повертає найдовше слово.
def longest_word(text):
    list_text = text.split()
    longest = list_text[0]
    for item in list_text:
       if len(item) > len(longest):
           longest = item
    return longest 
print(longest_word("I love Python"))  

#10 Повертає найдовше слово.
def longest_word(text):
    res = {}
    m = ""
    list_text = text.split()
    for item in list_text:
        res[item] = len(item)
    m = max(res, key=res.get)
    return m
print(longest_word("I love Cabbage"))  '''

#11 Повернути найкоротше слово.
def shortest_word(text):
    text = text.split()
    shortest = text[0]
    for item in text:
        if len(item) < len(shortest):
            shortest = item
    return shortest
print(shortest_word(" hello here, dont look like a stingy scrooge"))
#OR
def shortest_word_2(text):
    res = {}
    shortest = ""
    list_text = text.split()
    for item in list_text:
        res[item] = len(item)
    shortest = min(res, key = res.get)
    return shortest
print(shortest_word(" hello here, dont look like stingy scrooge"))

#12 Порахувати середню довжину слова.
def average_len_word(text):
    total = 0
    list_text = text.split()
    for word in list_text:
        total += len(word)
    average_word = total / len(list_text)
    return average_word
print(average_len_word(" hello here, dont look like stingy scrooge"))

#13 Повернути список усіх слів довших за 5 символів.
def words_longest_then_five(text):
    res = []
    list_text = text.split()
    for word in list_text:
        if len(word) > 5:
            res.append(word)
    return res
print(words_longest_then_five(" hello here, dont look like stingy scrooge"))

#14 Повернути список слів, що починаються з малої літери.
def lower_case_words(text):
    res = []
    list_text = text.split()
    for word in list_text:
        if word[0].islower():
            res.append(word)
    return res
print(lower_case_words(" hello here, Dont Look Like stingy scrooge"))

#15 Повернути список слів, які складаються тільки з літер.
def alphas(text):
    res = []
    l_text = text.split()
    for word in l_text:
        if word.isalpha():
            res.append(word)
    return res
print(alphas("cat dog123 hello!"))

#16 Повернути всі слова без повторень.
def list_with_no_repetition(text):
    res = []
    list_words = text.split()
    for word in list_words:
        if word not in res:
            res.append(word)
    return res
print(list_with_no_repetition("cat dog cat bird dog"))

#17 Порахувати кількість голосних. (англійські: aeiou)
def count_vowels(text):
    v = ["a","e","i","o","u"]
    count = 0
    list_words = list(text)
    for char in list_words:
        if char in v:
            count = count +1
    return count
print(count_vowels("cat dog cat bird dog"))

#18 Порахувати кількість приголосних
def count_conson(text):
    v = ["a", "e","i","o","u"]
    count = 0
    list_words = list(text)
    for char in list_words:
        if char.isalpha() and char not in v:
            count = count +1
    return count
print(count_conson("cat dog cat bird dog"))

#19 Замінити кожну голосну на "*".
def replace_vowels(text):
    v = "aeiou"
    res = ""
    for char in text:
        if char in v:
            char = "*"
            res = res + char
        else:
            res = res + char
    return res
print(replace_vowels("Programming"))

#OR
def replace_vowels(text):
    v = "aeiou"
    res = ""
    for char in text:
        if char in v:
            char = "*"
        res += char
    return res
print(replace_vowels("Programming"))

#20 Перевірити, чи всі літери у рядку маленькі. Повернути True або False. Не використовуй islower().

def lower_string(text):
    for char in text:
        if char.isalpha() and char != char.lower():
            return False
        else:
            return True
print(lower_string("dkfjrjifjoifj"))