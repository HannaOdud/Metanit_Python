#Напиши функцію, яка поверне список імен усіх студентів із найвищою оцінкою:
students = [
    {"name": "Anna", "score": 95},
    {"name": "Ivan", "score": 81},
    {"name": "Olena", "score": 90},
    {"name": "Petro", "score": 95}
]
def best_students(students):
    res_list = []
    max_score = 0
    for dict in students:
        if dict["score"] > max_score:
            max_score = dict["score"] 
    for dict in students:
        if dict["score"] == max_score:
            res_list.append(dict["name"])
    return res_list
print(best_students(students))