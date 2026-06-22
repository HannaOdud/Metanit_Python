#Python Lists Practice (Additional 20 Tasks)

'''print("1. Weekend Plans. Create a list of three weekend activities.Add one more activity to the end. Print the updated list. ") activities = ["basketball", "football", "tennis"]
activities.append("swimming pool")
print(activities)'''

'''print("2. Favorite Numbers. Create a list of five numbers. Insert the number 100 at the beginning of the list.  ")
num = [1, 2, 3, 4, 5]
num.insert(0, 100)
print(num)'''

'''print("3. Merge Guest Lists. Combine both guest lists using extend(). ")
guests1 = ["Alice", "Bob"]
guests2 = ["Charlie", "Diana"]
guests1.extend(guests2)
print(guests1)'''

'''print("4. Remove a Cancelled Order. Remove only the first 'Burger'. ")
orders = ["Pizza", "Burger", "Pasta", "Burger"]
orders.remove("Burger")  #remove() - remove first occurrence
print(orders)'''

'''print("5. Last Student Leaves. Remove the last student using pop(). Print the removed student's name. ")
students = ["Tom", "Anna", "Kate", "John"]
last = students.pop(-1)
print(last)'''

'''print("6. Remove by Position. Remove 'March' using its index with pop(). ")
months = ["January", "February", "March", "April"]
ind = months.index("March")
print(ind)
months.pop(ind)
print(months)'''
        #OR
'''months = ["January", "February", "March", "April"]
months.pop(months.index("March"))
print(months)'''

'''print("7. Find the index of 'C++'.")
books = ["Python", "Java", "C++", "JavaScript"]
ind = books.index("C++")
print(ind)'''

'''print("8. Count how many 'Yes' votes there are.")
votes = ["Yes", "No", "Yes", "Yes", "No"]
y = votes.count("Yes")
n = votes.count("No")
print(f"Yes: {y}")
print(f"No: {n}")'''

'''print("9. Sort the ages in ascending order.")
ages = [18, 21, 19, 25, 20]
ages.sort()
print(ages)'''

'''print("10. Reverse the queue.")
queue = ["Person1", "Person2", "Person3", "Person4"]
queue.sort(reverse=True)
print(queue)'''

'''print("11. Create a list of five cities. Make a copy of the list. Add another city to the copied list. Print both lists.")
cities = ["Glasgow", "Edinburgh", "Perth", "Dundee", "Inverness"]
cities_copy = cities.copy()
print(cities)
print(cities_copy)
cities_copy.append("Largs") 
print(cities)
print(cities_copy)'''

'''print("12. Empty the Basket. Remove all items using clear(). Check the length of the list. ")
basket = ["Milk", "Eggs", "Bread", "Cheese"]
basket.clear()
print(basket)
l = len(basket)
print(l)'''

'''print("13. Find the Highest and Lowest Temperature")
temperatures = [12, 18, 7, 21, 15]
high = max(temperatures)
low = min(temperatures)
print(high)
print(low)'''

print("14. Keep the Original List. Create a new sorted list using sorted(). ")