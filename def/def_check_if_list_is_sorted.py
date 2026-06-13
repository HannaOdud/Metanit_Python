print("Check if a List is Sorted")
print("Write a function that returns True if a list is sorted in ascending order, otherwise False.")

def check (numbers):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return False
    return True
print(check([1, 2, 3, 5]))
print(check([1, 3, 2, 5]))