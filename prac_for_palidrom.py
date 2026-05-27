print("Паліндром. Перевір, чи слово читається однаково зліва направо і справа наліво.")

t = input("Write your word: ")
reverse = ""
for i in t:
    reverse = i + reverse
print(f"The words: {t} and reverse: {reverse}")
if t == reverse:
    print(f"The word {t} is palindrome")