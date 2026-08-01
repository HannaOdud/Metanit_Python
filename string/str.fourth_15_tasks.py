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
print("5---------------------------------------------------------")
#5 Напиши функцію. Повертає слово, у якому найбільше приголосних.
def most_cons_word(text):
    words = text.split()
    cons = ['b', 'c', 'd', 'f', 'g', 'j', 'h', 'q', 'x', 'z', 'l', 'm', 'p', 's', 'r', 'n', 't', 'k']
    res = {}
    for word in words:
        count_cons = 0
        for char in word:
            if char.lower() in cons:
                count_cons += 1
        res[word] = count_cons
    max_word = max(res, key=res.get)
    return max_word
print(most_cons_word("Apple Amazing Ant  Book  Banana Ball"))

#OR
def most_cons_word2(text):
    words = text.split()
    cons = ['b', 'c', 'd', 'f', 'g', 'j', 'h', 'q', 'x', 'z', 'l', 'm', 'p', 's', 'r', 'n', 't', 'k']
    max_cons = 0
    max_cons_word = ""
    for word in words:
        count_cons = 0
        for char in word:
            if char in cons:
                count_cons += 1
        if count_cons > max_cons:
            max_cons = count_cons
            max_cons = word
    return max_cons_word

print(most_cons_word("Apple Amazing Ant  Book  Banana Ball"))    
print("6-------------------------------------------------------------------------")
#6 Напиши функцію. Перевіряє, чи всі слова починаються з різних літер. Повертає True або False.
def first_letter_all_different(text):
    words = text.split()
    first_letter = []
    for word in words:
        first_letter.append(word[0].lower())
    return len(first_letter) == len(set(first_letter))
          
print(first_letter_all_different("Apple Amazing Ant  Book  Banana Ball"))
print(first_letter_all_different("Apple Cat Ball"))
print("7------------------------------------------------------------------------")
#7 Напиши функцію. Повертає словник  {слово : кількість_різних_букв}
def dict_word_diff_letter(text):
    words = text.split()
    res = {}
    for word in words:
        letter_dict = {}
        for char in word:
            letter_dict[char.lower()] = True
        res[word] = len(letter_dict)    
    return res
print(dict_word_diff_letter("Apple Amazing Ant  Book  Banana Ball"))

def dict_word_diff_letter(text):
    words = text.split()
    res = {}
    for word in words:
        res[word] = len(set(word))
    return res
print(dict_word_diff_letter("Apple Amazing Ant  Book  Banana Ball"))
    #OR
def word_and_diff_letters(text):
    words = text.split()
    res = {}
    for word in words:
        res[word] = len(set(word.lower()))
    return res
print(word_and_diff_letters("Apple Amazing Ant  Book  Baana Ball"))

print("8----------------------------------------------------------")
#8 Напиши функцію. Повертає список слів, які містять більше голосних, ніж приголосних.
def words_with_more_vowels(text):
    words = text.split()
    res = []
    cons = ['b', 'c', 'd', 'f', 'g', 'j', 'h', 'q', 'x', 'z', 'l', 'm', 'p', 's', 'r', 'n', 't', 'k','v', 'w', 'y']
    vow  = ["a","e","i","o","u"]
    for word in words:
        count_cons = 0
        count_vow = 0
        for char in word:
            if char.lower() in cons:
                count_cons += 1   
            if char.lower() in vow:
                count_vow +=1
        if count_vow > count_cons:
            res.append(word)
    return res
print(words_with_more_vowels("Apple Amazing Ant  Book  Baana Ball"))

print("9----------------------------------------------------------")
#9 Напиши функцію. Повертає найдовше слово, яке зустрічається лише один раз. Без max().
def single_appear_of_longest_word(text):
    words = text.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest) and words.count(word) == 1:
            longest = word
    return longest
        
print(single_appear_of_longest_word("Apple Amazing Amazing Ant  Book  Banana Ball"))   


