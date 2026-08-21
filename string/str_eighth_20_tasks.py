print("1.-----------------------------------------------")
# Частота слів
def word_frequency(text):
    words = text.split()
    res ={}
    for word in words:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res
print(word_frequency("cat dog cat bird dog dog"))
#
def word_frequency2(text):
    words = text.split()
    res ={}
    for word in words:
        res[word] = res.get(word, 0)+1
    return res
print(word_frequency2("cat dog cat bird dog dog"))

print("2.-----------------------------------------------")
# Найчастіше слово Без max().
def most_common_word(text):
    words = text.split()
    res ={}
    for word in words:
        res[word] = res.get(word, 0)+1
    result = max(res, key=res.get) 
    return result
print(most_common_word("cat dog cat bird dog dog"))
#
def most_common_word2(text):
    words = text.split()
    res ={}
    for word in words:
        res[word] = res.get(word, 0)+1
    result = sorted(res, key=res.get, reverse=True)[0]
    return result
print(most_common_word2("cat dog cat bird dog dog"))
#
def most_common_word3(text):
    words = text.split()
    res ={}
    for word in words:
        res[word] = res.get(word, 0)+1
    max_key = None
    max_value = float("-inf")
    for key, value in res.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
print(most_common_word3("cat dog cat bird dog dog"))
#
def most_common_word4(text):
    res = word_frequency(text)
    max_key = None
    max_value = float("-inf")
    for key, value in res.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
print(most_common_word4("cat dog cat bird dog dog"))

print("3.----------------------------------------------")
# Слова, які зустрічаються один раз
def unique_occurrence_words(text):
    words = text.split()
    all_dict = {}
    for word in words:
        if word in all_dict:
        # all_dict[word] = all_dict.get(word, 0)+1
            all_dict[word] += 1
        else:
            all_dict[word] = 1
    result = []
    for key,value in all_dict.items():
        if value == 1:
            result.append(key)
    return result
print(unique_occurrence_words("cat dog cat bird dog fish"))