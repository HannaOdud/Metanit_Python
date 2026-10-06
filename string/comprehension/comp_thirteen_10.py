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

print("2.------Найчастіша перша літера → найбільша кількість унікальних символів")

#Знайди літеру, з якої починається найбільша кількість слів.
#Якщо таких літер декілька — вибери алфавітно меншу.
#Серед слів, які починаються з цієї літери, знайди слово з найбільшою кількістю унікальних символів.
#Якщо нічия — алфавітно перше слово.

words = [
    "apple", "animal", "ant",
    "area", "book", "banana",
    "car", "code", "cat",
    "python"
]
char_freq = {}
for word in words:
    first_char = word[0]
    char_freq[first_char] = char_freq.get(first_char,0)+1
print(char_freq)

srt = sorted(char_freq.keys(), key=lambda item:(
    -char_freq[item],item
))
print("Sorted char",srt)
most_char = srt[0]
print("Most char: ",most_char)
target_words = [word for word in words if word[0] == most_char ]
print("target words", target_words)
srt2 = sorted(target_words, key=lambda word: (
    -len(set(word)), word
)) 
print("sorted2",srt2)
res = srt2[0]
print(res)