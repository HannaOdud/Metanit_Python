print("Find Unique Elements")
print("Given two lists: Create a list containing elements that appear in exactly one of the two lists.")
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = []
for i in a:
    if i not in b:
        c.append(i)
for j in b:
    if j not in a:
        c.append(j)
print(c)        