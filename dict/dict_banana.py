#Порахувати, скільки разів кожна літера зустрічається у слові (наприклад, "banana" → {'b': 1, 'a': 3, 'n': 2}).
def count_letter(word):
    new_dict = dict()
    word_list = list(word)
    for letter in word_list:
        if letter in new_dict:
            new_dict[letter] += 1
        else:
            new_dict[letter] = 1
    return new_dict
print(count_letter("banana"))