'''print("Перевернути слово. Користувач вводить слово. Виведи його у зворотному порядку через for.")
word= input("Write your word: ")
reverse = " "
for i in range(1, len(word)+1):
    index = len(word) - i
    new_char = word[index] 
    reverse = reverse + new_char
print(reverse)'''

print("Перевернути слово. Користувач вводить слово. Виведи його у зворотному порядку через for.")
word= input("Write your word: ")
reverse = ""
for i in word:
    reverse = i + reverse
print(f"Навпаки: {reverse}")    