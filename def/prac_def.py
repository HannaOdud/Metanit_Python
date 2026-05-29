'''def print_person(name ="Tom", age = 18):
    print(f"Name: {name} Age: {age}")
print_person()
print_person("Bob")
print_person("Sam", 37)  '''

'''def sum(*numbers):
    result = 0
    for i in numbers:
        result += i
    print(f"Sum = {result}")    
sum(1, 2, 3, 4, 5)   
sum(3, 4, 5, 6) '''

print("Створи функцію add(a, b), яка повертає суму двох чисел.")
a = 5
b = 3
def add(a,b):
    print(a + b)
add(a,b)


def addd(a,b):
    print(a + b)
addd(5,4)

def is_even(num):
    if num % 2 == 0:
        print(f"Num is even: {num}")
    else: 
        print("Not even!")
is_even(5)
is_even(6)
is_even(7)

def square(num):
    rez = num * num
    return rez
print(square(5))

print("Створи функцію max_number(a, b), яка повертає більше число.")
def max_number(a,b):
    if a > b:
        return a
    else: 
        return b
print(max_number(8,9))    

print("Створи функцію word_length(word), яка повертає кількість букв у слові.")
def word_length(word):
    return len(word)
print (word_length("Tuesday"))

print("Створи функцію count_vowels(text), яка рахує голосні букви.")
def count_vowels(text):
    tot = 0
    for i in text:
        if i == "a" or i == "o" or i == "e" or i == "i" or i == "y" or i == "u":
            tot = tot + 1
    return tot
print(count_vowels("weather")) 

print("9. Факторіал. Створи функцію factorial(n).") 
def factorial(n):
    tot = 1
    for i in range(1,n+1):
        tot = tot * i
    return tot
print(factorial(5))  

print("Створи функцію multiplication_table(num), яка друкує таблицю множення.")
def multiplication_table(num):
    for i in range(1, 11):
        print(f"{i} * {num} = {i * num} ")
multiplication_table(5) 


print("Створи функцію is_palindrome(word). Функція повинна перевіряти, чи слово є паліндромом.")
def is_palindrome(word):
    new_word = ""
    for i in word:
        new_word = i + new_word
    if word == new_word:
        return(f"{word} - Is palindrome")
    else: return (f"{word} - Is not palindrome")
print(is_palindrome("tot"))    


print("Створи функцію is_prime(num).")
def is_prime(num):
    for i in range (2, num):
        if num % i == 0:
            return (f"{num} - is not a prime number")
    return(f"{num} - is a prime num")    
print(is_prime(5))


print("Створи функцію find_max(numbers) без використання max()")
def find_max(numbers):
    max_number = numbers[0]
    for i in numbers:
        if max_number < i:
            max_number = i
    return(f"{max_number} is Max number in {numbers}")    
print(find_max([2, 3, 4, 5]))    


print("Середнє значення списку. Створи функцію average(numbers). ")
def average(numbers):
    tot = 0
    for i in numbers:
        tot = tot + i
    avg = tot / len(numbers)
    return avg
print(average([1, 2, 3, 4]))

print("Створи функцію fizzbuzz(n)")
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return " Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else: return "None"
print(fizzbuzz(15))    