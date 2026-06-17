print("1. Create a copy of the list using copy().  Add 20 to the copied list only. Print both lists")
'''numbers = [5, 10, 15]
new_l = numbers.copy()
new_l.append(20) 
print(f"New: {new_l}")
print(numbers)

new_2 = new_l[:]
new_2.append(25)
print(new_2)'''

'''print("2. Find the Second Occurrence")
print("Use index() with the start parameter to find the second occurrence of b")
letters = ["a", "b", "c", "b", "d"]
first = letters.index("b")
second = letters.index("b", first + 1)
print(letters[:second])
print(first)
print(second) ''' 

'''print("3. Sort in Descending Order")
scores = [82, 95, 71, 88, 90]
scores.sort(reverse=True)
print(scores)'''


print("4. Sort the words by their length using the key parameter.")
words = ["elephant", "cat", "giraffe", "dog", "lion"]
words.sort(key = len)
print(words)