print("Compress Consecutive Duplicates")
'''letters = ["a","a","a","b","b","c","a","a"]
res = []
for i in range(0, len(letters)-1):
    if letters[i] != letters[i + 1]:
        res.append(letters[i])
res.append(letters[len(letters)-1])
print(res)'''  

letters = ["a","a","a","b","b","c","a","a"]  
res = [] 
res.append(letters[0])
for i in range(1, len(letters)):
    if letters[i] != letters[i-1]:
        res.append(letters[i])    
print(res)           

