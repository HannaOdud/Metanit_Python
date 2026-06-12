print("Given a list of integers, find the largest absolute difference between any two numbers.")

numbers = [8, 3, 15, 1, 9]
largest_diff = 0
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        diff = abs(numbers[i] - numbers[j])
        if diff > largest_diff:
            largest_diff = diff
print(f"Largest difference: {largest_diff}")            