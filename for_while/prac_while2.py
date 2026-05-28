print("Числа від 1 до 10")
n = 0
while n < 10:
    n += 1
    print (n)

print("Виведи всі парні числа від 2 до 20.")
n = 0
while n < 10:
    n += 2
    print (n)

print("Зворотний відлік. Виведи числа від 10 до 1. Після цього надрукуй: \"Start\"")
n = 10
while n >= 1:
    print (n)
    if n == 1:
        print("Start..")
    n -= 1
print("Знайди суму чисел від 1 до 100 через while.")
n = 1
tot = 0
while n <= 100:
    tot = tot + n
    n += 1
print (f"Tot: {tot}")
#  
print("Користувач вводить число. Виведи таблицю множення від 1 до 10 через while. ")
m = int(input("Write the number: "))
n = 1
while n <= 10:
    print(f" {n} * {m} = {n * m}")
    n += 1
    
# 
#     