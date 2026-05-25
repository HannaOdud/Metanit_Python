print("Програма повинна запитувати пароль, поки користувач не введе:")
isCorrect = False
while isCorrect == False:
    p_ww= input("Write your password: ")
    if p_ww == "admin123":
        print("Access granted")
        isCorrect = True
        

print(" Сума введених чисел. Користувач вводить числа. Програма працює, поки не введуть 0. \n Після завершення виведи загальну суму.")        
tot = 0
while True:
    n = int(input("Write the number: "))
    tot = tot + n
    if n == 0:
        break
print(f"Total: {tot}")

print("10. Розворот числа. Користувач вводить число. Виведи його у зворотному порядку.")
n = input("Write the number: ")
l = len(n)-1
rez = ""
while l >= 0:
    rez += n[l]
    l -= 1
print (f"Result: {rez}")