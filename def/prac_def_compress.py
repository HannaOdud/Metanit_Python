print("Створи функцію: ")
def compress(text):
    num = 1
    rez = text[0]
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            num = num+1
        else:
            rez = rez + str(num)
            num = 1
            rez = rez + text[i]
        if i == len(text)-1:
            rez = rez + str(num)
    return rez

print(compress("aaabbcccc"))
