#1 Напиши функцію. Повертає словник, де:
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

    

            





            
