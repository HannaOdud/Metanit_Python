print("Find the Longest Word")
print("Sort the list by word length.")
words = ["cat", "elephant", "dog", "horse"]
w = sorted(words, key = len)

print(w)
words = ["cat", "elephant", "dog", "horse"]
def sort_l(s):
    ww = sorted(s, key = len )
    return ww    
print (sort_l(words))