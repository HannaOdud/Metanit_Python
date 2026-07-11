#Порахуй кількість кожного слова у реченні.
'''cat dog cat bird dog dog
{
    "cat": 2,
    "dog": 3,
    "bird": 1
}'''
def count_words(words):
    res_dict = dict()
    a_list = words.split()
    for word in a_list:
        if word in res_dict:
            res_dict[word] = res_dict[word] + 1
        else:
            res_dict[word] = 1
    return res_dict
print(count_words("cat dog cat bird dog dog"))


#Створи словник, який порахує, скільки разів зустрічається кожне ім'я.

students = [
    "Anna",
    "Ivan",
    "Anna",
    "Olena",
    "Ivan",
    "Anna"
]
def count_dict_name(students):
    count_name = {}
    for name in students:
        if name in count_name:
            count_name[name] = count_name[name] + 1
        else:
            count_name[name] = 1
    return count_name
print(count_dict_name(students))