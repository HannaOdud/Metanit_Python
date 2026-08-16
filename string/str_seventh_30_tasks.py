print("1.-----------------------------------------------------------")
# Повернути список слів, довжина яких парна.
def list_even_len(text):
    words = text.split()
    res = []
    for word in words:
        if len(word) % 2 == 0:
            res.append(word)
    return res
print(list_even_len("Apple cat elephant dog"))

print("2.----------------------------------------------------------")
# Повернути список слів, довжина яких непарна.
def list_odd_len(text):
    words = text.split()
    res = []
    for word in words:
        if len(word) % 2 == 1:
            res.append(word)
    return res
print(list_odd_len("Apple cat elephant dog"))

print("3.------------------------------------------------------------")
#Створити словник: слово → перша літера
def dict_word_fchar(text):
    words = text.split()
    res = {}
    for word  in words:
        res[word] = word[0]
    return res
print(dict_word_fchar("Apple cat elephant dog"))

print("4.------------------------------------------------------------")
#Створити словник: слово → last літера
def dict_word_lchar(text):
    words = text.split()
    res = {}
    for word  in words:
        res[word] = word[-1]
    return res
print(dict_word_lchar("Apple cat elephant dog"))

print("5.------------------------------------------------------------")
# Повернути слова, у яких перша і остання літери однакові без урахування регістру.
def first_last_char(text):
    words = text.split()
    res = []
    for word  in words:
        if word[0].lower() == word[-1].lower():
            res.append(word)
    return res
print(first_last_char("level Anna apple elephant radar Test"))

print("6.----------------------------------------------------------")
# Повернути слова, довжина яких від 5 до 8 символів включно.
def spec_len(text):
    words = text.split()
    res = []
    for word in words:
        if len(word) >= 5 and len(word) <= 8:
            res.append(word)
    return res
print(spec_len("level Anna apple elephant radar Test"))

print("7.-----------------------------------------------------------")
# Повернути словник:   слово → кількість приголосних
def dict_cons_count(text):
    words = text.split()
    res = {}
    vows = ["a","e","i","o","u"] 
    
    for word in words:
        count_cons = 0
        for char in word:
            if char.lower() not in vows and char.isalpha():
                count_cons += 1
        res[word] = count_cons
    return res
print(dict_cons_count("level An2na apple ele2phant radar Test"))

print("8.----------------------------------------------------------")
# Повернути список слів, у яких кількість приголосних більша за кількість голосних.
def con_more_then_vows(text):
    words = text.split()
    vows = ["a","e","i","o","u"] 
    res = []
    for word in words:
        total_cons = 0
        total_vows = 0
        for char in word: 
            if char.lower() in vows:
                total_vows += 1
            elif char.isalpha():
                total_cons += 1
        if total_cons > total_vows:
            res.append(word)
    return res
print(con_more_then_vows("level An2na apple ele2phant radar Test"))

print("9.--------------------------------------------------------------")
# Повернути список слів, які містять хоча б одну цифру.
def has_digit(text):
    words = text.split()
    res = []
    for word in words:
        if any(char.isdigit() for char in word):
            res.append(word)
    return res 
print(has_digit("level An2na apple ele2phant radar Test"))
#OR
def has_digit2(text):
    words = text.split()
    res = []
    for word in words:
        has_digit = False
        for char in word:
            if char.isdigit():
                has_digit = True
        if has_digit:
            res.append(word) 
    return res            
print(has_digit2("level An2na apple ele2phant radar Test"))

print("10.--------------------------------------------------------------")
# Повернути список слів, які не містять цифр.
def all_alpha(text):
    words = text.split()
    res = []
    for word in words:
        if all(char.isalpha() for char in word):
            res.append(word)
    return res
print(all_alpha("level An2na apple ele2phant radar Test"))
#OR
def all_alpha2(text):
    words = text.split()
    res = []
    for word in words:
      if word.isalpha():
          res.append(word)
    return res
print(all_alpha2("level An2na apple ele2phant radar Test"))

print("11.----------------------------------------------------------------")
# Порахувати, скільки слів починаються з голосної.