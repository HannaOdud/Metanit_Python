print("1.---------------------------------------------")
def list_even_words(text):
    words = text.split()
    even_words = []
    for word in words:
        if len(word.lower()) % 2 == 0:
            even_words.append(word)
    return even_words
print(list_even_words("Apple Amazing Ant  Book  Banana Ball"))

print("2.---------------------------------------------")
def list_even_words2(text):
    words = text.split()
    even_words = []
    for word in words:
        if len(word.lower()) % 2 == 1:
            even_words.append(word)
    return even_words
print(list_even_words2("Apple Amazing Ant  Book  Banana Ball"))

print("3.----------------------------------------------")
def dict_words(text):
    words = text.split()
    res = {}
    for word in words:
        res[word] = word[0]
    return res
print(dict_words("Apple Amazing Ant  Book  Banana Ball"))

print("4.-----------------------------------------------")
def dict_words2(text):
    words = text.split()
    res = {}
    for word in words:
        res[word] = word[-1]
    return res
print(dict_words2("Apple Amazing Ant  Book  Banana Ball"))

print("5.----------------------------------------------")
def end_start_w(text):
    words = text.split()
    res = []
    for word in words:
        if word[0].lower() == word[-1].lower():
            res.append(word)
    return res
print(end_start_w("level apple Anna radar test"))

print("6.------------------------------------------------")
def word_in_range(text):
    words = text.split()
    res = []
    for word in words:
        if len(word) > 4 and len(word) < 8:
            res.append(word)
    return res
print(word_in_range("level apple Anna radar test"))

print("7.-------------------------------------------------")
#Повертає найдовше слово, яке містить букву "a". Без max().
def longest_word_with_a(text):
    words = text.split()

    longest_len = 0
    longest_word = ""
    for word in words:
        if "a" in word:
            if len(word) > longest_len :
                longest_len = len(word)
                longest_word = word
    return longest_word
print(longest_word_with_a("level apple top Anna radaaar test"))

print("8.--------------------------------------------------")
def shortest_word_with_e(text):
    words = text.split()
    sh_len = words[0]
    sh_word = None
    for word in words:
        if "e" in word.lower():
            if len(word) < len(sh_len) :
                sh_len = len(word)
                sh_word = word
    return sh_word
print(shortest_word_with_e("level apple top Anna radaaar test"))

print("9.---------------------------------------------------")
#Повертає список слів, що містять хоча б одну цифру.
def word_with_digit(text):
    words = text.split()
    res = []
    for word in words:
        if any(char.isdigit() for char in word ):
            res.append(word)
    return res
print(word_with_digit("level2 apple top Anna3 3 radaaar test"))

print("10.---------------------------------------------------")
#Повертає список слів, що не містять жодної цифри.
def words_alpha(text):
        words = text.split()
        res = []
        for word in words:
            if not any(char.isdigit() for char in word ):
                res.append(word)
        return res
print(words_alpha("level2 apple top Anna3 3 radaaar test"))

print("11.----------------------------------------------------")
#Порахувати, скільки слів починаються з голосної.
def count_vow(text):
    words = text.split()
    v = ["a","e","i","o","u"]
    count = 0
    for word in words:
        if word[0].lower() in v:
            count += 1
    return count
print(count_vow("level2 apple top Anna3 3 radaaar test"))

print("12.----------------------------------------------------")
def count_vow2(text):
    words = text.split()
    v = ["a","e","i","o","u"]
    count = 0
    for word in words:
        if word[-1].lower() in v:
            count += 1
    return count
print(count_vow2("level2 apple top Anna3 3 radaaar test"))

#Повернути список слів, які починаються і закінчуються голосною.
print("13.----------------------------------------------------")
def count_vow3(text):
    words = text.split()
    v = ["a","e","i","o","u"]
    count_start = 0
    count_end = 0
    res = []
    for word in words:
       if word[0].lower() in v and word[-1].lower() in v:
           res.append(word)
           
    return res
print(count_vow3("level2 apple top Anna 3 radaaar test"))

#Повернути словник
print("14.----------------------------------------------------")
def vow_in_word(text):
    words = text.split()
    v = ["a","e","i","o","u"]
    res = {}
    
    for word in words:
        count = 0
        for char in word.lower():
            if char in v:
                count += 1
        res[word] = count
    return res
print(vow_in_word("level2 apple top Anna 3 radaaar test"))

#Повернути словник слово: кількість_приголосних
print("15.-------------------------------------------------------")
def cons_in_word(text):
    words = text.split()
    cons = ['b', 'c', 'd', 'f', 'g', 'j', 'h', 'q', 'x', 'z', 'l', 'm', 'p', 's', 'r', 'n', 't', 'k','v', 'w', 'y']
    res = {}
    for word in words:
        count = 0
        for char in word.lower():
            if char in cons:
                count += 1
        res[word] = count
    return res
print(cons_in_word("level2 apple top Anna 3 radaaar test"))

#Повернути слово, у якому найбільше голосних. Без max().
print("16.------------------------------------------------------")
def max_vow(text):
    words = text.split()
    v = ["a","e","i","o","u"]
    max_count_vow = 0
    max_word_vow = ""
    for word in words:
        inner_count = 0
        for char in word.lower():
            if char in v:
                inner_count +=1
        if inner_count > max_count_vow:
            max_count_vow = inner_count
            max_word_vow = word
    return max_word_vow        
