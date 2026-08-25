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
    for word in words:
        words_count[word] = words_count.get(word, 0)+1
    #return words_count
    first_common_word = ""
    second_common_word = ""
    max_common_count = 0
    for key,value in words_count.items():
        if value > max_common_count:
