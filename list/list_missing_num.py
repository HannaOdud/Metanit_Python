print("A list contains numbers from 1 to 10, but some num are missing.")
print("Find the missing number efficiently")

'''numbers = [1, 2, 3,  10]
max_num = numbers[0]
for i in numbers:
    if max_num < i:
        max_num = i
print(f"Max_num: {max_num}")        
min_num = numbers[0] 
for i in numbers:
    if min_num > i:
        min_num = i
print(f"Min_num: {min_num}")       
missing_num = []    
for num in range(min_num+1, max_num):
    if num not in numbers:
        missing_num.append(num) 
print(f"Missing: {missing_num}")    '''    
print("------------------------------------------------------------")
'''numbers = [1, 2, 3,  10]
missing_num = []
for num in range(1, 10):
    if num not in numbers:
        missing_num.append(num)
print(f"Missing num are: {missing_num}")    '''
print("------------------------------------------------------------")    
numbers = [1, 2, 3,  10]
missing_num = []
for num in range(1, 10):
    if num not in numbers:
        missing_num.append(num)
print(f"Missing num are: {missing_num}") 