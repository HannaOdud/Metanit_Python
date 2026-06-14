print("Rotate a list to the left by k positions.")

numbers = [1,2,3,4,5]
k = 2

before_k = numbers[:k]
after_k = numbers[k:]
print(before_k)
print(after_k)
res = after_k + before_k
print(res)