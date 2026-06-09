print("Find All Pairs With Target Sum")
print("Find all unique pairs whose sum equals the target.")
numbers = [2, 4, 3, 5, 7, 8, 9]
target = 10

'''res = []

for i in range(len(numbers)):  
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            res.append((numbers[i], numbers[j]))   
print(res)  '''     



def find_pairs(numbers, target):
    res = []
    while numbers:
        num = numbers.pop()
        diff = target - num
        if diff in numbers:
            res.append((diff, num))
           
    return res
    
numbers = [2, 4, 3, 5, 7, 8, 9]
target = 10
print(find_pairs(numbers, target))