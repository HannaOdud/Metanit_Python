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

avg_scores = { length:sum(scores)/len(scores) for length, scores in length_scores.items()}
print("Avg scores: ",avg_scores)

srt = sorted(avg_scores.keys(), key=lambda item: (
    -avg_scores[item], item
))
print("Sorting ", srt)

len_with_max_avg_scores = srt[0]
print("len_with_max_avg_scores: ",len_with_max_avg_scores)

all_words = [word for word in words if len(word) == len_with_max_avg_scores ]
print(all_words)

res = sorted(all_words)
print(res)


print("6.Найчастіша довжина → найбільша сума унікальних символів ")
words = [
    "apple", "house", "plant",
    "dog", "book", "cat",
    "python", "java", "code"
]
#Знайди найчастішу довжину.
#Якщо нічия — меншу довжину.
#Для кожного слова вибраної довжини порахуй кількість унікальних символів.
#Після цього знайди слово, у якого:
# найбільша кількість унікальних символів;
# при нічиї — найбільша довжина без повторень;
# при повній нічиї — алфавітно перше.

len_freq = {}
for word in words:
    length = len(word)
    len_freq[length] = len_freq.get(length, 0)+1
print("Len_freq",len_freq)

srt = sorted(len_freq.keys(), key=lambda item: (
    -len_freq[item], item
))
print("sorted len freq", srt)
most_freq_len = srt[0]
print(most_freq_len)

all_words = [word for word in words if len(word)==most_freq_len]
print("All words with most freq len: ",all_words)

print("7.--Найчастіша довжина → найчастіша остання літера → найдовше слово- ")
words = [
    "cat", "boat", "dog",
    "apple", "house", "car",
    "table", "code", "phone",
    "tree", "book"
]
# Знайди найчастішу довжину.
# При нічиїй вибери меншу довжину.
# Залиш слова цієї довжини.
# Серед них знайди найчастішу останню літеру.
# При нічиїй вибери алфавітно меншу літеру.
# Залиш слова з цією останньою літерою.
# Вибери найдовше слово.
# Якщо довжина однакова — алфавітно перше.
len_freq = {}
for word in words:
    length = len(word)
    len_freq[length] = len_freq.get(length, 0)+1
print("Len_freq",len_freq)
srt = sorted(len_freq.keys(), key=lambda item: (
    -len_freq[item], item
))
print("sorted len freq", srt)
most_freq_len = srt[0]
print(most_freq_len)
all_words = [word for word in words if len(word)==most_freq_len]
print("All words with most freq len: ",all_words)

char_freq = {}
for word in all_words:
    last = word[-1]
    char_freq[last] = char_freq.get(last, 0)+1
print("Last char freq: ",char_freq)
srt2 = sorted(char_freq.keys(), key=lambda item:(-char_freq[item],item))
most_freq_last_char = srt2[0]
print(most_freq_last_char)
target_words = [word for word in all_words if word[-1] == most_freq_last_char]
print("All words with most freq last char: ", target_words)

res = sorted(target_words, key=lambda item: (-len(item), item))
print("Result:",res[0]) 

print("8.-Друге найбільше число → серед повторюваних чисел-")
numbers = [
    10, 5, 7, 10,
    3, 8, 7, 12,
    5, 12, 9, 8,
    12, 7
]
# Знайди друге найбільше різне число, яке зустрічається мінімум двічі.
# Результатом має бути друге найбільше число серед чисел, які повторюються.
freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0)+1
print("Freq: ", freq)

evens = [key for key,value in freq.items() if value >=2]
print("All even num: ", evens)

sort = sorted(evens, reverse=True)
second = sort[1]

print("Sorted evens num: ",sort)
print("Second:", second)


print("9.------------------------------------------------------")
# Найкращий студент — 4 критерії
students = {
    "Anna": [90, 80, 90, 100],
    "John": [95, 85, 90, 80],
    "Mike": [90, 90, 90, 90],
    "Kate": [100, 70, 100, 80],
    "Lisa": [90, 90, 80, 90]
}
# Для кожного студента знайди:
#середній бал;
#кількість оцінок 90+;
#кількість різних оцінок.
#Визнач найкращого студента за такими критеріями в такому порядку:
#більший середній бал;
#якщо нічия — більше оцінок 90+;
#якщо нічия — більше різних оцінок;
#якщо все ще нічия — ім'я алфавітно перше.
#Виведи ім'я переможця.

avg = {key:sum(value)/len(value) for key,value in students.items()}
print(avg)
count_high_marks = {key:sum(1 for mark in value if mark >= 90) for key,value in students.items()}
count_high_marks2 = {
    key: len([mark for mark in value if mark >= 90]) 
    for key, value in students.items()}

print(count_high_marks)
print(count_high_marks2)
uniq_mark = { key: len(set(value)) for key,value in students.items()}
print(uniq_mark)

srt = sorted(students.keys(), key=lambda item:(
    -avg[item],
    -count_high_marks[item],
    -uniq_mark[item],
    item

))
res = srt[0]
print("ім'я переможця: ", res)


print("10.----------------------------------------------------")
# Велика комбінована задача
words = [
    "cat", "car", "code",
    "dog", "door",
    "apple", "ant", "area",
    "python", "pen",
    "book", "boat"
]
#Потрібно знайти одне слово за таким алгоритмом:
#Знайди найчастішу довжину.
#При нічиїй — менша довжина.
#Залиш слова цієї довжини.
#Серед них знайди найчастішу першу літеру.
#При нічиїй — алфавітно менша літера.
#Залиш слова з цією першою літерою.

#Серед них знайди слово з найбільшою кількістю унікальних символів.
#При нічиїй — слово з найбільшою кількістю голосних.
#При повній нічиї — алфавітно перше слово.
#Виведи тільки фінальне слово.
len_freq = {}
for word in words:
    length = len(word)
    len_freq[length] = len_freq.get(length, 0)+1
print("Len_freq: ",len_freq)
srt = sorted(len_freq.keys(), key=lambda item: (
    -len_freq[item], item
))
print("sorted len freq", srt)
most_freq_len = srt[0]
print("Most freq len: ",most_freq_len)
all_words = [word for word in words if len(word)==most_freq_len]
print("All words with most freq len: ",all_words)

char_freq = {}
for word in all_words:
    first = word[0]
    char_freq[first] = char_freq.get(first, 0)+1
print("First letter freq: ",char_freq)
srt2 = sorted(char_freq.keys(), key=lambda item:(-char_freq[item],item))
most_freq_last_char = srt2[0]
print(most_freq_last_char)
target_words = [word for word in all_words if word[0] == most_freq_last_char]
print("All words with most freq last char: ", target_words)