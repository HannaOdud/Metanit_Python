#1 Напиши функцію.
#Повертає словник, де:
#ключ — кількість голосних у слові;
#значення — список слів із такою кількістю голосних.
def group_by_vowels(text):
    words = text.split()
    vowels = ["a","e","i","o","u"]
    res = {}
    for word in words:
        count_vowels = 0
        for char in word:
            if char.lower() in vowels:
                count_vowels += 1
        if count_vowels not in res:
            res[count_vowels] = []
        res[count_vowels].append(word)
    return res
print(group_by_vowels("cat dog elephant book"))    

#2 Напиши функцію.
#Повертає слово, у якому найбільше різних букв.
#Без max().
def most_different_letter(text):
    words = text.split()
    count_letter = 0
    diff_letter_word = ""
    for word in words:
        if len(set(word)) > (count_letter):
            diff_letter_word = word
            count_letter = len(set(word))
    return diff_letter_word
print(most_different_letter("cat dog elephant book"))

#OR
def most_different_letter2(text):
    words = text.split()
    res = {} 
    for word in words:
        res[word] = len(set(word))
    max_diff_letter = max(res, key=res.get)
    return max_diff_letter
print(most_different_letter2("cat dog elephant book"))
print("3--------------------------------------------------------")
#3 Напиши функцію.Повертає список слів, у яких усі літери різні.
def word_with_all_diff_letter(text):
    words = text.split()
    res = []
    for word in words:
        if len(word) == len(set(word)):
            res.append(word)
    return res
print(word_with_all_diff_letter("cat apple moon dog"))

#OR
def word_with_all_diff_letter2(text):
    words = text.split()
    res = []
    for word in words:
        appeared_letters = []
        for char in word:
            if char in appeared_letters:
                break
            else:
                appeared_letters.append(char)
        #print(appeared_letters)
        if len(word) == len(appeared_letters):
            res.append(word)
    return res
print(word_with_all_diff_letter2("cat apple moon dog"))

#OR
def word_with_all_diff_letter3(text):
    words = text.split()
    res = []
    for word in words:
        letter_count = {}
        has_duplicate = False
        for char in word:
            if char in letter_count:
                has_duplicate = True
                break
            else:
                letter_count[char] = 1
        if not has_duplicate:
            res.append(word)     
    return res
print(word_with_all_diff_letter3("cat apple moon dog"))

#4 Напиши функцію  перша_літера : найдовше_слово
print("4---------------------------------------------------")
def first_word_and_longest(text):
    words = text.split()
    res = {}
    for word in words:
        if word[0] in res:
            if len(word) > len(res[word[0]]):
                res[word[0]] = word
        else:
            res[word[0]] = word
    return res    
               
print(first_word_and_longest("Apple Amazing Ant  Book  Banana Ball"))