print("Створи функцію: яка повертає один список без повторень. ")

def merge_lists(list1, list2):
    res = []
    for i in list1:
        if i not in res:
            res.append(i)
    for i in list2:
        if i not in res:
            res.append(i)         
    return res      
print(merge_lists([1,1,2,2,3,4,5,5], [6,7,7,8,9,9]))  