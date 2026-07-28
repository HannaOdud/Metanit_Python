'''#1 Напиши функцію. Повертає словник, де:
# #ключ — перша літера слова; 
# #значення — кількість слів, що починаються на цю літеру.

def first_letter_count(text):
    words = text.split()
    res = {}
    for word in words:
        if word[0] in res:
            res[word[0]] += 1
        else:
            res[word[0]] = 1
    return res
print(first_letter_count("Apple Ant Banana Ball Cat"))

#2 Напиши функцію.Повертає найдовше слово, що містить хоча б одну цифру.
def longest_with_num(text):
    longest = ""
    words = text.split()
    for word in words:
        if any(char.isdigit() for char in word):
            if len(word) > len(longest):
                longest = word
    return longest
print(longest_with_num("I am abc123 Programming22 test1"))

#OR
def longest_with_num1(text):
    longest = ""
    words = text.split()
    for word in words:
        for char in word:
            if char.isdigit():
                if len(word) > len(longest):
                    longest = word
                break
    return longest
print(longest_with_num1("I am abcdefg123 test1"))

#3 Напиши функцію. Повертає список слів, довжина яких більша за середню довжину всіх слів.
def longer_words(text):
    res = []
    total = 0
    words = text.split()

    for word in words:
        total = total + len(word)
    average = total / len(words)
    for word in words:
        if len(word) > average:
            res.append(word)
    return res
print(longer_words("hello here, dont look like a stingy scrooge"))

#4  
def len_and_sum_words(text):
    res = {}
    words = text.split()

    for word in words:
        if len(word) in res:  
            res[len(word)] = res[len(word)] + 1
        else:
            res[len(word)] = 1
    return res
print(len_and_sum_words("hello here dont look like a stingy scrooge"))

#OR
def len_and_sum_words1(text):
    res = {}
    words = text.split()
    for word in words:
        clean_word = ""
        for char in word:
            if char.isalpha():
                clean_word +=char
        if len(clean_word) in res:
            res[len(clean_word)] = res[len(clean_word)] + 1
        else:
            res[len(clean_word)] = 1
    return res
print(len_and_sum_words1("hello here, dont !look #like a stingy scrooge"))

#OR 
def len_and_sum_words2(text):
    clean_text = ""
    for char in text:
        if char.isalpha() or char ==" ":
            clean_text += char
    clean_text = clean_text.split()
    #print(clean_text)
    res = {}
    for word in clean_text:
        if len(word) in res:
            res[len(word)] =  res[len(word)] + 1
        else:
            res[len(word)] = 1
    return res
print(len_and_sum_words2("hello here, dont !look #like a stingy scrooge"))

#5 Напиши функцію. Повертає слово, яке зустрічається найчастіше. Без max().
def most_frequent_word(text):
    words = text.split()
    most_frequent = {}
    for word in words:
        if word in most_frequent:
            most_frequent[word] += 1
        else:
            most_frequent[word] = 1 
    max_appear = 0
    max_appear_word = ""
    for key, value in most_frequent.items():
        if value > max_appear:
            max_appear_word = key
            max_appear = value
    return max_appear_word   
print(most_frequent_word("hello here dont look here like a stingy scrooge"))

#OR

def most_frequent_word2(text):
    words = text.split()
    res = {}
    max_frequent_word = ""
    max_frequent_count = 0

    for word in words:
        count = words.count(word)
        if count > max_frequent_count:
            max_frequent_count = count
            max_frequent_word = word
    return max_frequent_word
print(most_frequent_word2("hello here dont look here like a stingy scrooge"))

#6 Напиши функцію.Перевіряє, чи є слово паліндромом.
def check_palindrome(text):
    pal_text = text[::-1]
    if text == pal_text:
        return True
    else:
        return False
print(check_palindrome("level"))
print(check_palindrome("levell"))'''

#OR
def check_palindrome2(text):

    rev_list = reversed(text)
    back = "".join(rev_list)
    #back = "".join(reversed(text))
    if text == back:
        return True
    else:
        return False
     
print(check_palindrome2("level"))
print(check_palindrome2("leveel"))

#7 Напиши функцію. Повертає список усіх паліндромів у реченні.
def list_of_palindrome(text):
    text = text.split()
    all_palindromes = []

    for word in text:
        if word == word[::-1]:
            all_palindromes.append(word)
    return all_palindromes
