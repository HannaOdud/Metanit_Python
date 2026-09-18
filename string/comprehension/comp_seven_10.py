print("1.-----------------------------------------------------------------")
#Знайди найдорожчий товар, ціна якого менша за 700.
products = {
    "laptop": 1200,
    "phone": 800,
    "mouse": 25,
    "keyboard": 70,
    "monitor": 300,
    "tablet": 600,
    "webcam": 50
}
cheaper = {key:value for key,value in products.items() if value < 700}
print(cheaper)
max_val = max(cheaper.values())
res = [key for key,value in cheaper.items() if value == max_val]
print(res[0])

# shorter way
cheaper = {key:value for key,value in products.items() if value < 700}
res = max(cheaper, key=cheaper.get)
print(res)

print("2.------------------------------------------------------------------")
# Якщо кілька слів мають однакову довжину — вибери перше за алфавітом.
words = [
    "cat",
    "python",
    "developer",
    "code",
    "algorithm",
    "AI",
    "programming"
]
res = sorted(words, key = lambda w: (-len(w),w))
print(res[0])


print("3.-----------------------------------------------------------------")
# Найменша унікальна частота
words = [
    "python",
    "java",
    "python",
    "c++",
    "java",
    "ruby",
    "go",
    "go"
]
freq = {}
for word in words:
    freq[word] = freq.get(word,0)+1
small_freq = min(freq.values())
print(small_freq)
res = [key for key,value in freq.items() if value == small_freq]
print(res)

print("4.------------------------------------------------------------")
#First repeated після нормалізації
words = [
    "Python",
    "JAVA",
    "python",
    "Ruby",
    "java",
    "RUBY",
    "C++"
]
clean_words = [word.lower().strip(",.;:?! ") for word in words] 
print(clean_words)
checked = set()
for word in clean_words:
    if word in checked:
        print(word)
        break
    checked.add(word)


print("5.-----------------------------------------------------------")
# Другий найдешевший унікальний товар
prices = [
    1200,
    800,
    25,
    800,
    300,
    1200,
    600,
    25
]
unique_price = list(set(prices))
sort_unique = sorted(unique_price)
print(sort_unique[1])

print("6.--------------------------------------------------------")
# сортування за двома критеріями: оцінка ↓, при однаковій оцінці — ім'я ↑
students = {
    "Anna": 90,
    "John": 85,
    "Mike": 90,
    "Kate": 75,
    "Lisa": 85,
    "Tom": 90
}
res = [key for key,value in sorted(students.items(), key=lambda w:w[1], reverse=True)]
print(res)

print("7.------------------------------------------------------")
# Групування за першою літерою
words = [
    "apple",
    "algorithm",
    "banana",
    "book",
    "cat",
    "code",
    "python",
    "program"
]
group = {}
for word in words:
    if word[0] in group:
        group[word[0]].append(word)
    else:
        group[word[0]] = [word]
print(group)
res = [key for key,value in sorted( group.items(), key=lambda w: len(w))]
print(res[0])

print("8.---------------------------------------------------------------")
# Найчастіше слово певної довжини
# Знайди найчастіше слово серед слів довжиною 3.
#кщо частота однакова — вибери слово за алфавітом.
#Тут тобі потрібно подумати про порядок дій: відфільтрувати ↓ порахувати частоти, знайти максимум

words = [
    "cat",
    "dog",
    "sun",
    "car",
    "apple",
    "house",
    "banana",
    "orange",
    "python"
]
clean_word = [word.lower().strip(",.:;?! ") for word in words]
freq = {}
for word in clean_words:
    freq[word] = freq.get(word, 0)+1
print(freq)
max_freq = max(freq.values())
print(max_freq)
res = [key for key,value in freq.items() if value == max_freq]
print(res[0])

print("9.----------------------------------------------------------------------")
# найбільший середній бал;
# якщо середні однакові — найбільше унікальних оцінок;
# якщо і це однаково — ім'я за алфавітом. 
students = {
    "Anna": [85, 90, 85, 95],
    "John": [70, 80, 70, 75],
    "Mike": [95, 95, 90, 95],
    "Kate": [80, 85, 80, 90],
    "Lisa": [95, 90, 95, 90]
}
avg_st = {key:sum(value)/len(value) for key,value in students.items()}
print(avg_st)
max_avg_mark = max(avg_st.values())
print(max_avg_mark)
res = sorted(students.items(), key=lambda item:(
    -sum(item[1])/len(item[1]),
    -len(set(item[1])),
    item[0]
))
print(res)


print("10.--------------------------------------------------------------------")
words = [
    "Python",
    "python",
    "JAVA",
    "java",
    "Java",
    "C++",
    "c++",
    "ruby",
    "Ruby",
    "go",
    "GO",
    "javascript",
    "JavaScript",
    "python",
    "PHP"
]
# step1
clean_words = [word.lower().strip(",.:;?! ") for word in words]
print(clean_words)

#step2
freq = {}
for word in clean_words:
    freq[word] = freq.get(word, 0)+1
print(freq)

#step3
max_val = max(freq.values())
print(max_val)

#step4
words_with_max_val = [key for key,value in freq.items() if value == max_val]
print(words_with_max_val)

#step5 first_unique
for word in clean_words:
    if freq[word] == 1:
        print(word)
        break


#step6 first repeated in clean_word
checked = set()
for word in clean_words:
    if word in checked:
        print(word)
        break
    checked.add(word)

#step7 dictionary тільки для слів із частотою >= 2.
freq_two = {key:value for key,value in freq.items() if value >= 2}
print(freq_two)

#step8 Відсортуй усі унікальні слова за правилами:1. частота ↓ 2. довжина ↓ 3. алфавіт ↑
unique_w = list(set(clean_words))
print(unique_w)
sort_uniques = sorted(unique_w, key=lambda w: (-freq[w],-len(w),w))
print(sort_uniques)

#step9
# Знайди другу найбільшу унікальну частоту.
unique_freq = sorted(set(freq.values()), reverse=True)
sec_max_freq = unique_freq[1]
sec_max_freq_word = [key for key,value in freq.items() if value == sec_max_freq ]
print(sec_max_freq_word)

#step10 перший оригінальний елемент, який має другу частоту
for word in clean_words:
    if freq[word] == sec_max_freq:
        print(word)
        break