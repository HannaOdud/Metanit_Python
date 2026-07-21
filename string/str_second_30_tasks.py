#1 Повертає кількість літер у рядку (ігноруючи цифри, пробіли та розділові знаки).
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
        if item.isalpha():
            res += item
    return res
print( remove_digits("ab12cd34"))

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
    for item in text:
        if item == " ":
            count = count +1
    return count
print(count_words(" My phone is 12345"))

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











'''#*8* Повертає останнє слово без split().

def last_word(text):
    text = text.strip()
    to_list = list(text)
    res = []
    for item in to_list:
        if item == item[-1]:
            res.append(item)
        res = " ".join(res)
    return res
print(last_word(" My phone 12345")) '''

'''#10 Повертає найдовше слово.
def longest_word(text):
    res = {}
    list_text = text.split()
    for item in list_text:
        res[item] = len(item)
    for key, value in res.items():
        max(value)
    return max(value)
    
print(longest_word("I love Python"))  '''


