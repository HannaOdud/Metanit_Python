print("1.--------------------------------------------------")
# Слова з максимальною частотою
# Поверни всі слова, які зустрічаються найбільше разів.
def words_with_max_frequency(text):
    words = text.split()
    max_count = 0
    dict_words = {}
    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1
    for key,value in dict_words.items():
        if value > max_count:
            max_count = value
    res = []
    for key,value in dict_words.items():
        if value == max_count:
            res.append(word)
    return res
print(words_with_max_frequency("cat dog cat bird dog"))

print("2.------------------------------------------------")
# Найкоротше слово серед тих, що повторюються
# Слово повинно зустрічатися хоча б двічі. Серед таких слів знайди найкоротше.
# Без min().
def shortest_repeated_word(text): 
    words = text.split()
    dict_words = {} 
    for word in words:
        dict_words[word] = dict_words.get(word, 0)+1
    shortest = ""
    len_shortest = float("inf")
    for key,value in dict_words.items():
        if len(key) < len_shortest and  value >= 2:
            len_shortest = len(key)
            shortest = key
    return shortest
print(shortest_repeated_word("Apple Ant Ant Amazing Amazing Ball Book Banana Cat"))

print("3.-------------------------------------------------")
# Найдовше слово серед унікальних
# Слово повинно зустрічатися рівно один раз. Без max().
def longest_unique_word(text):
    words = text.split()
    dict_words = {} 
    for word in words:
        dict_words[word] = dict_words.get(word, 0)+1
    res = []
    for key, value in dict_words.items():
        if value == 1:
            res.append(key) 
    max_word = ""
    max_word_len = 0
    for word in res:
        if len(word) > max_word_len:
            max_word_len = len(word)
            max_word = word
    return max_word
print(longest_unique_word("Apple Ant Ant Amazing Amazing Ball Book Banana Cat"))