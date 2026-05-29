print("Створи функцію count_words(text)")
def count_words(text):
    text_list = text.split()
    tot = len(text_list)
    return tot
print(count_words("My lovely man - Mr.Line"))