print("Split a List into Chunks")
print("Split the list into chunks of size 4.")

numbers = list(range(0, 16))
n = 4
res = []
for i in range(0,len(numbers),n):
    res.append(numbers[i:i+n])
print(res)    