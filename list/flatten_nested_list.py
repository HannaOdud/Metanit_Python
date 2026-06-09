print("Flatten a Nested List. Convert it into a single flat list.")
nested = [[1, 2], [3, 4, 5], [6], [7, 8]]
flat = []
for i in nested:
    flat.extend(i)
print(f"Nested: {nested}")
print(f"Flat: {flat}")