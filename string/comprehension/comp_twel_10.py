print("1. Найчастіша довжина → перше слово")
#Знайди довжину слова, яка зустрічається найчастіше.
#Якщо кілька довжин мають однакову частоту → вибери меншу довжину.
#Після цього серед слів цієї довжини знайди перше слово за алфавітом.
words = [
    "sun", "apple", "dog", "house",
    "cat", "book", "car", "python", "pen"
]
freq = {}
for word in words:
    freq[len(word)] = freq.get(len(word), 0)+1

srt_len = sorted(freq, key=lambda item:(
    -freq[item],
    item
))
most_freq_len = srt_len[0]

words_with_most_freq_len = []
for word in words:
    if len(word)== most_freq_len:
        words_with_most_freq_len.append(word)
print(words_with_most_freq_len)

words_with_most_freq_len2 = [word for word in words if len(word) == most_freq_len]
print(words_with_most_freq_len2)

first_alf = sorted(words_with_most_freq_len2)[0]
print(first_alf)

print("2.Найчастіша кількість літер → найдовше слово")
# Знайди довжину, яка зустрічається найчастіше.
# Якщо нічия → менша довжина.
# Серед слів цієї довжини знайди найдовше.
words = [
    "red", "blue", "green", "cat",
    "dog", "house", "tree", "apple",
    "sun", "car"
]
freq = {}
for word in words:
    if len(word) in freq:
        freq[len(word)].append(word)
    else:
        freq[len(word)] = [word]
print(freq)

srt = sorted(freq.keys(), key=lambda item: (
    -len(freq[item]),
    item)
)
print(srt)
most_srt = srt[0]
print(most_srt)
words_with_srt_len = [word for word in words if len(word) == most_srt]
print(words_with_srt_len)

longest = max(words_with_srt_len, key=len)
print(longest)


print("3. Найчастіша перша літера → найдовше слово ")
#Згрупуй слова за першою літерою.
#Знайди літеру, яка має найбільшу групу.
#Якщо кілька груп однакового розміру → менша літера.
#Серед слів цієї групи знайди найдовше слово.
#Якщо довжина однакова → алфавітно перше. 

words = [
    "apple", "animal", "ant",
    "book", "banana",
    "cat", "car", "code",
    "python"
]
group = {}
for word in words:
    first_letter = word[0]
    if first_letter in group:
        group[first_letter].append(word)
    else:
        group[first_letter]=[word]
print(group)

srt = sorted(group.keys(), key=lambda item:(
    -len(group[item]), 
    item
))
print(srt)
srt_char = srt[0]
print(srt_char)

all_words = [word for word in words if word[0] == srt_char]
print(all_words)

first_alph_word = sorted(all_words, key=lambda word: (-len(word),word))
print(first_alph_word[0])

print("4.Найчастіша остання літера → алфавітно перше слово ")
# Знайди останню літеру, яка зустрічається у найбільшої кількості слів.
# Якщо нічия → вибери алфавітно меншу літеру.
# Відбери слова, які закінчуються на цю літеру.
# Серед них знайди перше слово за алфавітом.
group = {}
for word in words:
    last_char = word[-1]
    if last_char in group:
        group[last_char].append(word)
    else:
        group[last_char] = [word]
print(group)
srt_last_chars = sorted(group, key=lambda item:(
    -len(group[item]),
    item
    ))
print(srt_last_chars)
last_char = srt_last_chars[0]
print(last_char)
all_words_with_last_char = [word for word in words if word[-1]==last_char]
print(all_words_with_last_char)
res = sorted(all_words_with_last_char)
print(res[0])


print("5. Найчастіша довжина → найдовше слово?")
#довжину, яка зустрічається найчастіше;
#якщо нічия → меншу довжину;
#усі слова цієї довжини;
#слово, яке має найбільшу кількість голосних літер;
#якщо нічия → алфавітно перше.
#Тут уже буде три рівні аналізу.
words = [
    "cat", "dog", "sun",
    "apple", "house",
    "book", "code",
    "python", "java"
]
freq = {}
for word in words:
    length = len(word)
    if length in freq:
        freq[length].append(word)
    else:
        freq[length] = [word]
