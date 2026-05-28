'''
Practice "for" 
'''
#1.Вивести числа від 1 до 4
for i in range(4):
    print (i)



#2.Знайти суму всіх чисел від 1 до 100.
sum = 0
for i in range(101):
   sum += i 
print (sum)  



#3.Виведи таблицю множення для числа, яке вводить користувач. Наприклад для 5:
num = int( input("Enter your number (1-5): "))
for i in range(1,6):
    print( f" {num} * {i} = {num * i} ")



#4.Виведи всі парні числа від 1 до 10.
for i in range(0, 4, 2):
    print (i)


#5. Порахуй, скільки в ньому голосних букв.
text = "Hello Python"
char = ""
for i in range(len(text)):
    if text[i] == "e" or text[i] == "o":
        char += text[i]
print (char)


text = "Heeeello Python"
tot = 0
for i in text:
    if i == "e" or i == "o":
        tot += 1
print(f"Tot number of vowels are: {tot}")