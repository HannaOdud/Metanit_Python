print("1.---------------------------------")
# Знайди назву найдешевшого товару.
products = {
    "laptop": 1200,
    "phone": 800,
    "mouse": 25,
    "keyboard": 70,
    "monitor": 300,
    "tablet": 600
}
res = min(products, key=products.get)
print(res)
#OR
res2 = [key for key,value in sorted(products.items(), key=lambda item:item[1])]
print(res2[0])

print("2.-------------------------------")
products = {
    "laptop": 1200,
    "phone": 800,
    "mouse": 25,
    "keyboard": 70,
    "monitor": 300,
    "tablet": 600,
    "webcam": 50
}
res = [key for key,value in sorted(products.items(), key=lambda item: item[1])]
print(res[0:3])

print("3.------------------------------")
scores = [
    85,
    92,
    76,
    92,
    88,
    95,
    85,
    95
]
no_duplicate = list(set(scores))
print(no_duplicate)
sort_sco = sorted(no_duplicate, reverse=True)
print(sort_sco)
print(sort_sco[1])
#OR
res = [item for item in sorted(no_duplicate, reverse=True) ]
print(res[1])

print("4.--------------------------------")
words = [
    "cat",
    "python",
    "dog",
    "algorithm",
    "book",
    "code",
    "AI",
    "banana"
]
print(words)
#res = [word for word in sorted(words, key=len)]
res = sorted(words, key=lambda item:(-len(item),item))
print(res)

print("5.-----------------------------")
numbers = [
    5,
    8,
    3,
    7,
    8,
    2,
    3,
    5
]
repeated = []
checked = []
for num in numbers:
    if num in checked:
        repeated.append(num)
        break
    else:
        checked.append(num)
print(repeated[0])

print("6.--------------------------")
words = [
    "Apple",
    "banana",
    "APPLE",
    "orange",
    "banana",
    "Kiwi",
    "ORANGE",
    "melon"
]
#clean_words
clean_words = [word.lower().strip(",.:;?! ") for word in words ]
print(clean_words)

#freq
freq = {}
for word in clean_words:
    freq[word] = freq.get(word, 0)+1

#first uniq
first_uniq = []
for word in clean_words:
    if freq[word] == 1:
        first_uniq.append(word)
        break
print(first_uniq[0])

print("7.---------------------------")
students = {
    "Anna": [85, 90, 88],
    "John": [72, 80, 75],
    "Mike": [95, 91, 94],
    "Kate": [88, 90, 89],
    "Lisa": [95, 91, 94]
}

print("8.---------------------------")
# Групування слів
#1 - Згрупуй слова за їхньою довжиною.
# - Потім знайди групу з найбільшою кількістю слів.
words = [
    "cat",
    "dog",
    "apple",
    "sun",
    "book",
    "banana",
    "car",
    "orange",
    "pen"
]
#1
freq = {}
for word in words:
    if len(word) in freq:
        freq[len(word)].append(word)
    else:
        freq[len(word)] = [word]
print(freq)
#2
res = max(freq.values())
print(res)

print("9.-------------------------")
words = [
    "python",
    "java",
    "python",
    "c++",
    "java",
    "ruby",
    "python",
    "java",
    "ruby",
    "go"
]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0)+1
print(freq)

sort_freq = sorted(
    freq.keys(),
      key=lambda word:(-freq[word], -len(word), word)
      )
print(sort_freq)

print