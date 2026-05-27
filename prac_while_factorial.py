#Факторіал. Обчисли факторіал числа через while.
num = int(input("Write your num: "))
tot = 1
i = 1
while i <= num:
    tot = i * tot
    i = i + 1
print (f"Total: {tot}")