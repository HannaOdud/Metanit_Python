print("Створи функцію: ")
'''def compress(text):
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

print(compress("aaabbcccc"))'''



def compress2(text2):
    res = text2[0]
    n = 1
    for i in range (1, len(text2)):
        if text2[i] == text2[i-1]:
            n = n + 1
        else: 
            res = res + str(n)
            res = res + text2[i]
            n = 1
        if i == len(text2)-1:
            res = res + str(n)    
    return res            



print(compress2("sssseeekkkmcccyuskfoo"))

