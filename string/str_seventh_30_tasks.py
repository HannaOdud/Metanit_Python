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
def start_with_vow(text):
    words = text.split()
    vows = ["a","e","i","o","u"] 
    count = 0
    for word in words:
        if word[0].lower() in vows:
            count += 1
    return count
print(start_with_vow("level An2na apple ele2phant radar Test"))

print("12.---------------------------------------------------------------")
# Порахувати, скільки слів закінчуються голосною.
def last_char_vow(text):
    words = text.split()
    vows = ["a","e","i","o","u"] 
    count = 0
    for word in words:
        if word[-1].lower() in vows:
                count += 1
    return count
print(last_char_vow("level An2na apple ele2phant radar Test"))

print("13.---------------------------------------------------------------")
# Повернути слова, які одночасно починаються і закінчуються голосною.
def first_and_last(text):
    words = text.split()
    vows = ["a","e","i","o","u"] 
    count = 0
    for word in words:
        if word[0].lower() in vows and word[-1].lower() in vows:
            count += 1
    return count
print(first_and_last("level Anna apple ele2phant radar Test"))

print("14.-----------------------------------------------------------------")
# Повернути словник: слово → кількість голосних
def dict_count_vow(text):
    words = text.split()
    vows = ["a","e","i","o","u"] 
    res = {}
    for word in words:
        count = 0
        for char in word:
            if char.lower() in vows:
                count += 1
        res [word] = count 
    return res 
print(dict_count_vow("level Anna apple ele2phant radar Test"))

print("15.-----------------------------------------------------------")
# Повернути слово, у якому найменше голосних. 
def min_vow_word(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    min_vows_word = ""
    min_vow_len = float("inf") 
    for word in words:
        count = 0
        for char in word:
            if char.lower() in vows:
                count += 1
        if  count < min_vow_len :
            min_vow_len = count
            min_vows_word = word
    return min_vows_word
print(min_vow_word("level Anna apple ele2phant radar Test"))
#
def min_vow_word(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    min_vows_word = ""
    min_vow_len = float("inf") 
    for word in words:
        count = sum(1 for char in word.lower() if char in vows)
        if  count < min_vow_len :
            min_vow_len = count
            min_vows_word = word
    return min_vows_word
print(min_vow_word("level Anna apple ele2phant radar Test"))

print("16.--------------------------------------------------------------------")
# Повернути слово, у якому найбільше голосних. Без max().
def max_vows_word(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    max_vow_word = ""
    max_vow_len = float("-inf")
    for word in words:
        count = 0
        for char in word:
            if char.lower() in vows:
                count += 1
        if count > max_vow_len:
            max_vow_len = count
            max_vow_word = word
    return max_vow_word
print(max_vows_word("level Anna apple ele2phant radar Test"))

print("17.-----------------------------------------------------------------")
# Повернути найдовше слово, яке містить не менше двох голосних. Без max().
def max_len_word(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    max_word = ""
    for word in words:
        count = 0
        for char in word:
            if char.lower() in vows:
                count += 1
        if len(word) > len(max_word) and count >= 2:
            max_word = word
    return max_word
print(max_len_word("level Anna apple ele2phant radar Test"))

print("18.------------------------------------------------------------------")
# Порахувати кількість слів, у яких голосних більше, ніж приголосних.
def count_vow_words(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    count = 0
    for word in words:
        tot_vows = 0
        tot_cons = 0
        
        for char in word:
            if char.lower() in vows:
                tot_vows += 1
            elif  char.isalpha():
                tot_cons += 1
        if tot_vows > tot_cons:
            count += 1
    return count
print(count_vow_words("level Anna apple ele2phant aaan radar Test"))

#OR
def count_vow_words2(text):
    words = text.split()
    vows = ["a","e","i","o","u"]

    count = 0
    for word in words:
        tot_vows = sum(1 for char in word.lower() if char in vows)
        tot_cons = sum(1 for char in word.lower() if char.isalpha() and char not in vows)
        if tot_vows > tot_cons:
            count += 1
    return count
print(count_vow_words("level Anna apple ele2phant aaan radar Test"))


print("19.-------------------------------------------------------------------")
# Повернути список слів, у яких кількість голосних дорівнює кількості приголосних.
def vows_equal_cons(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    res = []
    for word in words:
        tot_vow = sum(1 for char in word.lower() if char in vows)
        tot_cons = sum(1 for char in word.lower() if char.isalpha() and char not in vows)
        if tot_vow == tot_cons:
            res.append(word)
    return res
print(vows_equal_cons("level Anna apple ele2phant aaan radar Test"))

print("20.---------------------------------------------------------------------")
# довжина слова → кількість слів
def dict_len_tot_words(text):
    words = text.split()
    res = {}
    for word in words:
        if len(word) in res:
            res[len(word)] += 1
        else:
            res[len(word)] = 1
    return res
print(dict_len_tot_words("level Anna apple ele2phant aaan radar Test"))

#OR
def dict_len_tot_words2(text):
    words = text.split()
    res = {}
    for word in words:
        res[len(word)] = res.get(len(word), 0) +1
    return res
print(dict_len_tot_words2("level Anna apple ele2phant aaan radar Test"))


