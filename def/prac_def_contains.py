print("Створи функцію contains(numbers, target).Поверни True, якщо число є у списку.")
def contains(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return True
    return False
print(contains ([2,5,8,3], 3))
print(contains ([2,5,8,3], 0))