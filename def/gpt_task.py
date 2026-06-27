#1
'''def introduce(name, age):
    print(f"Мене звати {name}. Мені {age} років.")
introduce("Олена", 25)
#2
def multiply(a, b):
    print(a * b)
multiply(4, 7)
#3
def even_or_odd(number):
    if number % 2 == 0:
        print ("Even")
    else: 
        print("Odd")
even_or_odd(3)
even_or_odd(4)
#4
def stars(count):
    print(count * "*")
stars(5)'''

#1
def cube(number):
    return number * number * number
print(cube(3))

#2
def is_positive(number):
    if number > 0:
        return(True)
    if number < 0:
        return(False)
print(is_positive(5))
print(is_positive(-2))

#3
def full_name(first, last):
    return first+" " + last
print(full_name("Іван", "Петренко"))