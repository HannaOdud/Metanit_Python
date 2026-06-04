print("Міні-проєкт №2 — Система оцінок")
print("Створи функції: ")
print("------*------*------*-------*-------*-------")

grades = [95, 88, 76]

def add_grades():
    new_grade = int(input("Please add a new grade: "))
    grades.append(new_grade)

def show_grades():
    for i in grades:
        print(i)

def average_grades():
    avg = sum(grades) / len(grades)
    print(round(avg,2))

def best_grades():
    print(max(grades))

def menu():
    while True:
        print("------*------*------*-------*-------*-------")
        print("1. Add grade")
        print("2. Show grades")
        print("3. Average grade")
        print("4. Best grade")
        print("0. Exit")
        print("------*------*------*-------*-------*-------")

        choice = input("Select your option: ")
        if choice == "1":
            add_grades()
        elif choice == "2":
            show_grades()
        elif choice == "3":
            average_grades()
        elif choice == "4":
            best_grades()
        elif choice == "0":
            break
        else:
            print("Invalid input! ")

menu()




