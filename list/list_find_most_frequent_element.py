'''from collections import Counter
# Counter return list of tuples, where each tuple contains the element and the element count. 
print("Find the Most Frequent Element. Find the element that appears most frequently.")
numbers = [4, 1, 2, 4, 3, 4, 2, 2, 2]
most_freq = Counter(numbers).most_common(2)
print(f"Most Frequent Element: {most_freq}")'''



'''print("Find the Most Frequent Element. Find the element that appears most frequently.")
# key = new_dic.get - знаходить ключ у якого найбільше значенння
numbers = [4, 1, 2, 4, 3, 4, 2, 2, 2]
new_dic = {}
for num in numbers:
    if num not in new_dic.keys():
        new_dic[num] = 1
    else:
        new_dic[num] = new_dic[num] + 1
print(new_dic)
max_v = max(new_dic, key = new_dic.get) 
print(max_v)'''


print("Test exercise for finding: max_v / max_k ")

new_dic = {
    4: 3,
    1: 1,
    2: 4,
    3: 1
}
max_k = None
max_v = 0
for key in new_dic:
    if new_dic[key] > max_v:
        max_v = new_dic[key]
        max_k = key
print(f"Max_key: {max_k}")
print(f"Max_val: {max_v}")

