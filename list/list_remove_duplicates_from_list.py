print("Тобто видалити дублікати, але зберегти порядок появи елементів.")
numbers = [4, 2, 5, 2, 7, 4, 8]

new_num = []
for n in numbers:
    if n not in new_num:
        new_num.append(n)
print(new_num)        