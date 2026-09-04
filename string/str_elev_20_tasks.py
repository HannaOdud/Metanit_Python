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