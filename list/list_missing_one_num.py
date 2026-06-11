print("A list contains numbers from 1 to 100, but one number is missing.")
print("Find the missing number efficiently.")

numbers = [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,  20]

expected_sum = sum(range(1, 21))
real_sum = sum(numbers)
missing_num = expected_sum - real_sum
print(missing_num)