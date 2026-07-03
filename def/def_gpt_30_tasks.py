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

'''#11 Повертає кількість пробілів
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

#19 Повертає рядок навпаки. Без [::-1].
def reverse_sentence(text):
    new_text = ""
    for letter in text:
        new_text = letter + new_text 
    return new_text
print(reverse_sentence("Hello"))

#20 Повертає True, якщо рядок починається з букви "A" або "a".
def starts_with_a(text):
    if text[0] == "A" or text[0] == "a":
        return True
    return False
print(starts_with_a("Hello"))
print(starts_with_a("again"))'''

# 21 Повертає суму всіх чисел.Без sum().
def sum_numbers(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total
print(sum_numbers([1,2,3,4,5]))   

#22 Повертає добуток усіх чисел.
def multiply_numbers(numbers):
    tot = 1
    for n in numbers:
        tot = tot * n
    return tot
print(multiply_numbers([1,2,3,4,5]))   

#23 Повертає кількість додатних чисел.
def count_positive(numbers):
    tot = 0
    for n in numbers:
        if n > 0:
            tot = tot + 1
    return tot
print(count_positive([0,1,2,3,4,5,-1,-2,-3]))

#24 
def count_negative (numbers):
    tot = 0
    for n in numbers:
        if n < 0:
            tot = tot + 1
    return tot
print(count_negative([0,1,2,3,4,5,-1,-2,-3]))

#25 Повертає перше парне число.
def first_even(numbers):
    for n in numbers:
        if n %2 == 0:
            return n
print(first_even([1,3,5,7,8])) 

#26  Повертає останнє парне число.    
def last_even(numbers):
    new_lst = []
    for n in numbers:
        if n % 2 == 0:
            new_lst.append(n)
    return new_lst [-1]
print(last_even([1,2,3,4,5]))
 #OR
def last_even(numbers):
    lst = 0
    for n in numbers:
        if n%2 == 0:
            lst = n
    return lst        
print(last_even([1,2,3,4,5,6]))

#27 Повертає новий список, де кожне число піднесене до квадрата.
def square_list(numbers):
    new_lst = []
    for n in numbers:
        new_lst.append(n * n)
    return new_lst
print(square_list([1,2,3,4,5]))

#28 Повертає список у зворотному порядку. Без reverse() і [::-1].
def reverse_list(numbers):
    new_lst = []
    for n in range(len(numbers)-1, -1, -1):
        new_lst.append(numbers[n])
    return new_lst
print(reverse_list([1,2,3,4,5]))

#29 Рахує, скільки разів зустрічається число.
def count_occurrences(numbers, value):
    count = 0
    for n in numbers:
        if n == value:
            count = count + 1
    return count
print(count_occurrences([1,2,2,3,2], 2))

#30 Повертає друге найбільше число.
def second_largest(numbers):
    largest = float("-inf")
    second_largest = float("-inf")
    for n in numbers:
        if n > largest:
            second_largest = largest
            largest = n
    return second_largest
print(second_largest([7, 3, 9, 2, 5]))
    

