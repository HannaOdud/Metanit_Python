def sec_largest(numbers):
    largest = float("-inf")
    second_largest = float("-inf")
    for n in numbers:
        if n > largest:
            second_largest = largest
            largest = n 
        elif n < largest and n > second_largest:
            second_largest = n
    return second_largest        
print(sec_largest([4,1,2,9,7]))