print("Створи функцію reverse_text(text)")
def reverse_text(text):
    reversed_word = ""
    for i in text:
        reversed_word = i + reversed_word
    return reversed_word
print(reverse_text("weather "))    