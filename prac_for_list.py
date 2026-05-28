print("Пошук найбільшого числа. Знайди найбільше число без max().:")

numbers = [3, 7, 2, 9, 5]
max_num = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]
print(max_num)

print("Знайди середнє значення списку чисел.")
numbers = [3, 7, 2, 9, 5]
tot = 0
for i in range(len(numbers)):
    tot = tot + numbers[i]
avg = tot / len(numbers)
print(f"Avg: {avg}")