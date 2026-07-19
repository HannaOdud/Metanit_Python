#first 20 tasks

#1 Напиши функцію: Повертає рядок у нижньому регістрі.
def make_lower(text):
    return text.lower()
print(make_lower("HeLlo"))

#2 Повертає рядок у верхньому регістрі.
def make_upper(text):
    return text.upper()
print(make_upper("hellO"))

#3 Повертає рядок, у якому лише перша літера велика.
def capitalize_text(text):
    return text.capitalize()
print(capitalize_text("hello"))

#4Повертає рядок, де кожне слово починається з великої літери.
def title_text(text):
    return text.title()
print(title_text("hello here, dont look like a stingy scrooge"))

#5 Прибирає пробіли на початку і в кінці рядка.
def remove_spaces(text):
    text.strip()
print(remove_spaces(" hello here, dont look like a stingy scrooge "))

#6 Замінити всі пробіли символом _.
def replace_spaces(text):
    return text.replace(" ", "_")
print(replace_spaces(" hello here, dont look like a stingy scrooge "))

#7 Замінити всі "a" на "*".
def replace_a(text):
    return text.replace("a", "*")
print(replace_a("hello here, dont look like a stingy scrooge"))

#8 Порахувати, скільки разів зустрічається буква "o".
def count_o(text):
    return text.count("o")
print(count_o("hello here, dont look like a stingy scrooge"))

#9 Повернути індекс першої букви "e". Якщо її немає — повернути -1.
def find_e(text):
    return text.find("e")
print(find_e("hello here, dont look like a stingy scrooge"))

#10 Перевірити, чи рядок починається зі слова "https".
def check_if_startswith(text):
    return text.startswith("https")
print(check_if_startswith("hello here, dont look like a stingy scrooge"))

#11 Перевірити, чи ім'я файлу закінчується на .txt
def check_if_endswith(text):
    return text.endswith(".txt")
print(check_if_endswith("hello here, dont look like a stingy scrooge"))