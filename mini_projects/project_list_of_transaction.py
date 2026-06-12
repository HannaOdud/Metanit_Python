print("Given a list of transactions:")
print("Create a report showing each person's final balance:")
print("This combines lists, loops, dictionaries, and aggregation—similar to real-world data processing.")

transactions = [
    ["Alice", 120],
    ["Bob", -50],
    ["Alice", -20],
    ["Charlie", 200],
    ["Bob", 30]
]
dict_transaction = {}
for t in transactions:
    key = t[0]
    value = t[1]
    if key not in dict_transaction.keys():
        dict_transaction[key] = value   
    else:
        dict_transaction[key] = dict_transaction[key] + value
print(dict_transaction)        
