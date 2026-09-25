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
max_len_w = max(set_words, key=lambda item:(len(item), item))
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

odd_num = [num for num in numbers if freq[num]%2==1]
print(odd_num)

uniq_num = [num for num in odd_num if set(odd_num)]
max_uniq_num = max(uniq_num)
print(max_uniq_num)