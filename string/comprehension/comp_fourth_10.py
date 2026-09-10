print("1.-----------------------")
# Знайди перше число, яке зустрічається вдруге.
freq = {} 
numbers = [4, 7, 2, 9, 7, 5, 2, 8]
for num in numbers:
    freq[num] = freq.get(num, 0)+1
print(freq)
res = []
for key,value in freq.items():
    if value > 1:
        res.append(key)
        break
#OR
res = [key for key,value in freq.items() if value > 1]
print(res[0])

print("2.----------------------")
numbers = [12, 5, 8, 20, 3, 20, 15, 12]
res = sorted(set(numbers), reverse = True)
print(res[1])

print("3.---------------------")
freq = {}
text = "programming"
for char in text:
    freq[char] = freq.get(char,0)+1
print(freq)

print("4.--------------------")
words = [
    "python",
    "java",
    "python",
    "c++",
    "java",
    "python",
    "ruby",
    "java"
]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0)+1
m_word = max(freq, key=freq.get)
print(m_word)

print("5.--------------------")
words = [
    "python",
    "java",
    "python",
    "c++",
    "java",
    "ruby"
]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0)+1
res = []
max_v = float("-inf")
max_k = ""
for key,value in freq.items():
    if value > max_v:
        max_v = value
        max_k = key
for key,value in freq.items():
    if value == max_v:
        res.append(key)
#OR 
#res = [key for key,value in freq.items() if value == freq[max(freq, key=freq.get)]]
print(res)

print("6.-------------------")
words = [
    "cat",
    "dog",
    "apple",
    "book",
    "banana",
    "car"
]
freq = {}
for word in words:
    if len(word) in freq:
        freq[len(word)].append(word)
    else:
        freq[len(word)] = [word]
print(freq)

print("7.------------------")
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9] 
set1 = set(list1)
set2 = set(list2)
res = set1.intersection(set2)
print(res)
#OR
res = {num for num in list1 if num in list2}
print(res)