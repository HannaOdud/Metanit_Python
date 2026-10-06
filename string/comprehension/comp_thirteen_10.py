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

print("3.Найчастіше число → перше число, яке зустрічається повторно ")
# Знайди число, яке зустрічається найчастіше.
# Якщо кілька чисел мають однакову максимальну частоту — вибери менше число.
# Після цього серед усіх чисел, які зустрічаються стільки ж разів, скільки й 
# максимальна частота, знайди те, яке першим з'являється в оригінальному списку.
numbers = [
    5, 2, 7, 5, 3,
    2, 8, 2, 7, 9,
    5, 4, 7
]
num_freq = {}
for num in numbers:
    num_freq[num] = num_freq.get(num,0)+1
print("Частоти num",num_freq)

srt = sorted(num_freq.keys(), key=lambda item:(
    -num_freq[item], item
))
print("ВІдсортовані за частотою та значенням - ",srt)
most_freq_num_value = max(num_freq.values())
print("Максимальна частота: ",most_freq_num_value)

all_most_nums = [key for key,value in num_freq.items() if most_freq_num_value == value ]
print("Усі числа з максимальною частотою: ",all_most_nums)

srt2 = sorted(all_most_nums, key=lambda item:(numbers.index(item)))
first_in_numbers = srt2[0]
print("Перше в оригінальному списку",first_in_numbers)

print("4.---Найчастіша довжина → найчастіше слово → алфавітний tie-break")
words = [
    "cat", "dog", "cat",
    "sun", "dog", "car",
    "apple", "dog",
    "sun", "car",
    "cat"
]
#Знайди найчастішу довжину слова.
#Якщо нічия — вибери меншу довжину.
#Залиш тільки слова цієї довжини.
#Серед них знайди найчастіше слово.
#Якщо кілька слів мають однакову частоту — вибери алфавітно перше.
len_freq = {}
for word in words:
    length = len(word)
    len_freq[length] = len_freq.get(length, 0)+1
print("Частоти довжин слова: ",len_freq)

srt = sorted(len_freq.keys(), key=lambda item: (
    -len_freq[item], item
))
most_freq = srt[0]
print("Найчастіша довжина слова: ",most_freq)

all_most_freq_len_words = [word for word in words if len(word) == most_freq]
print("Всі слова з цієї довжини",all_most_freq_len_words)

freq_word ={}
for word in words:
    freq_word[word] = freq_word.get(word, 0)+1
print("Частоти слів: ",freq_word)

srt2 = sorted(freq_word.keys(), key=lambda item:(
    -freq_word[item], item
))
most_freq_len = srt[0]
print("Найчастіша довжина слова: ",most_freq_len)
all_words = [key for key,value in freq_word.items() if most_freq_len== value]

print("All words: ",all_words)

srt2 = sorted(all_words, key=lambda item: (
    -freq_word[item], item
))
res = srt2[0]
print(res)

print("5.----Групування за довжиною → найбільша група → середній бал")
words = [
    "cat", "dog", "sun",
    "apple", "house",
    "book", "tree",
    "python", "java"
]

scores = {
    "cat": 70,
    "dog": 90,
    "sun": 80,
    "apple": 100,
    "house": 60,
    "book": 80,
    "tree": 90,
    "python": 70,
    "java": 100
}
# Для кожної довжини знайди середній бал слів цієї довжини.
# потім: 
# Знайди довжину, у якої найбільший середній бал.
# Якщо середні бали однакові — вибери меншу довжину.
# Виведи всі слова цієї довжини в алфавітному порядку
length_scores = {}
for word in words:
    length = len(word)
    score = scores[word]
    length_scores[length] = length_scores.get(length, [])+ [score]
print("Групування балів: ",length_scores)