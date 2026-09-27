print("1.-----------------------------------------------------------")
# Перше число, яке зустрічається найчастіше
# Знайди максимальну частоту серед чисел.
# Якщо кілька чисел мають однакову максимальну частоту — вибери перше з них в оригінальному списку.

numbers = [
    4, 7, 2, 4, 9, 7, 4, 2, 7, 7, 5, 2
]
freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0)+1
max_freq = max(freq.values())
print(max_freq)
for num in numbers:
    if freq[num] == max_freq:
        print(num)
        break

print("2.---------------------------------------------------------")
# Найдовше слово без повторюваних символів
# Знайди найдовше слово, у якому жодна літера не повторюється.
# Якщо кілька слів мають однакову довжину — вибери перше за алфавітом.

words = [
    "apple",
    "dog",
    "house",
    "lamp",
    "python",
    "world",
    "banana",
    "code"
]
max_len = 0
max_len_word = ""
for word in words:
    if len(word) > max_len and len(word) == len(set(word)):
        max_len = len(word)
        max_len_word = word
        max_len = len(word)
print(max_len_word)
print(max_len)

#solution 2
set_words = [word for word in words if len(word) == len(set(word))]
max_len_w = sorted(set_words, key=lambda item:(-len(item), item))[0]
print(max_len_w)

print("3.-------------------------------------------------------------")
# Друге найбільше число серед чисел, які зустрічаються непарну кількість разів

# частоту кожного числа;
# залиш тільки числа, які зустрічаються непарну кількість разів;
# серед них знайди друге найбільше унікальне число.
numbers = [
    10, 5, 7, 10, 5, 7, 7,
    8, 8, 8, 12, 12, 3
]
freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0)+1

odd_num = {num for num in freq if freq[num] % 2 == 1}
print(odd_num)
sorted_num = sorted(odd_num, reverse=True)
print(sorted_num)
print(sorted_num[1])

print("4.--------------------------------------------------------------")
#Згрупуй слова за першою літерою.
#Знайди групу, у якій найбільше слів.
#Якщо кілька груп мають однаковий розмір — вибери групу з алфавітно меншою першою літерою.
#Виведи саму групу слів.
words = [
    "apple",
    "algorithm",
    "animal",
    "banana",
    "book",
    "cat",
    "code",
    "car",
    "python"
]
group = {}
for word in words:
    if word[0] in group:
        group[word[0]].append(word)
    else:
        group[word[0]] = [word]
print(group)
max_words_gr = sorted(group.keys(), key=lambda item: (-len(group[item]), item))
print(max_words_gr)
best_letter = max_words_gr[0]
print(best_letter)
best_group = group[best_letter]
print(best_group)

print("5.----------------------------------------------------------------")

words = [
    "cat",
    "dog",
    "cat",
    "house",
    "book",
    "python",
    "dog",
    "code",
    "sun"
]
uniq_list = list(set(words))
print(uniq_list)

freq = {}
for word in uniq_list:
    if len(word) in freq:
        freq[len(word)] += 1
    else:
        freq[len(word)] = 1
print(freq)

max_freq_len = max(freq.values())
print(max_freq_len)

max_equal_freq = []
for key, value in freq.items():
    if value == max_freq_len:
        max_equal_freq.append(key)
print(max_equal_freq)

min_len = min(max_equal_freq)
print(min_len)


print("6.----------------------------------------------------------")
# Студент із найкращим результатом
# -найбільший середній бал;
# -якщо середні однакові → найбільша кількість оцінок 90+;
# -якщо і це однаково → найбільша кількість різних оцінок;
# -якщо все однаково → ім'я за алфавітом.
students = {
    "Anna": [90, 80, 90, 100, 90],
    "John": [95, 85, 90, 90, 95],
    "Mike": [100, 100, 90, 80, 100],
    "Kate": [90, 90, 90, 90, 90],
    "Lisa": [95, 95, 95, 90, 90]
}
avg = {key:sum(value)/len(value) for key,value in students.items()}
print(avg)
max_mark = max(avg.values())
print(max_mark)

res = sorted(students.keys(), 
             key = lambda item: (
                 -(sum(students[item])/len(students[item])),
                 -sum(1 for grade in students[item] if grade >= 90),
                 -len(set(students[item])),
                 item
             ))
print(res)

print("7.---------------------------------------------------------------------")
# Знайди найменшу частоту, яка зустрічається серед слів.
# Потім знайди перше слово в оригінальному списку, яке має цю частоту.
words = [
    "python",
    "java",
    "python",
    "ruby",
    "java",
    "c++",
    "ruby",
    "go",
    "javascript",
    "go",
    "go"
]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0)+1
print(freq)

min_freq = min(freq.values())
print(min_freq)

for word in words:
    if freq[word] == min_freq:
        print(word)
        break

print("8------------------------------------------------------------------")
# 
# Для кожної категорії знайди другий найдорожчий товар.
# Тут треба подумати, як зручно спочатку згрупувати товари, а потім провести аналіз кожної групи.
products = {
    "laptop": ("electronics", 1200),
    "phone": ("electronics", 800),
    "tablet": ("electronics", 600),
    "monitor": ("electronics", 300),

    "keyboard": ("accessories", 70),
    "mouse": ("accessories", 50),
    "hedphones": ("accessories", 100),
    "webcam": ("accessories", 80)
}

electronics = {}
for key, value in products.items():
    if value[0] == "electronics":
        electronics[key] = value[1]
print(electronics)
sec_el = sorted(electronics.keys(), key=lambda item: -electronics[item])[1]
print(sec_el)

accessories = {}
for key, value in products.items():
    if value[0] == "accessories":
        accessories[key] = value[1]
print(accessories)
sec_ac = sorted(accessories.keys(), key=lambda item: -accessories[item])[1]
print(sec_ac)

res = {
    "electronics": sec_el,
    "accessories": sec_ac
}
print(res)


print("9.--------------------------------------------------------------")
# Знайди всі слова з максимальною частотою.
# 1. довжина ↓
# 2. алфавіт ↑
# Спочатку треба визначити максимальну частоту, а вже потім застосовувати другі критерії.
words = [
    "cat",
    "dog",
    "cat",
    "python",
    "dog",
    "java",
    "python",
    "java",
    "code",
    "ruby",
    "ruby"
]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0)+1
print(freq)
max_freq = max(freq.values())
print(max_freq)

res = sorted(freq.keys(), key = lambda item:( max_freq, -len(item[1]), item))
print(res)