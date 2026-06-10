print("Write a function that takes an array of strings and returns the longest string prefix that is common to all the strings in the array. ")
print("For example, an input of  [carpet, car, carrier] would return car as the result.")

def longest_prefix(list_str):
    shortest_word_len = len(list_str[0])
    for i in range(1, len(list_str)):
        if len(list_str[i]) < shortest_word_len:
            shortest_word_len = len(list_str[i])
    res = ""
    for i in range(shortest_word_len):
        char = list_str[0][i]
        is_difference_detected = False
        for j in range (1, len(list_str)):
            if char != list_str[j][i]:
                is_difference_detected = True
                break
        if is_difference_detected == True:
            break
        else:
            res = res + char
    return res    
print(longest_prefix(["carpet,", "car", "carrier"]) )   




    










