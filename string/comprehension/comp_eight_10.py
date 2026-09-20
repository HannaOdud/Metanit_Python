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
print(len_words)

# Знайди довжину, для якої є найбільше слів.
max_list_len = 0
for key,value in len_words.items():
    if len(value) > max_list_len:
        max_list_len = len(value)
print(max_list_len)

# Якщо кілька довжин мають однакову кількість слів — вибери меншу довжину.



print("5.-----------------------------------------------------------")
words = [
    "apple",
    "python",
    "banana",
    "house",
    "developer",
    "algorithm"
]
longest = [[word.append(word)] for word in words if word == max(words, key=len)]
print(longest)







