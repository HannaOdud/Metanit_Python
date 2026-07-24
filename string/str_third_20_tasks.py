#1 Напиши функцію. Повертає словник, де:
# #ключ — перша літера слова; 
# #значення — кількість слів, що починаються на цю літеру.

def first_letter_count(text):
    words = text.split()
    res = {}
    for word in words:
        if word[0] in res:
            res[word[0]] += 1
        else:
            res[word[0]] = 1
    return res
print(first_letter_count("Apple Ant Banana Ball Cat"))

#2 Напиши функцію.Повертає найдовше слово, що містить хоча б одну цифру.
def longest_with_num(text):
    longest = ""
    words = text.split()
    for word in words:
        if any(char.isdigit() for char in word):
            if len(word) > len(longest):
                longest = word
    return longest
print(longest_with_num("I am abc123 Programming22 test1"))

#OR
def longest_with_num1(text):
    longest = ""
    words = text.split()
    for word in words:
        for char in word:
            if char.isdigit():
                if len(word) > len(longest):
                    longest = word
                break
    return longest
print(longest_with_num1("I am abcdefg123 test1"))
