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
