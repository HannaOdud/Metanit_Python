print("Python Lists Practice")

'''numbers = [10, 20, 40, 50]
numbers.insert(2, 30)
print(numbers)'''


'''list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)'''

'''animals = ["cat", "dog", "rabbit", "dog"]
animals.remove("dog")
print(animals)
animals.clear()
print(animals)'''

'''letters = ["A", "B", "C", "D"]
p = letters [len(letters)-1]
print(p)
print(letters[-1])'''


'''numbers = [5, 10, 15, 20]
n = numbers.pop(2)
print(numbers)
print(n)'''

'''nums = [2, 5, 2, 8, 2, 10]
counter = 0
for n in nums:
    if n == 2:
        counter = counter + 1
print(counter) 
print(len(nums))'''

'''numbers = [8, 3, 12, 1, 5]
numbers.sort()
print(numbers)'''

'''days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
days.reverse()
print(days)'''

'''original = [1, 2, 3]
o = original.copy()
print(o)
o.append(4)
print(o)'''

'''scores = [78, 91, 65, 84, 99]
mn = min(scores) 
mx = max(scores)
print(mn)
print(mx)'''

'''numbers = [9, 4, 7, 1]
n_l = sorted(numbers)
print(numbers)
print(n_l)'''

'''cities = ["Paris", "London", "Tokyo", "Berlin"]
c = sorted(cities)
print(c)'''

'''ls = []
ls.append(1)
ls.append(2) 
ls.append(3)
print(ls)
ls.insert(0, 0)
print(ls)
ls.pop(-1)
print(ls)'''

'''shop_ls = ["eggs", "milk", "butter", "bread", "tea"]
shop_ls.append("sugar")
shop_ls.remove("tea")
print(f" Len: {len(shop_ls)}")
ind = shop_ls.index("sugar")
print(f"Index of sugar: {ind}")
print(shop_ls)'''

'''names = ["Tom", "Anna", "Tom", "Kate", "Tom"]
for i in range(len(names)):
    if names[i] == "Tom":
        names.pop(i)
        break
print(names)'''


'''names = ["Tom", "Anna", "Tom", "Kate", "Tom"]
t = names.index("Tom")
print(t)
r = names.pop(0)
print(names)
t2 = names.remove("Tom")
print(names)
i = names.index("Tom")
print(i)
del names[2]
print(names)'''

'''numbers = [15, 7, 22, 7, 9]
numbers.append(30)
print(numbers)
numbers.insert(2, 100)
print(numbers)
numbers.remove(7)
print(numbers)
c = numbers.count(7)
print(c)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(max(numbers))
print(len(numbers))'''


data = [5, 12, 7]
data.append(20)
print(data)
data.insert(0, 1)
print(data)
data.extend([30, 40])
print(data)
data.remove(12)
print(data)
r_s = data.pop(len(data)-1)
print(r_s)
print(data)
s_data = sorted(data)
print(s_data)
print(data)
print(len(data))
print(f"Max: {max(data)} Min: {min(data)}")