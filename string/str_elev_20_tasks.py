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

#OR
def shortest_unique_word(text):
    words = text.split()
    freq_words = {}
    for word in words:
        clean_word = word.lower().strip(".,!?:;")
        freq_words[clean_word] = freq_words.get(clean_word, 0)+1
    min_len = float("inf")
    min_word = ""
    for word in words:
        clean_word = word.lower().strip(".,!?:;")
        if freq_words[clean_word] == 1:
            if len(clean_word) < min_len:
                min_len = len(clean_word)
                min_word = clean_word
    return min_word
print(shortest_unique_word("apple cat dog apple house"))

print("10.--------------------------------------------------")
# Найдовше слово, яке повторюється
# Слово повинно зустрічатися хоча б двічі. Без max().
def longest_repeated_word(text):
    words = text.split()
    freq_word = {}
    for word in words:
        clean_word = word.lower().strip(".,!?:;")
        freq_word[clean_word] = freq_word.get(clean_word, 0)+1
    longest_len = float("-inf")
    longest_word = ""
    res = []
    for key,value in freq_word.items():
        if freq_word[clean_word] >= 2:
            res.append(clean_word)
    longest_len = float("-inf")
    longest_word = ""
    for word in res:
        if len(clean_word)>longest_len:
            longest_len = len(clean_word)
            longest_word = clean_word
    return longest_word
print(longest_repeated_word("cat elephant cat house elephant"))
#OR
def longest_repeated_word2(text):
    words = text.split()
    freq_word = {}
    for word in words:
        clean_word = word.lower().strip(".,!?:;")
        freq_word[clean_word] = freq_word.get(clean_word, 0)+1
    longest_len = float("-inf")
    longest_word = ""
    for key,value in freq_word.items():
        if freq_word[clean_word] >= 2:
            if len(clean_word) > longest_len:
                longest_len = len(clean_word)
                longest_word = clean_word
    return longest_word      
print(longest_repeated_word2("cat elephant cat house elephant"))


print("11.------------------------------------------")
# Статистика слів
def word_statistics(text):
    words = text.split()
    #uniq_words
    checked = []
    repeated = []
    uniques = []
    for word in words:
        if word in checked:
            repeated.append(word)
        checked.append(word)
    for word in words:
        if word not in repeated:
            uniques.append(word)
 
    res = {
        "total_words": len(words),
        "unique_words": len(uniques),
        "repeated_words": len(repeated),
    }
    return res
print(word_statistics("cat dog cat bird dog house"))

print("12.--------------------------------------")
# Аналіз найчастішого слова
def most_frequent_word_info(text):
    words = text.split()
    freq_words = {}
    for word in words:
        clean_word = word.lower().strip(".,!?:;")
        freq_words[clean_word] = freq_words.get(clean_word, 0)+1
    max_freq_count = 0
    max_freq_word = ""
    for key,value in freq_words.items():
        if value > max_freq_count:
            max_freq_count = value
            max_freq_word = key
    res = {
        "word": max_freq_word,
        "count": max_freq_count,
        "length": len(max_freq_word)
    }
    return res
print(most_frequent_word_info("cat dog cat bird cat"))

print("13.----------------------------------------")
# Аналіз унікальних слів
# Розглядати тільки слова, які зустрічаються рівно один раз. Без min() і max().
def unique_words_info(text):
    words = text.split()
    freq_words = {}
    for word in words:
        clean_word = word.lower().strip(".,!?:;")
        freq_words[clean_word] = freq_words.get(clean_word, 0)+1
    max_freq_count = 0
    for key,value in freq_words.items():
        if value > max_freq_count:
            max_freq_count = value
    uniques = []
    for key,value in freq_words.items():
        if value == 1:
            uniques.append(key)
    max_unique_word = ""
    max_unique_len = float("-inf")
    for word in uniques:
        if len(word) > max_unique_len:
            max_unique_len = len(word)
            max_unique_word = word
    min_unique_word = ""
    min_unique_len = float("inf")
    for word in uniques:
        if len(word) < min_unique_len:
            min_unique_len = len(word)
            min_unique_word = word
    res = {
        "count": max_freq_count,
        "longest": max_unique_word,
        "shortest": min_unique_word
    }
    return res
print(unique_words_info("cat dog cat elephant house dog"))

