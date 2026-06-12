print("Move all zeros to the end while keeping the order of the other elements.")

numbers = [0, 4, 0, 2, 5, 0, 1]
new_num = []
zeros = []
for n in numbers:
    if n == 0:
        zeros.append(n)
    else:
        new_num.append(n)  
new_num.extend(zeros)
print(new_num)

     