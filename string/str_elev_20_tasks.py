print("1.-------------------------------------------")
# Перше слово, яке зустрічається двічі
def first_repeated_word(text):
    words = text.split()
    checked = []
    repeated = []
    for word in words:
        if word in checked:
            repeated.append(word)
        checked.append(word)
    return repeated[0]
print(first_repeated_word("cat dog bird dog cat"))
#OR
def first_repeated_word2(text):
    words = text.split()
    checked = []
    for word in words:
        if word in checked:
            return word  
        checked.append(word)    
print(first_repeated_word2("cat cat dog bird dog cat"))
#
def first_repeated_word3(text):
    words = text.split()
    checked = set()
    for word in words:
        if word in checked:
            return word  
        checked.add(word)    
print(first_repeated_word3("cat cat dog bird dog cat"))

print("2.------------------------------------------")
# Перше слово, яке зустрічається один раз
def first_unique_word(text):
    words = text.split()
    checked = []
    repeated = []
    for word in words:
        if word in checked:
            repeated.append(word)
        checked.append(word)
    for word in words:
        if word not in repeated:
            return word
    return ""
print(first_unique_word("cat dog cat bird bird dog house"))

print("3.------------------------------------------")
# Усі унікальні слова
# Поверни список усіх слів, які зустрічаються рівно один раз.
def unique_words(text):
    words = text.split()
    checked = []
    repeated = []
    res = []
    for word in words:
        if word in checked:
            repeated.append(word)
        checked.append(word)
    for word in words:
        if word not in repeated:
            res.append(word)
    return res
print(unique_words("cat dog cat bird house dog"))

print("4.---------------------------")
# Усі слова, які повторюються
def repeated_words(text):
    words = text.split()
    repeated = []
    checked = []
    for word in words:
        if word in checked:
            repeated.append(word)
        checked.append(word)
    return set(repeated)
print(repeated_words("cat dog cat bird dog cat"))

print("5.--------------------------")
# Скільки унікальних слів
# Поверни кількість слів, які зустрічаються рівно один раз.
def count_unique_words(text):
    words = text.split()
    w_dict = {}
    res = []
    for word in words:
        w_dict[word] = w_dict.get(word, 0) +1
    for key,value in w_dict.items():
        if value == 1:
            res.append(key)
    return len(res)
print(count_unique_words("cat dog cat bird house dog"))
#OR
def count_unique_words2(text):
    words = text.split()
    repeated = []
    checked = []
    res = []
    for word in words:
        if word in checked:
            repeated.append(word)
        checked.append(word)
    for word in words:
        if word not in repeated:
            res.append(word)
    return len(res)
print(count_unique_words2("cat dog cat bird house dog"))

print("6.--------------------------")
# 6. Слово з найбільшою кількістю повторень. Поверни одне слово з найбільшою частотою. Без max().
# Якщо кілька слів мають однакову максимальну частоту, повертай те, яке раніше з'явилося в тексті.
def count_unique_words(text):
    words = text.split()
    w_dict = {}
    for word in words:
        w_dict[word] = w_dict.get(word, 0)+1
    max_freq = 0
    for key, value in w_dict.items():
        if value > max_freq:
            max_freq = value
    for word in words:
        if w_dict[word] == max_freq:
            return word
print(count_unique_words("cat dog cat bird dog cat"))

#OR
def count_unique_words2(text):
    words = text.split()
    freq_dict = {}
    for word in words:
        clean_word = word.lower().strip(".,!?:;")
        freq_dict[clean_word] = freq_dict.get(clean_word, 0) +1
    max_freq_word = ""
    max_count = 0
    for word in words:
        clean_word = word.lower().strip(".,!?:;")
        count = freq_dict[clean_word]
        if count > max_count:
            max_count = count
            max_freq_word = clean_word
    return max_freq_word
print(count_unique_words2("cat dog cat bird dog cat"))


print("7.-----------------------------------------")
# Слова з однаковою частотою
# Поверни всі слова, які зустрічаються рівно n разів.
def words_with_frequency(text, n): 
    words = text.split()
    freq_dict = {}
    res = []
    for word in words:
        clean_word = word.lower().strip(".,!?:;")
        freq_dict[clean_word] = freq_dict.get(clean_word, 0)+1
    for key,value in freq_dict.items():
        if value == n:
            res.append(key)
    return res
print(words_with_frequency("cat dog cat bird bird dog house cat", 2))

print("8.-----------------------------------------")
# Знайди максимальну частоту, а потім поверни перше слово, яке має цю частоту.
def first_word_with_max_frequency(text):
    words = text.split()
    freq_words = {}
    for word in words:
        freq_words[word] = freq_words.get(word, 0)+1
    max_freq = 0
    for key, value in freq_words.items():
        if value > max_freq:
            max_freq = value
    for word in words:
        if freq_words[word] == max_freq:
            return word
print(first_word_with_max_frequency("dog cat bird cat dog"))

print("9.---------------------------------------------")
# Найкоротше унікальне слово. Слово повинно зустрічатися рівно один раз.
# Без min().
def shortest_unique_word(text):
    words = text.split()
    all_words = []
    repeated = []
    uniq = []
    for word in words:
        if word in all_words:
            repeated.append(word)
        all_words.append(word)
    print(all_words)
    print(repeated)
    for word in words:
        if word not in repeated:
            uniq.append(word)
    min_len = float("inf")
    min_word = ""
    print(uniq)
    for word in uniq:
        if len(word) < min_len:
            min_len = len(word)
            min_word = word
    return min_word
print(shortest_unique_word("apple cat dog apple house"))