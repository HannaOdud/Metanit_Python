print("Write your own Bubble Sort function that sorts a list in ascending order.")

'''num = [5, 1, 4, 2, 8] 
num.sort()
print (num)'''


num_list = [5, 1, 4, 2, 8]
for i in range(len(num_list)-1):
    temporary = 0
    for j in range(i+1,len(num_list)):
        if num_list[j] < num_list[i]:
            temporary = num_list[i]
            num_list[i] = num_list[j]
            num_list[j] = temporary
print(num_list)

