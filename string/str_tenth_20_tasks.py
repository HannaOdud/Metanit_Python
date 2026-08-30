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
