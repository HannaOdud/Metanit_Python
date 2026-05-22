#Practice "while"

#1. За допомогою while виведи числа від 1 до 10.
num = 1
while num <= 10:
    print(num) 
    num += 1

num = 1
while num < 5:  
    print (f" num = {num}")
    num += 1 
print ("End of cycle") 


#2. Створи програму, яка просить користувача ввести пароль, поки він не введе:
#"python123"
"""password = input("Please, enter your password: ")
while password != "python123":
    password = input("Wrong password, try again")  
print(f"Here we are: {password}")"""
        

#3.Сума введених чисел
#Користувач вводить числа. Програма працює, поки не введуть 0.
#Після цього виведи суму всіх введених чисел.
tot = 0
num = int(input("Please enter the number: "))
while num != 0:
    tot += num
    num = int(input("Please enter the number: "))
print("Sum: ",tot)


#4.Вгадати число. Створи гру: програма загадує число від 1 до 10;
#  користувач вгадує; цикл триває, поки число не буде вгадано.
r_num = 7
num = int(input("Please enter the number: "))
while r_num != num:
    num = int(input("Please enter the number: "))
print (f"Yesss...The random number: {r_num}")

#5. Намалюй трикутник із *****. За допомогою циклу виведи.
sign = "*"
n = 1
while n <= 5:
    print(sign * n)
    n += 1


