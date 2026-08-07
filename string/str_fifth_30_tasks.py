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
        if word[0] == word[-1]:
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
    sh_word = ''
    for word in words:
        if "e" in word and len(word) < len(sh_len) :
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



