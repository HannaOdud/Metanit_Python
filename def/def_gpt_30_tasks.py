#30 gpt_tasks
#1
'''def triple(number):
    return number*3
print(triple(3))
#2
def power(number):
    return number*number
print(power(4))
#3
def is_negative(number):
    if number < 0:
        return True
print(is_negative(-2))
#4
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print(maximum(3, 4))    
#5
def repeat_word(word):
    return word * 2
print(repeat_word("Hello "))
#6
def first_character(text):
    return text[0]
print(first_character("Hello"))
#7
def middle_character(text):
    middle_index = len(text)//2
    return text[middle_index]
print(middle_character("Hello"))
print(middle_character("word"))
#8
def multiply_three(a, b, c):
    return a*b*c
print(multiply_three(1,2,3))
#9
def is_multiple_of_five(number):
    if number%5 == 0:
        return True
    else:
        return False
print(is_multiple_of_five(25))
print(is_multiple_of_five(24))
#10
def greeting(name):
    return f"Доброго дня, {name}"
print(greeting("Олена!"))'''

#11 Повертає кількість пробілів
def count_spaces(text):
    count = 0
    for t in text:
        if t == " ":
            count = count + 1
    return count
print(count_spaces("Hello world"))

#12 Повертає кількість букв "a".
def count_letter_a(text):
    count = 0
    for a in text:
        if a == "a":
            count = count +1
    return count
print(count_letter_a("Hello again"))

#13 Повертає рядок без пробілів.
def remove_spaces(text):
    return text.replace(" ","")
print(remove_spaces("Hello world"))

#14 Повертає перше слово.
def first_word(text):
    return text.split()[0]
print(first_word("Hello world"))

#15 Повертає останнє слово.
def last_word(text):
    return text.split()[-1]
print(last_word("Hello world"))

#16 Повертає довший рядок.
def longer_text(text1, text2):
    if len(text1) > len(text2):
        return text1
    else:
        return text2
print(longer_text("Hello", "friend"))

#17 Повертає кількість цифр у рядку
def count_digits(text):
    num = ["1","2","3","4","5","6","7","8","9","0"]
    count = 0
    for n in text:
        if n in num:
            count = count + 1
    return count
print(count_digits("Hel1l2o wo7ld8"))

#18 Повертає кількість великих літер. 
def count_uppercase(text):
    count = 0
    for char in text:
        if char.isalpha() and char == char.upper():
            count = count + 1
    return count        
print(count_uppercase("HelLO world"))

#OR 
def count_uppercase(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    return count        
print(count_uppercase("HelLO world"))