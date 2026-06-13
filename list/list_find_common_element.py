print("Find Common Elements")
print("Given two lists:")
print("Create a new list containing only the common elements.")

'''a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
res = []
for i in a:
    for j in b:
        if i == j:
            res.append(i)
print(res)   '''     


a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
res = []
for i in a:
    if i in b:
        res.append(i)
print(res)        