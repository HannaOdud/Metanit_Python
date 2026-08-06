print("1------------------------------------------------------------")
'''Повертає словник, де:

ключ — кількість голосних у слові;
значення — список слів із такою кількістю голосних.
{
    1: ["cat", "dog"],
    2: ["book"],
    3: ["elephant"]
}
''' 
def group_by_vowels2(text):
    words = text.split()
    vowels = ["a", "e", "i", "o", "u"]
    res = {}
    for word in words:
        tot_vow = 0
        for char in word:
            if char in vowels:
                tot_vow += 1
        if tot_vow not in res:
            res[tot_vow] = []
        res[tot_vow].append(word)
    return res

print(group_by_vowels2("cat dog wolf elephant book"))

print("2-------------------------------------------------------------")
def word_with_max_diff_letters(text):
    words = text.split()
    winner_word = ""
    count_letter = 0
    for word in words:
        if len(set(word)) > count_letter:
            count_letter = len(word)
            winner_word = word
    return winner_word
print(word_with_max_diff_letters("cat dog wolf elephant book"))


print("3--------------------------------------------------------------")
'''Напиши функцію.
Повертає список слів, у яких усі літери різні.
Наприклад
"cat apple moon dog"
↓
["cat", "dog"]'''
def diff_letter_words(text):
    words = text.split()
    res = []
    for word in words:
        if len(word) == len(set(word)):
            res.append(word)
    return res
print(diff_letter_words("cat apple moon dog"))

print("4--------------------------------------------------------------")
'''
Напиши функцію.
Повертає словник
{
    перша_літера : найдовше_слово
}
Наприклад
"Apple Ant Amazing Book Ball Banana"
↓
{
    "A": "Amazing",
    "B": "Banana"
}
'''
def first_letter_and_longest_word(text):
    words = text.split()
    res = {}
    for word in words:
        if word[0] in res:
            if len(word) > len(res[word[0]]):
                res[word[0]] = word
        else:
            res[word[0]] = word
            
    return res
print(first_letter_and_longest_word("Apple Ant Amazing Book Ball Banana"))

#OR
def first_letter_and_longest_word2(text):
    words = text.split()
    res = {}
    for word in words:
        for char in word:
            first_char = word[0]
            if first_char not in res:
                res[first_char] = word
            else:
                if len(word) > len(res[first_char]):
                    res[first_char] = word
    return res
print(first_letter_and_longest_word2("Apple Ant Amazing Book Ball Banana"))

#OR
def first_letter_and_longest_word3(text):
    words = text.split()
    res = {}
    for word in words:
        if word[0] not in res:
            res[word[0]] = word
        else:
            if len(word) > len(res[word[0]]):
                res[word[0]] = word
    return res
print(first_letter_and_longest_word3("Apple Ant Amazing Book Ball Banana"))

print("5---------------------------------------------------------------")
#Напиши функцію.Повертає слово, у якому найбільше приголосних.
def word_con(text):
    words = text.split()
    cons = ['b', 'c', 'd', 'f', 'g', 'j', 'h', 'q', 'x', 'z', 'l', 'm', 'p', 's', 'r', 'n', 't', 'k']
    cons_tot_word = 0
    cons_word = ""
    for word in words:
        tot_cons = 0
        for char in word:
            if char in cons:
                tot_cons += 1
        if tot_cons > cons_tot_word:
            cons_tot_word = tot_cons
            cons_word = word
    return cons_word
print(word_con("Apple Ant Amazing Book Ball Banana"))

print("6-------------------------------------------------------------")
'''
Напиши функцію.Перевіряє, чи всі слова починаються з різних літер. Повертає True або False.
'''
def diff_first_letter(text):
    words = text.split()
    first_letter = [word[0].lower() for word in words ]
    print(first_letter)
    
    return len(first_letter) == len(set(first_letter))
print(diff_first_letter("Apple Ant Amazing Book Ball Banana"))

print("7--------------------------------------------------------------")
'''
Напиши функцію.
Повертає словник
{
    слово : кількість_різних_букв
}
'''
def word_set_letters(text):
    words = text.split()
    res = {}
    for word in words:
        res[word] = len(set(word.lower()))
    return res
print(word_set_letters("Apple Ant Amazing Book Ball Banana"))      

print("8--------------------------------------------------------------")
'''Напиши функцію.
Повертає список слів, які містять більше голосних, ніж приголосних.'''
def more_vow_then_cons(text):
    words = text.split()
    cons = ['b', 'c', 'd', 'f', 'g', 'j', 'h', 'q', 'x', 'z', 'l', 'm', 'p', 's', 'r', 'n', 't', 'k','v', 'w', 'y']
    vow = ["a","e","i","o","u"]
    res = []
    
    for word in words:
        count_vow = 0
        count_cow = 0
        for char in word.lower():
            if char in cons:
                count_cow += 1
            if char in vow:
                count_vow += 1
        if count_vow > count_cow:
            res.append(word.lower())
    return res
print(more_vow_then_cons("Apple Ant Amazing Book Ball Banana ana"))

print("9--------------------------------------------------------------")
'''Напиши функцію.Повертає найдовше слово, яке зустрічається лише один раз.
Без max().
'''
def longest_word(text):
    words = text.split()
    longest_word = ""
    longest_len = words[0]
    res = []
    for word in words:
        if len(word.lower()) > len(longest_len):
            longest_len = word
            longest_word = word
    #res.append(set(longest_word))
    return longest_word
   
print(longest_word("Apple Ant Amazing Amazing Book Ball Banana ana"))
