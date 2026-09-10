print("1.-------------")
numbers = [3, 4, 7, 10, 13, 16, 21, 24]
sq = [number**2 for number in numbers if number%2==0]
print(sq)

print("2.-------------")
words = [" Python ", "JAVA", " python", "Java ", "C++", " python "]
res = {word.lower().strip(",.!&:; ") for word in words}
print(res)

print("3.----------------")
students = {
    "Anna": 85,
    "John": 62,
    "Mike": 91,
    "Kate": 74,
    "Tom": 55
}
res = {key:value for key,value in students.items() if value >= 75}
print(res)

print("4.-------------")
text = "Python is a powerful and popular programming language"
words = text.split()
res = {word for word in words if len(word)>5}
print(res)

print("5.-------------") 
words = ["cat", "python", "developer", "code", "algorithm"]
res = {word:len(word) for word in words if len(word)>4 }
print(res)

print("6.------------")
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
res = [number for inner_list in numbers for number in inner_list]
print(res)

print("7.------------")
numbers = [
    [1, 5, 8],
    [10, 13, 16],
    [21, 24, 27]
]
res = [number for inner_list in numbers for number in inner_list if number%2==0]
print(res)

print("8.----------")
words = ["apple", "banana", "kiwi", "orange"]
res = {i: word for i, word in enumerate(words)}
print(res)

print("9.---------")
res = (number for number in range(1,101) if number % 3 == 0 and number % 5 != 0)
for number in res:
    print(number)

print("10.-----------")
words = [
    "apple",
    "banana",
    "apple",
    "kiwi",
    "banana",
    "orange",
    "kiwi",
    "apple"
]
#step1
freq_dict = {}
for word in words:
    freq_dict[word] = freq_dict.get(word,0)+1
print(freq_dict)

#step2
step2 ={key for key,value in freq_dict.items() if value > 1}
print(step2)

#step3
dict_comp = {key:value for key,value in freq_dict.items() if value>1}
print(dict_comp)

#step4
step4 = [
    item[0]
    for item in sorted(
        freq_dict.items(),
        key=lambda item: item[1],
        reverse=True
    )
]
print(step4)