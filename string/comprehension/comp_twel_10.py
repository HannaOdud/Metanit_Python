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