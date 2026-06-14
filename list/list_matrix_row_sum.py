print("Matrix Row Sums")
print("Given a list of lists:")
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
res = []

for i in matrix:
    sum = 0
    for j in i:
        sum = sum + j
    res.append(sum)    
print(res)