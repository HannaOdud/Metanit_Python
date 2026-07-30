#1 Напиши функцію.
#Повертає словник, де:
#ключ — кількість голосних у слові;
#значення — список слів із такою кількістю голосних.
def group_by_vowels(text):
    words = text.split()
    vowels = ["a","e","i","o","u"]
    res = {}
    for word in words:
        count_vowels = 0
        for char in word:
            if char.lower() in vowels:
                count_vowels += 1
        res[count_vowels] = [word]
    return res
print(group_by_vowels("cat dog elephant book"))    

#

