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

#12 Розбити речення на слова.
def split_text(text):
    return text.split()
print(split_text("Python is awesome"))

#13 Є список. Повернути:red-green-blue
def join_list_text(text):
    return "-".join(text)
print(join_list_text(["red", "green", "blue"]))

#14 Порахувати кількість слів у реченні. split()
def count_words(text):
    text = text.split()
    return len(text)
print(count_words("hello here, dont look like a stingy scrooge"))

#15 Повернути найдовше слово у реченні. Без max().
def longest_word(text):
    longest = ""
    for word in text.split():
        if len(word) > len(longest):
            longest = word
    return longest
print(longest_word("hello here, dont look like a stingy scrooge"))

#16 Порахувати кількість пробілів у рядку без циклу.
def count_space(text):
    return text.count(" ")
print(count_space("hello here, dont look like a stingy scrooge"))

#17 Замінити всі цифри символом "*".
def replace_digit(text):
    new_text = ""
    for char in text:
        if  char.isdigit():
            char = '*'
            new_text = new_text + char
        else:
            new_text = new_text + char
    return new_text
print(replace_digit("My phone is 12345"))

#18 Повернути всі слова, що починаються з великої літери.
def title_text(text):
    res = ""
    for char in text:
        if char.title():
            res = res + char
    res = res.split()
    return res
print(title_text("I Love Python And Kyiv"))

#19 Написати функцію
def normalize_name(name):
    return name.strip().lower().capitalize()
print(normalize_name("  oLENA   "))

#20 
def word_lengths(sentence):
    res = {}
    sent_split = sentence.split()
    for word in sent_split:
        res[word] = len(word)
    return res
print(word_lengths("Python is awesome"))