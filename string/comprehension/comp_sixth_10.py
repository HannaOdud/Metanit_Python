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
#OR
checked = set()
for num in numbers:
    if num in checked:
        print(num)
        break
    checked.add(num)

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

print("7.----------------------------------------------------------------------")
students = {
    "Anna": [85, 90, 88],
    "John": [72, 80, 75],
    "Mike": [95, 91, 94],
    "Kate": [88, 90, 89],
    "Lisa": [95, 91, 94]
}
st_avg = {key: sum(value)/len(value) for key,value in students.items()}
print(st_avg)
st_ranking = sorted(st_avg.items(), key=lambda item:item[1],reverse=True)
print(st_ranking)
best_st = sorted(
    st_avg.items(),
    key=lambda item:(-item[1],item[0])
)  
print(best_st)

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
res = max(freq.values(),key=len) # <== означає знайди найбільший список за його довжиною.
print(res)

print("9.-----------------------------------------------------------------------------------")
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
      )[0][0]
print(sort_freq)

print("10.---------------------------------------------------------------------------------------")
words = [
    "Python",
    "python",
    "JAVA",
    "java",
    "C++",
    "c++",
    "ruby",
    "Ruby",
    "go",
    "Go",
    "javascript",
    "JavaScript",
    "python"
]

#clean word
clean_words = [word.lower().strip(",.?!:; ") for word in words]
print(clean_words)

#freq dict
freq = {}
for word in clean_words:
    freq[word] = freq.get(word, 0)+1
print(freq)

#max_freq
max_freq = max(freq.values())
print(max_freq)

#all words with max_freq
res = [key for key,value in freq.items() if value==max_freq]
print(res)

#first_unique word
fuw = []
for word in clean_words:
    if freq[word] == 1:
        fuw.append(word)
        break
print(fuw)

#dict for repeated word
repeated = { key:value for key,value in freq.items() if value >= 2}
print(repeated)

#sort: freq(word)desc, len(word)acs, word alphab
srt = sorted(freq, key=lambda word:( -freq[word], -len(word),word))
print(srt)

# list of unique words
set_freq = {key:value for key,value in freq.items()}
print(set_freq)
res = sorted(set_freq, key=lambda word:(-freq[word]))
print (res)

#second most frequent word
uniq_freq = sorted(set(freq.values()),reverse=True)
print(uniq_freq)
second_max_freq = 0
if len(uniq_freq) > 1:
    second_max_freq = uniq_freq[1]
    second_max_freq_words = [key for key,value in freq.items() if value == second_max_freq]
    print(second_max_freq_words)

for word in clean_words:
    if freq[word] == second_max_freq:
        print(word)
        break


#перше слово в оригінальному списку, яке має другу найбільшу унікальну частоту.
first_word_of_second_max_freq_words = second_max_freq_words[0]
print(first_word_of_second_max_freq_words)