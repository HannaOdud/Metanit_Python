'''print("Creating list()")
numbers1 = []
numbers2 = list()
numbers3 = [1, 2.6, "Hello", True]
letters = list("hello")
numbers4 = [5] * 6

print(numbers1)
print(numbers2)
print(numbers3)
print(letters)
print(numbers4)'''

print("-----*------*------*-------*------")
people = ["Tom", "Sam", "Bob"]
print(people[0])
print(people[-1])
print(people[-2])

people[1] = "Mike"
print(people[1])

for person in people:
    print(person)

print("-----*------*------*-------*------")

people = ["Tom", "Sam", "Bob"]
i = 0
while i<len(people):
    print(people[i])
    i += 1

print("-----*------*------*-------*------")

numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4, 5])
if numbers1 == numbers2:
    print("numbers1 equal to numbers2")
else:
    print("numbers1 is not equal to numbers2")

print("-----*------*------*-------*------")

people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]

slice_people1 = people[:3]
print(slice_people1)