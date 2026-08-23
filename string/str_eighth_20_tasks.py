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

print("4.---------------------------------------------")
# Друге найдовше слово
def second_longest_word(text):
    words = text.split()
    longest_word = ""
    sec_longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            sec_longest_word = longest_word
            longest_word = word
        elif len(word) > len(sec_longest_word): 
            sec_longest_word = word
    return sec_longest_word
print(second_longest_word("cat elephant dog programming apple"))
#
def second_longest_word2(text):
    words = text.split()
    second_largest = sorted(words, key = len)[-2]
    return second_largest
print(second_longest_word2("cat elephant dog programming apple"))

print("5.-----------------------------------------------")
# Друге найкоротше слово
def second_shortest_word(text):
    words = text.split()
    sec_shortest = sorted(words, key = len )[1]
    return sec_shortest
print(second_shortest_word("cat elephant dog programming apple"))
# 
def second_shortest_word2(text):
    words = text.split()
    shortest = words[0]
    sec_shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            sec_shortest = shortest
            shortest = word
        elif  len(word) < len(sec_shortest):
            sec_shortest = word
    return sec_shortest
print(second_shortest_word2("cat elephant dog programming apple"))

print("6.------------------------------------------------")
# Групування за першою літерою
def group_by_first_letter(text):
    words = text.split() 
    res = {}
    for word in words:
        if word[0] in res:
            res[word[0]].append(word)
        else:
            res[word[0]] = [word]
    return res
print(group_by_first_letter("Apple Ant Banana Ball Cat"))

print("7.----------------------------------------------")
# Групування за довжиною
def group_by_length(text):
    words = text.split()
    res = {}
    
    for word in words:
        if len(word) in res:
            res[len(word)].append(word)
        else:
            res[len(word)] = [word]
    return res
print(group_by_length("I cat dog elephant"))

print("8.--------------------------------------------")
# Найдовше слово в кожній групі Без max().
def longest_by_first_letter(text):
    words = text.split()
    res = {}
    for word in words:
        if word[0] in res:
            res[word[0]].append(word)
        else:
            res[word[0]] = [word]
    res2= {}
    for key,value in res.items():
        res2[key] = max(value, key=len )
    return res2 
print(longest_by_first_letter("Apple Ant Amazing Ball Book Cat"))

#
def longest_by_first_letter2(text):
    words = text.split()
    res = {}
    for word in words:
        if word[0] in res and len(word) > len(res[word[0]]):
            res[word[0]] = word
        else:
            res[word[0]] = word
   
    return res
print(longest_by_first_letter2("Apple Ant Amazing Ball Book Cat"))



print("9.---------------------------------------------")
# Слова з найбільшою кількістю голосних
def words_with_max_vowels(text):
    words = text.split()
    vows = ["a","e","i","o","u"]
    max_count = 0
    for word in words:
        count = 0
        for char in word:
            if char in vows:
                count += 1
        if count > max_count:
            max_count = count
    res = []
    for word in words:
        count = 0
        for char in word:
            if char in vows:
                count += 1
        if count == max_count:
            res.append(word)
    return res
print(words_with_max_vowels("cat apple idea banana"))