print(freq)
srt_length = sorted(freq, key=lambda item: (
    -len(freq[item]),
    #len(item)
    item
))
print(srt_length)
most_freq_len = srt_length[0]
print(most_freq_len)

all_most_freq_words = [word for word in words if len(word)==most_freq_len]
print(all_most_freq_words)

vows = ["a","e","i","o","u"]
max_vow = float("-inf")
max_vow_word = ""
for word in all_most_freq_words:
    count = 0
    for char in word:
        if char in vows:
            count += 1
    if max_vow < count:
        max_vow = count
        max_vow_word = word
print(max_vow_word)
all_vows_words = []
for word in all_most_freq_words:
    count = 0
    for char in word:
        if char in vows:
            count += 1
    if count == max_vow:
        all_vows_words.append(word)
res = sorted(all_vows_words)
print(res[0])


print("6.Найчастіша довжина → слово з найбільшою кількістю унікальних символів ")
#Знайди найчастішу довжину.
#При нічиї → менша довжина.
#Відбери слова цієї довжини.
#Знайди слово з найбільшою кількістю унікальних символів.
#Якщо нічия → алфавітно перше.

words = [
    "apple", "house", "plant",
    "dog", "book", "cat",
    "python", "java", "code"
]
freq = {}
for word in words:
    length = len(word)
    if length in freq:
        freq[length].append(word)
    else:
        freq[length] = [word]
print(freq)
srt_length = sorted(freq, key=lambda item: (
    -len(freq[item]),
    #len(item)
    item
))
print(srt_length)
most_freq_len = srt_length[0]
print(most_freq_len)

all_most_freq_words = [word for word in words if len(word)==most_freq_len]
print(all_most_freq_words)


max_uniq_word = ""
max_uniq_len = 0
for word in all_most_freq_words:
    if len(set(word)) > max_uniq_len:
        max_uniq_len = len(set(word))
        max_uniq_word = word
print(max_uniq_word)
all_uniq_words = []
for word in words:
    if len(set(word)) == max_uniq_len:
        all_uniq_words.append(word)
print("з найбільшою кількістю унікальних символів: ", all_uniq_words[0])
    #OR
res = sorted(all_most_freq_words, key=lambda item: (
    -len(set(item)),
    item
))
print("з найбільшою кількістю унікальних символів:", res[0] )

print("7. Найчастіша довжина → перше слово в оригінальному порядку")
#Знайди найчастішу довжину.
#При нічиї → менша довжина.
#Відбери слова цієї довжини.
#Не сортуй їх.
#Виведи перше таке слово, яке зустрічається в оригінальному списку.
words = [
    "python", "cat", "dog",
    "apple", "sun", "book",
    "house", "car", "pen"
]
freq = {}
for word in words:
    length = len(word)
    if length in freq:
        freq[length].append(word)
    else:
        freq[length] = [word]
print(freq)
srt_len = sorted(freq, key=lambda item:(
    -len(freq[item]),
    item
))
most_length = srt_len[0]
print(most_length)

all_most_freq_len = [word for word in words if len(word)==most_length]
print(all_most_freq_len)
for word in words:
    if word in all_most_freq_len:
        print(word)
        break

print("8. Найчастіша довжина → найбільш часте слово")
# Знайди довжину, яка зустрічається найчастіше.
# При нічиї → менша довжина.
# Залиш тільки слова цієї довжини.
# Серед них знайди слово з найбільшою власною частотою.
# При однаковій частоті → алфавітно перше.
# Тут потрібно буде використовувати два різні види частот:
#    -частота довжин;
#    -частота самих слів.
words = [
    "cat", "dog", "cat",
    "apple", "dog",
    "sun", "cat",
    "house", "sun"
]
freq = {}
for word in words:
    length = len(word)
    if length in freq:
        freq[length].append(word)
    else:
        freq[length] = [word]
print(freq)
srt_len = sorted(freq, key=lambda item:(
    -len(freq[item]),
    item
))
most_length = srt_len[0]
print(most_length)
all_most_freq_words = [word for word in words if len(word)==most_length]
print(all_most_freq_words)

word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
print(word_freq)   

res = sorted(all_most_freq_words, key=lambda item:(
    -word_freq[item],
    item
))
print(res[0])
