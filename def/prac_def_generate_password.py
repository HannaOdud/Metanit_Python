print("Створи функцію: яка генерує випадковий пароль. ")

import random

def generate_password(length):
    password = ""
    for p in range(length):
        symbol = random.randrange(0, 10)
        password = password + str(symbol)
    return password
print(generate_password(8))
print(generate_password(5))
print(generate_password(3))


print("------*------*------*------*------*------*------*------*------")

def random_stronger_password(length_pw):
    password2 = ""
    example = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for p in range(length_pw):
        symbol_index = random.randrange(0,len(example))
        symbol = example[symbol_index]
        password2 = password2 + symbol
    return password2
print(random_stronger_password(8))   
print(random_stronger_password(5))  
print(random_stronger_password(3))  