print(max_vow("level2 apple top Anna 3 radaaar test"))

#Повернути слово, у якому найменше голосних.Без min().
print("17.-------------------------------------------------------")
def min_vow(text):
    words = text.split()
    v = ["a","e","i","o","u"]
    min_word = ""
    min_word_count = float('inf')
    for word in words:
        inner_count = 0
        for char in word.lower():
            if char in v:
                inner_count += 1
        if inner_count < min_word_count:
            min_word_count = inner_count
            min_word = word
    return min_word
print(min_vow("level2 apple top Anna 3tam radaaar test"))

#Повернути список паліндромів.
print("18.-------------------------------------------------------")
def palindrome(text):
    words = text.split()
    res = []
    for word in words:
        if word.lower() == word[::-1].lower():
            res.append(word)
    return res
print(palindrome("level cat radar Anna civic"))

#Повернути словник - довжина_слова: кількість_слів
print("19.------------------------------------------------------")
def len_count(text):
    words = text.split()
    res = {}

    for word in words:
        if len(word) in res:
            res[len(word)] += 1
        else:
            res[len(word)] = 1
    return res
print(len_count("I love Python code"))

#Повернути список слів, довжина яких зустрічається лише один раз.
print("20.------------------------------------------------------")
'''def list_of_single_words(text):
    words = text.split()
    res = []
    for word in words:
        if len(word) not in res:
            res.append(word)
    return res
print(list_of_single_words("level 2top apple top top Anna 3tam radaaar test"))'''

#OR

def list_of_single_words2(text):
    words = text.split()
    all_len = [] 
    res = []
    for word in words:
        all_len.append(len(word))
        
    for word in words:
        if all_len.count(len(word)) == 1:
            res.append(word)
   
    return res
print(list_of_single_words2("level 2top apple top top Anna 3tam radaaar test"))

def list_of_single_words2(text):
    words = text.split()
    len_res = {}
    for word in words:
        length = len(word)
        len_res[length] = len_res.get(length, 0) +1
    res = []
    for word in words:
        if len_res [len(word)] == 1:
            res.append(word)
    return res
print(list_of_single_words2("level 2top apple top top Anna 3tam radaaar test"))

##Повернути список слів, довжина яких зустрічається лише один раз
def list_of_single_words3(text):
    words = text.split()
    words_len = {}
    res = []
    for word in words:
        if len(word) in words_len:
            words_len[len(word)] += 1
        else:
             words_len[len(word)] = 1
    for word in words:
        if words_len[len(word)] == 1:
            res.append(word)
    return res
print(list_of_single_words3("level 2top apppppppple top top Anna 3tam radaaar test"))


print("21.------------------------------------------------------------------")
#Повернути найдовше слово без повторюваних букв.

def longest_no_repet(text):
    words = text.split()
    no_repeat = []
    for word in words:
        if len(word) == len(set(word.lower())):
            no_repeat.append(word)
    longest_word = ""
    longest_len = 0
    print(no_repeat)
    for word in no_repeat:
        if len(word) > longest_len:
            longest_len = len(word)
            longest_word = word
    return longest_word
print(longest_no_repet("level 2top apppppppple top top Anna 3tam radaaar test"))    

print("22.--------------------------------------------------------------------")
#Повернути список слів, у яких усі літери однакові.
#aaa bbbb cat xxxx hello
def all_letters_same(text):
    words = text.split()
    res = []
    for word in words:
        x = len(set(word))
        if (x == 1):
            res.append(word)
    return res
print(all_letters_same("aaa bbbb cat xxxx hello"))

#OR
def all_letters_same2(text):
    words = text.split()
    res = []
    for word in words:
        if word == len(word) * word[0]:
            res.append(word)
    return res
print(all_letters_same2("aaa  hello"))

#OR
def all_letters_same3(text):
    words = text.split()
    res = []
    for word in words:
        if word.count(word[0]) == len(word):
            res.append(word)
    return res
print(all_letters_same3("aaa  hello"))


print("23.--------------------------------------------------------------")
#Повернути список слів, у яких хоча б одна літера повторюється.
def repeated_word(text):
    words =text.split()
    res = []
    for word in words:
        if len(word) > len(set(word.lower())):
            res.append(word)
    return res
print(repeated_word("aaa bbbb cat xxxx hello"))

print("24.------------------------------------------------------------")
#Повернути словник - перша_літера: кількість_слів
def first_letter_count(text):
    words =text.split()
    res = {}
    for word in words:
        if word[0].lower() in res:
            res[word[0].lower() ] += 1
        else:
            res[word[0].lower() ] = 1
    return res
print(first_letter_count("level 2top apppppppple top top Anna 3tam radaaar test"))

print("25.------------------------------------------------------------")
#Повернути слово, яке має найбільшу кількість різних літер. Без max().
def max_different_letter2(text):
    words = text.split()
    max_word = ""
    max_count = 0
    for word in words:
        unique_word = len(set(word.lower()))
        if unique_word > max_count:
            max_count = unique_word
            max_word = word
    return max_word
print(max_different_letter2("level 2top apppppppple top top Anna 3tam radaaar test"))

print("26.---------------------------------------------------------------")