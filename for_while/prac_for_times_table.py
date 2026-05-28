'''print("Таблиця множення 1–10. Створи повну таблицю множення від 1 до 10.")
for i in range(1, 11):
    for j in range(1,11):
        print(f"{i} * {j} = {i * j}")'''

print("Таблиця множення 1–10. Створи повну таблицю множення від 1 до 10.")
for i in range(1, 11):
    for j in range(1,11):
        print(i*j, end="\t")
    print("\n")