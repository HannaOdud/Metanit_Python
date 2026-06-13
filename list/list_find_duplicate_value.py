print("Find Duplicate Values")
print("Return a list containing every duplicated value only once.")

numbers = [2, 5, 7, 5, 3, 2, 8, 7]
duplicates = []
new_set = set()
for n in numbers:
    if n in new_set:
        duplicates.append(n)
    else:
        new_set.add(n)
print(duplicates)
print(new_set)        