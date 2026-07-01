#30 gpt_tasks
#1
def triple(number):
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
print(greeting("Олена!"))