print("14.----------------------------------------")
# Перші унікальні символи кожного слова
# Поверни всі слова, перша літера яких зустрічається як перша літера тільки одного слова.
def words_with_unique_first_letter(text):
    words = text.split()
    char_freq_dict = {}
    for word in words:
        char_freq_dict[word[0]] = char_freq_dict.get(word[0], 0)+1
    res = []
    for key,value in char_freq_dict.items():
        if value == 1:
            res.append(key)
    result = []
    for word in words:
        if word[0] in res:
            result.append(word)
    return result        
print(words_with_unique_first_letter("apple ant ball cat banana"))

print("15.--------------------------------------")
# Перше слово з унікальною довжиною
# Знайди довжини слів, які зустрічаються тільки один раз, і поверни перше слово з такою довжиною.
def first_unique_length_word(text):
    words = text.split()
    len_freq_dict = {}
    for word in words:
        if len(word) in len_freq_dict:
            len_freq_dict[len(word)].append(word)
        else:
            len_freq_dict[len(word)] = [word] 
    #print(len_freq_dict)
    for key,value in len_freq_dict.items():
        if len(value) == 1:
            return value[0]
print(first_unique_length_word("cat house dog elephant sun"))  

print("16.-------------------------------------")
# Слово з найбільшою кількістю голосних серед унікальних
# Розглядай тільки слова, які зустрічаються один раз
# Серед них знайди слово з найбільшою кількістю голосних.
def unique_word_with_most_vowels(text):
    words = text.split()
    freq_word = {}
    for word in words:
        freq_word[word] = freq_word.get(word, 0)+1
    print(freq_word)
    uniques = []
    for key,value in freq_word.items():
        if value == 1:
            uniques.append(key)
    max_vows = 0
    vows = ["a","e","i","o","u"]
    for word in uniques:
        count = sum(1 for char in word.lower() if char in vows)
        if count > max_vows:
            max_vows = count
    for word in uniques:
        count = sum(1 for char in word.lower() if char in vows)
        if count == max_vows:
            return word
print(unique_word_with_most_vowels("cat house cat elephant bird")) 

print("17.----------------------------------------")
# Усі повторювані слова з максимальною довжиною
# Знайди максимальну довжину серед повторюваних слів і поверни всі такі слова.
def longest_repeated_words(text):
    words = text.split()
    freq_words = {}
    for word in words:
        freq_words[word] = freq_words.get(word, 0)+1
    repeated = []
    for key, value in freq_words.items():
        if value >= 2:
            repeated.append(key)
    return max(repeated, key=len)
print(longest_repeated_words("cat elephant dog elephant house dog"))


print("18.----------------------------------------")
# Аналіз першої та останньої літери
def first_last_statistics(text):
    words = text.split()
#most_common_first
    freq_first_char = {}
    for word in words:
        if word[0] in freq_first_char:
            freq_first_char[word[0]] += 1
        else:
            freq_first_char[word[0]] = 1
    print(freq_first_char)
    most_common_first_char = ""
    most_common_count = 0
    for key,value in freq_first_char.items():
        if value > most_common_count:
            most_common_count = value
            most_common_first_char = key
    print(most_common_first_char)
#most_common_last
    freq_last_char = {}
    for word in words:
        freq_last_char[word[-1]] = freq_last_char.get(word[-1], 0)+1
    print(freq_last_char)
    most_common_last_char = ""
    most_common__last_count = 0
    for key,value in freq_last_char.items():
        if value > most_common__last_count:
            most_common__last_count = value
            most_common_last_char = key
    print(most_common_last_char)
# unique_first_letters
    unique_first_char  = set()
    for word in words:
        first_char = word[0]
        unique_first_char.add(first_char)
# unique_last_char
    unique_last_char = set()
    for word in words:
        unique_last_char.add(word[-1])

    res = {
        "most_common_first": most_common_first_char,
        "most_common_last": most_common_last_char,
        "unique_first_letters": unique_first_char,
        "unique_last_letters": unique_last_char
    }
    return res
print(first_last_statistics("cat elephant elephant dog duck elephant house dog"))

print("19.----------------------------------------")
# Повний аналіз тексту
def analyze_text(text):
    words = text.split()
    #clean_word = word.lower().strip(".,!?:;")

#unique_word_count
    uwq = set(len(words))

#repeated_word_count
    for word in words:
        clean_word = word.lower().strip(".,!?:;")


    res = {
        "total_words": len(words),
        "unique_word_count": uwq,
        "repeated_word_count": ...,
        "first_unique_word": ...,
        "first_repeated_word": ...,
        "most_frequent_word": ...,
        "longest_unique_word": ...,
        "shortest_repeated_word": ...
    }
    return res
print(analyze_text("cat elephant elephant dog duck elephant house dog"))