#Level 3

print("1.--------------------------------------------")
# Найчастіше слово без max() Повертає слово, яке зустрічається найбільше разів.
def most_common_word(text):
    words = text.split()
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0)+1
    #return words_count
    max_common_word = ""
    max_common_count = 0
    for key,value in words_count.items():
        if value > max_common_count:
            max_common_count = value
            max_common_word = key
    return max_common_word
print(most_common_word("cat dog cat bird dog cat"))

print("2.--------------------------------------------")
# Усі слова з максимальною частотою
# Підказка: спочатку знайди максимальну частоту, потім зроби другий прохід.
def words_with_max_frequency(text):
    words = text.split()
    words_count = {}
    res = []
    for word in words:
        words_count[word] = words_count.get(word, 0)+1
    #return words_count
    max_common_count = 0
    for key,value in words_count.items():
        if value > max_common_count:
            max_common_count = value
    for key,value in words_count.items():
        if value == max_common_count:
            res.append(key)
    return res
print(words_with_max_frequency("cat dog cat bird dog"))

print("3.--------------------------------------------")
# Найдовше слово серед тих, що повторюються
# Тобто слово повинно зустрічатися мінімум двічі, а серед таких потрібно знайти найдовше.
def longest_repeated_word(text):
    words = text.split()
    words_count = {}
    res = []
    for word in words:
        words_count[word] = words_count.get(word, 0)+1
    #return words_count
    for key,value in words_count.items():
            if value >= 2:
                res.append(key)
    longest = max(res, key=len)
    return longest
print(longest_repeated_word("cat dog bird cat rabbit bird dog"))

#OR
def longest_repeated_word2(text):
    words = text.split()
    words_count = {}
    res = []
    for word in words:
        words_count[word] = words_count.get(word, 0)+1
    #return words_count
    for key,value in words_count.items():
            if value >= 2:
                res.append(key)
    longest = ""
    len_longest = 0
    for word in res:
        if len(word) > len_longest:
            len_longest = len(word)
            longest = word
    return longest
print(longest_repeated_word2("cat dog bird cat rabbit bird dog"))

#OR
def longest_repeated_word3(text):
    words = text.split()
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0)+1
    #return words_count
    longest = ""
    for key,value in words_count.items():
            if value >= 2 and len(key) > len(longest):
                longest = key   
    return longest
print(longest_repeated_word3("cat dog bird cat rabbit bird dog"))


print("4.---------------------------------------------------")
# Коротше за середнє. Повертає список слів, довжина яких менша за середню довжину всіх слів.
def shorter_than_average(text): 
    words = text.split()
    sum_len = 0
    for word in words:
        sum_len += len(word)
    avg = sum_len /len(words)
    res = []
    for word in words:
        if len(word) < avg:
            res.append(word)
    return res
print(shorter_than_average("cat dog bird cat rabbit bird dog"))     