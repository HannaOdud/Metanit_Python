print("Transpose a Matrix")

matrix = [
 [1,2,3],
 [4,5,6]
]

res = []
for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    res.append(row)    
print(res)    