print("Longest Increasing Subsequence (Advanced)")
print("Find the length of the Longest Increasing Subsequence (LIS).")
print("One valid subsequence: ")

numbers = [10, 22, 9, 33, 21, 50, 41, 60]
new_list = [numbers[0]]

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        new_list.append(numbers[i])
print(new_list)
print(len(new_list))
