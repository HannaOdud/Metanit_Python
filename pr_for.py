'''
print("Виведи таблицю множення від 1 до 10.")
num = int(input("Write your num: "))
tot = 0
for i in range(1, 11):
    tot = i*num
    print(f"{i}*{num} = {tot}")'''

'''print("Виведи кожну букву окремо через for.")
text = "Python"
for i in text:
    print(i)'''

'''print("Порахуй, скільки букв \"a\" є у слові.")
text = "banana"
tot = 0
for i in text:
    if i == "a":
        tot = tot + 1
print(f"Tot \"a\" in text: {tot}")'''

'''print("Знайди суму всіх парних чисел від 1 до 50.")
tot = 0
for i in range(2,51,2):
    tot = tot + i
print(tot)   ''' 


'''print("трикутник із зірочок")
num = int(input("Write your num: "))
for i in range(1,num+1):
    print(i * "*")'''

print("Перевернути слово. Користувач вводить слово. Виведи його у зворотному порядку через for.")
word= input("Write your word: ")
reverse = " "
for i in range(1, len(word)+1):
    index = len(word) - i
    new_char = word[index] 
    reverse = reverse + new_char
print(reverse)    

