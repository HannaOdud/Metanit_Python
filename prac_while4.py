'''print("Факторіал. Обчисли факторіал числа через while.")
num = int(input("Write your num: "))
tot = 0
while num <= 1:'''


print ("Найбільше число. Користувач вводить числа. Ввід завершується числом 0. Знайди найбільше введене число.")
bigger_num = int(input("Write your num: "))
while True:
    num = int(input("Write your num: "))
    if num == 0:
        break
    if num > bigger_num:
        bigger_num =  num
    
print(f"The biggest num is: {bigger_num}")    

""" bigger = int(input("Write your num: "))
while bigger != 0:
    num = int(input("Write your num: "))
    if num > bigger:
        bigger = num
print(f"The biggest num is: {bigger}")   """   