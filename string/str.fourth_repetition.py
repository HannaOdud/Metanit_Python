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
def first_letter_and_longest_word(text):
    words = text.split()
    res = {}
    for word in words:
        for word in words:
            first_char = word[0]
            if first_char not in res:
                res[first_char] = word
            else:
                if len(word) > len(res[first_char]):
                    res[first_char] = word
    return res
print(first_letter_and_longest_word("Apple Ant Amazing Book Ball Banana"))