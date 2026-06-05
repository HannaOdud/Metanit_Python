print("1.-----------------------------------------------------")
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print(student)
print("2.-----------------------------------------------------")
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022
}
print(car["brand"])
print(car["model"])

print("3.-----------------------------------------------------")
person = {
    "name": "John",
    "age": 30
}
person ["city"] = "London"
print(person)

print("4.-----------------------------------------------------")
product = {
    "name": "Laptop",
    "price": 800,
}
product["price"] = 900
print(product)
print("5.-----------------------------------------------------")
book = {
    "title": "Python Basic",
    "author":"Mike",
    "pages": 250
}
print(book)

if "pages" in book:
    del book["pages"]
print(book)

print("6.-----------------------------------------------------")
scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
for key,value in scores.items():
    print(f"Key: {key} Value: {value}")
for key in scores:
    print(f"Key:{key} Value: {scores[key]}")

print("7.-----------------------------------------------------")
print("Write a program that counts how many times each word appears in the following list:")
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
new_dic = dict()
for word in words:
    if word in new_dic.keys():
        new_dic[word] = new_dic[word] + 1  
    else:
        new_dic[word] = 1
print(new_dic)

print("8.-----------------------------------------------------")
print("Find and print the month with the highest sales.")
sales = {
    "January": 1200,
    "February": 1800,
    "March": 1500,
    "April": 2100
}
max_key = None
max_value = float('-inf') # (-infinity)
for key, value in sales.items():
    if max_value < value:
        max_key = key
        max_value = value
print(max_key,max_value)

print("9.-----------------------------------------------------")
print("Create a new dictionary where:All keys from both dictionaries are included.")
print("If a key exists in both dictionaries, add their values together.")

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "b": 50,
    "d": 40
}
dict3 = {}
dict3.update(dict1)
for key,value in dict2.items():
    print(f"Key: {key}, value: {value}")
    if key in dict3.keys():
        dict3[key] = dict3[key] + dict2[key]
    else: 
        dict3[key] = dict2[key]
print(dict3)


print("10.-----------------------------------------------------")
print("Write a program that:")
("1. Calculates the average score for each student.")
("2. Finds the student with the highest average.")
("3. Prints the student's name and average score")

students = {
    "Alice": {"math": 90, "science": 85, "english": 88},
    "Bob": {"math": 75, "science": 80, "english": 78},
    "Charlie": {"math": 95, "science": 92, "english": 90}
}

avg_scores = {} 

for student, subjects in students.items():
    score_sum = 0
    for subject, score in subjects.items():
        score_sum = score_sum + score
    avg = round((score_sum / len(subjects)), 2)
    avg_scores[student] = avg
print(avg_scores)        

max_k = None
max_v = float('-inf') # (-infinity)
for key, value in avg_scores.items():
    if max_v < value:
        max_k = key
        max_v = value
print(f"Top student: {max_k}")
print(f" Average score: {max_v}")