print(list_of_palindrome("level of level is levell"))
print("**************************************************")

#8 Напиши функцію. Замінює кожне слово його довжиною.
def replace_word_by_length(text):
    res = []
    words = text.split()
    for word in words:
        word_len = str(len(word))
        res.append(word_len)
    result = " ".join(res)
    return result
print(replace_word_by_length("level of level is levell"))
#OR   
def rep_len(text):
    words = text.split()
    res = []
    for word in words:
        len_word = str(len(word))
        res.append(len_word)
    return " ".join(res)
print(rep_len("level of level is levell"))
print("--------------------------------------------------")

#9 Напиши функцію. Повертає слово, у якому найбільше голосних. 
def word_with_max_vowels(text):
  
    v = ["a","e","i","o","u"]
    max_vow = ""
    max_count = 0
    words = text.split()
    for word in words:
        count = 0
        for char in word:
            if char in v:
                count += 1
        if count > max_count:
            max_count = count
            max_vow = word
    return max_vow
print(word_with_max_vowels("level of levl "))

#10 Напиши функцію. Повертає список слів, які містять лише великі літери.
def word_with_upper_only(text):
    words = text.split()
    res = []
    for word in words:
        if word == word.upper() and len(word) > 1:
            res.append(word)
    return res
print(word_with_upper_only("I LOVE Python USA Kyiv"))

#11 Напиши функцію. Повертає словник
def return_dict_with_vowels(text):
    words = text.split()
    result = {}
    v = ["a","e","i","o","u"]
    for word in words:
        count = 0
        for char in word:
            if char in  v :
                count += 1
        result[word] = count
    return result
print(return_dict_with_vowels("hello here dont look here like a stingy scrooge"))

#12 Напиши функцію.Видаляє всі слова, довші за 7 символів.
def longer_words(text):
    words = text.split()
    result = []
    for word in words:
        if len(word) > 7:
            result.append(word)
    return result
print(longer_words("hello here dont look here like a stingy scroooge"))

#13 Напиши функцію.Повертає всі слова, у яких однакова перша й остання літера.
def same_letter(text):
    words = text.split()
    res = []
    for word in words:
        if word[0] == word[-1]:
            res.append(word)
    return res
print(same_letter("Anna level test dad"))
print("-----------------------------------------------------")
#14 Напиши функцію. Повертає найдовше слово без жодної цифри.
def longest_word_no_num(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest) and word.isalpha():
            longest = word       
    return longest
print(longest_word_no_num("hell8o here dont lo2ok here like a stingy sc1roooge"))

#15 Напиши функцію. Повертає кількість різних слів (без повторень).
def unique_words(text):
    words = text.split()

    unique = []
    for word in words:
        if word not in unique:
            unique.append(word)
    return unique
print(unique_words("hello here dont look here like a stingy scroooge"))

#16 Напиши функцію.(Слово: остання літера) Повертає словник
def word_with_last_letter(text):
    words = text.split()
    res = {}
    for word in words:
        res[word] = word[-1]
    return res
print(word_with_last_letter("hello here dont look here like a stingy scroooge"))
print("-------------------------------------------------------")
#17 Перевіряє, чи всі слова мають різну довжину.Повертає True або False.
def check_the_length(text):
    words = text.split()
    res = {}
    for word in words:
        if len(word) in res:
            res[len(word)] += 1
        else:
            res[len(word)] = 1 
    print(res)
    for value in res.values():
        if value > 1:
            return False
    return True
print(check_the_length("hello here dont look here like a stingy scroooge"))
print("**********************************************************")
#OR
def check_the_length2(text):
    words = text.split()
    len_of_words = []
    for word in words:
        if len(word) in len_of_words:
            return False
        len_of_words.append(len(word)) 
    return True
print(check_the_length2("hello here a stingy scroooge"))

#OR
def check_the_length3(text):
    words = text.split()
    list_of_len_words = []
    for word in words:
        list_of_len_words.append(len(word))
    set_of_len_words = set(list_of_len_words)
    if len(list_of_len_words) == len(set_of_len_words):
        return True
    return False
print(check_the_length3("hello here here  here a stingy scroooge"))

# OR
def check_the_length4(text):
    words = text.split()
    res_dic = {}
    for word in words:
        if len(word) in res_dic:
            return False
        res_dic[len(word)] = 1
    return True
print(check_the_length4("hello here grer a stingy scroooge"))










            
