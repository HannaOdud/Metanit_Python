#def_gpt_20_tasks
#1
'''def double(number):
    return number * 2
print(double(3))

#2
def subtract(a, b):
    return a-b
print(subtract(7, 5))

#3
def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False
print(is_even(2))
print(is_even(3))

#4
def minimum(a, b):
    if a < b:
        return a
    else: 
        return b
print(minimum(1,3))

#5
def greeting(name):
    return name
print(greeting("Привіт, Олено!"))'''

#6
def rectangle_area(width, height):
    return width * height
print(rectangle_area(4, 5))

#7 
def longer_word(word1, word2):
    if len(word1) == len(word2):
        return word1
    elif len(word1) > len(word2):
        return word1
    else: 
        return word2
print(longer_word("sun", "shine"))

#8 
def last_character(text):
    return text[-1]
print(last_character("Hello again"))

#9
def first_and_last(text):
    return text[0]+text[-1]
print(first_and_last("Hello again"))

#10
def absolute(number):
    if number >= 0:
        return number
    else: 
        return number * -1
print(absolute(-2))

#11
def count_letters(word):
    count = 0
    for w in word:
        count = count + 1
    return count
print(count_letters("Hello again"))

#OR

def count_letters(word):
    count = 0
    for index, value in enumerate(word):
        if value != " ":
            count = index + 1
    return count    
print(count_letters("Hello again"))

#12
def reverse_word(word):
    rev = ""
    for letter in word:
        rev = letter + rev
    return rev
print(reverse_word("word"))

#13
def sum_to_n(n):
    tot = 0
    for num in range(n +1):
        tot = tot + num
    return tot    
print(sum_to_n(5))

#14
def factorial(n):
    tot = 1
    for num in range(1, n+1):
        tot = tot * num
    return tot
print(factorial(5))

#15
def count_even(numbers):
    tot = 0
    for n in numbers:
        if n % 2== 0:
            tot = tot + n
    return tot
print(count_even([1,2,3,4]))    

#16
def largest(numbers):
    max_num = 0
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num
print(largest([1, 2, 3]))       

#17
def smallest(numbers):
    min_num = 1
    for n in numbers:
        if n < min_num:
            min_num = n
    return min_num
print(smallest([1, 2, 3]))

#18
def average(numbers):
    tot = 0
    avg = 0
    for n in numbers:
        tot = tot + n
        avg = tot / len(numbers)
    return avg
print(average([1,2,3,4,5]))    

#19
def count_vowels(text):
    tot_vow = ""
    for v in text:
        if v == "a" or v == "e" or v == "o" or v == "i":
            tot_vow = tot_vow + v
    return tot_vow
print(count_vowels("word"))

#20
def is_palindrome(text):
    if all(text[i] == text[- i- 1] for i in range(len(text) // 2)):
        return True
    else:
        return False
print(is_palindrome("level"))    
#OR
def is_palindrome2(text):
    if text == text[::-1]:
        return True
    else: 
        return False
print(is_palindrome2("madam"))    