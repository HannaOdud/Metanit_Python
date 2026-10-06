print("1. Найчастіша довжина → найбільша сума балів")
words = [
    "cat", "dog", "sun",
    "apple", "house",
    "car", "pen", "book",
    "python"
]

scores = {
    "cat": 50,
    "dog": 80,
    "sun": 40,
    "apple": 90,
    "house": 70,
    "car": 60,
    "pen": 30,
    "book": 85,
    "python": 95
}
#Знайди найчастішу довжину слова.
#Якщо кілька довжин зустрічаються однаково часто — вибери меншу довжину.
#Серед слів цієї довжини знайди слово з найбільшим балом.
#Якщо бали однакові — вибери слово, яке алфавітно перше/
freq_len= {}
for word in words:
    length = len(word)
    freq_len[length] = freq_len.get(length, 0)+1
print("Частоти довжин слів: ",freq_len)
srt_len = sorted(freq_len.keys(), key=lambda item:(
    -freq_len[item],
    item
))
most_freq_len = srt_len[0]
print(most_freq_len)
target_words = [word for word in words if len(word) == most_freq_len ]
print(target_words)

res = sorted(target_words, key=lambda word:(
    -scores[word],
    word
))

print(res[0])
