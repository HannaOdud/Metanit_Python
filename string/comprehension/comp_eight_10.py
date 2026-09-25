print("1.----------------------------------------------")
# Перший елемент, який зустрічається рівно двічі
numbers = [ 4, 7, 2, 9, 7, 5, 2, 8, 4, 9]
freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0)+1
for num in numbers:
    if freq[num] == 2:
        print(num)
        break

print("2.--------------------------------------------")
words = [
    "apple",
    "house",
    "python",
    "banana",
    "world",
    "programming",
    "cat"
]
res = sorted(words)
max_w = ""
max_len = 0
for word in res:
    if len(word) > max_len and len(set(word)) == len(word):
       max_len = len(word)
       max_w = word
print(max_w) 

#solution 2
uniq_char_words = [word for word in words if len(word)==len(set(word))]
print(uniq_char_words)
longest = max(uniq_char_words, key=lambda word: (len(word), word))
print(longest)


print("3.-------------------------------------------------------")
# Друге найбільше число, яке зустрічається більше одного разу
numbers = [10, 5, 7, 10, 3, 7, 8, 8, 12, 12, 5]
checked = set()
repeated = set()
for num in numbers:
    if num in checked:
        repeated.add(num)
    checked.add(num)
print(repeated)
res = sorted(repeated, reverse=True)
print(res[1])

#solution 2
res = sorted({num for num in numbers if numbers.count(num) > 1}, reverse=True)
print(res[1])

print("4.----------------------------------------------------")
# Групування слів за довжиною + найбільша група
words = [
    "cat",
    "dog",
    "apple",
    "book",
    "python",
    "code",
    "house",
    "sun"
]
# Згрупуй слова за довжиною.
len_words = {}
for word in words:
    length = len(word)
    if length in len_words:
        len_words[length].append(word)
    else:
        len_words[length] = [word]
print("Згруповані слова:",len_words)

# Знайди довжину, для якої є найбільше слів.
max_list_len = 0
for key,value in len_words.items():
    if len(value) > max_list_len:
        max_list_len = len(value)
print(max_list_len)

# Якщо кілька довжин мають однакову кількість слів — вибери меншу довжину.
res = sorted(len_words.items(), key=lambda item: (-len(item[1]), item[0]) )
print(res[0][1])


print("5.-----------------------------------------------------------")
words = [
    "apple",
    "python",
    "banana",
    "house",
    "developer",
    "algorithm"
]
longest_w = [word for word in words if len(word) == len(max(words, key=len))]
print(longest_w)

#Порахуй частоту літер у них.
freq_char = {}
for word in longest_w:
    for char in word:
        l_char = char.lower()
        freq_char[l_char] = freq_char.get(l_char, 0)+1
print("freq of all char in long.words: ", freq_char)

#Знайди найчастішу літеру
max_char = max(freq_char.items(), key=lambda item:(-item[1],item[0]))[0]
print("max_char:", max_char)

print("6.----------------------------------------------------------")
# Найкращий студент із трьома критеріями
students = {
    "Anna": [90, 80, 90, 100],
    "John": [95, 85, 90, 90],
    "Mike": [100, 90, 100, 80],
    "Kate": [90, 90, 90, 95],
    "Lisa": [95, 90, 95, 90]
}
avg = {key:sum(value)/len(value) for key,value in students.items()}
print(avg)

max_avg = max(avg.values())
print(max_avg)

best_sts = {}
for key, value in students.items():
    if avg[key] == max_avg:
        best_sts[key] = value
print(best_sts)

unq_srt = sorted(best_sts.items(), key=lambda item:(-len(set(item[1])), item[0]))
print(unq_srt[0][0])


print("7.--------------------------------------------------------------")
# Перше слово з другою за величиною частотою
words = [
    "python",
    "java",
    "python",
    "ruby",
    "java",
    "c++",
    "ruby",
    "go",
    "go",
    "go"
]
freq = {}
for word in words:
    freq[word] = freq.get(word,0)+1
print(freq)

uniq = sorted(set(freq.values()), reverse=True)
print(uniq)
print(uniq[1])
for word in words:
    if freq[word] == uniq[1]:
        print(word)
        break


print("8.--------------------------------------------------------")
# другий найдорожчий у категорії
products = {
    "laptop": ("electronics", 1200),
    "phone": ("electronics", 800),
    "tablet": ("electronics", 600),
    "keyboard": ("accessories", 70),
    "mouse": ("accessories", 50),
    "monitor": ("electronics", 300),
    "headphones": ("accessories", 100)
}
electronics = {}
for key,value in products.items():
    if value[0] == "electronics":
        electronics[key] = value[1]

print(electronics)
srt = sorted(electronics.items(), key=lambda item: -item[1] )
print(srt[1][0])

print("9.-------------------------------------------------------")
# Найчастіша довжина слова + алфавітний tie-break
words = [
    "cat",
    "dog",
    "sun",
    "apple",
    "house",
    "book",
    "python",
    "code",
    "car"
]

len_dict = {}
for word in words:
    if len(word) in len_dict:
        len_dict[len(word)].append(word)
    else:
        len_dict[len(word)] = [word]
print(len_dict)

max_len = sorted(len_dict.items(), key=lambda item: (-len(item[1]), item[0]))
print(max_len)

print("10.--------------------------------------------------------------")
# Text Analyzer
text = """Python is powerful and Python is popular.
Java is popular, but Python is easier.
JavaScript is powerful and JavaScript is popular.
Ruby is simple and Ruby is elegant.
Go is simple and fast.
"""
words = [text.word().strip(".,!?:;") for word in text.split()]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0)+1
print(freq)

#max_freq
max_freq = max(freq.values())
print(max_freq)
max_freq_list = []
for key,value in freq.items():
    if value == max_freq:
        max_freq_list.append(key)
print(max_freq_list)
srt_alf = sorted(max_freq_list)
print(srt_alf)

#first uniq word
for word in words:
    if freq[word] == 1:
        print(word)
        break

#first repeated word
checked = set()
for word in words:
    if word in checked:
        print(word)
        break
    checked.add(word)

# sec_high_uniq_freq
"""reversed_freq = {}
for key,value in freq.items():
    if value in reversed_freq:
        reversed_freq[value].append(key)
    else:
        reversed_freq[value] = [key]
print(reversed_freq)

uniq_freq_list = []
for key,value in reversed_freq.items():
    if len(value) == 1:
        uniq_freq_list.append(key)
print(uniq_freq_list)
sec_high_uniq_freq = sorted(uniq_freq_list, reverse=True)[1]
print(sec_high_uniq_freq)"""

unique_freq = sorted(set(freq.values()), reverse=True)
second_freq = unique_freq[1]

#first word with second uniq freq
unique_freq = sorted(set(freq.values()), reverse=True)
second_freq = unique_freq[1]

for word in words:
    if freq[word] == second_freq:
        print(word)
        break

#word_len
"""word_len = {}
for word in words:
    if freq[word] > 1:
        word_len[word] = len(word)
print(word_len)"""

word_len = {
    word: len(word)
    for word in freq
    if freq[word] >= 2
}

#1.частота ↓2. довжина ↓3. алфавіт ↑
uniq_words = []
for word in words:
    if freq[word] == 1:
        uniq_words.append(word)
print(uniq_words)
sort_uniq_words = sorted(uniq_words, key = lambda item: (-freq[item],-len(item),item))
print(sort_uniq_words)

#max_len_uniq_word
max_len_uniq_word = max(uniq_words, key=len)
print(max_len_uniq_word)