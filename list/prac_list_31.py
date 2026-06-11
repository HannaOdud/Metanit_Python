print("Create a new list containing the elements in reverse order without using .reverse() or reversed().")
'''numbers = [1, 2, 3, 4, 5]
rev_num = numbers[::-1]
print(rev_num)  '''

'''numbers = [1, 2, 3, 4, 5]
rev_num = []
for i in numbers:
    rev_num = [i] + rev_num
    print(rev_num)
print(rev_num)  '''  

'''numbers = [1, 2, 3, 4, 5]
rev = []
for i in range(len(numbers)-1, -1, -1):
    rev.append(numbers[i])
print(rev) '''  

numbers = [1, 2, 3, 4, 5]
r = []
i = len(numbers)-1
while i>=0 :
    r.append(numbers[i])
    i= i-1
print(r)    

print("------------------------------------------------------------")
print("Create a dictionary that counts how many times each word appears.")
words = ["apple", "banana", "apple", "orange", "apple", "banana"]
fruits = {}
for fruit in words:
    if fruit not in fruits.keys():
        fruits[fruit] = 1
    else:
        fruits[fruit] = fruits[fruit] + 1    
print(fruits)
print("------------------------------------------------------------")
'''a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
c = a + b
print(c)
temporary = 0
for i in range(len(c)):
    for j in range(i+1, len(c)):
        if c[i] > c[j]:
            temporary = c[i]
            c[i] = c[j]
            c[j] = temporary

print(c)     '''

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
res = []
i1 = 0
i2 = 0

'''while i1 < len(a) and i2 <len(b):
    if a[i1] <= b[i2]:
        res.append(a[i1])
        i1 = i1 + 1   
    else:
        res.append(i2)
        i2 = i2 + 2
print(res)        '''

print("------------------------------------------------------------")
print("A list contains numbers from 1 to 10, but some numbers are missing.")
numbers = [1, 2, 3, 10]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
min = numbers[0]
for i in numbers:
    if i < min:
        min = i
missing = []        
for num in range(min+1, max) :
    if num not in numbers:
        missing.append(num)
print(missing)        