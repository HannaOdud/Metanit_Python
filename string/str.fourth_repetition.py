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
    for word in words:
        if len(word.lower()) > len(longest_len) and words.count(word) == 1:
            longest_len = word
            longest_word = word
    
    return longest_word
   
print(longest_word("Apple Ant Amazing Amazing Book Ball Banana ana"))


def single_appear_of_longest_word(text):
    words = text.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest) and words.count(word.lower()) == 1:
            longest = word
    return longest
        
print(single_appear_of_longest_word("Apple Amazing Amazing Ant  Book  Banana Ball"))  

print("10---------------------------------------------------------------")
def sorted_text(text):
    words = text.split()
    n = len(words)

    for i in range(n - 1):
        for j in range(0, n - 1 -i):
            if len(words[j]) > len(words[j + 1]):
                temp = words[j]
                words[j] = words[j + 1] 
                words[j + 1] = temp

    return words
print(sorted_text("pear dog banana cat apple"))

def sorted_list(text):
    words = text.split()
    sort_words = sorted(words, key=lambda word:(len(word),word))
    return sort_words
print(sorted_list("Apple Amazing Amazing Ant  Book  Banana Ball"))

print("11---------------------------------------------------------------")

def comp_dict(text):
    words = text.split()
    res = {}
    for word in words:
        if len(word) not in res:
            res[len(word)] = {word: 1}
        else:
            inner_dict = res[len(word)]
            if word in inner_dict:
                inner_dict[word] += 1
            else:
                inner_dict[word] = 1
    return res
print(comp_dict("Apple Amazing Amazing Ant  Book  Banana Ball"))

print("12---------------------------------------------------------------")
def word_max_char(text):
    words = text.split()
    max_same_char = ""
    max_same_value = 0
    for word in words:
        char_dict = {}
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else: 
                char_dict[char] = 1
        max_val = max(char_dict.values())
        if max_val > max_same_value:
            max_same_value = max_val
            max_same_char = word
    return max_same_char
print(word_max_char("Apple Amazing Amazing Ant  Book  Banana Ball"))



