print("Створи функцію: яка повертає друге найбільше число зі списку. ")
def second_largest(numbers):
    numbers.sort(reverse=True)
    return numbers[1]
print(second_largest([1,2,3,4]))


print("Створи функцію: яка повертає список без повторень. ")
def remove_duplicates(numbers):
    list_rez = []
    for i in numbers:
        if i not in list_rez:
            list_rez.append(i)
    return list_rez
print(remove_duplicates([11,10,11,12]))  


print("Створи функцію: яка знаходить найдовше слово у списку. ")
def longest_word(words):
    max_word = words[0]
    for i in words:
        if len(i) > len(max_word):
            max_word = i
    return max_word
print(longest_word(["lion", "fox"]))    


print("Створи функцію: яка повертає словник.")
def count_letters(text):
    dict = {}
    for i in text:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return dict
print(count_letters("hello"))        


#print(" Створи функцію: яка повертає всі прості числа до limit.")
#def find_primes(limit):
