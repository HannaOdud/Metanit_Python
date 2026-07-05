#1
book = {
    "title": "Harry Potter",
    "author": "J. K. Rowling",
    "year": 1997
}
print(book["author"])

#2
book["pages"] = 320
print(book)

#3 
book["year"] = 1998
print(book)

#4
del book["pages"]
print(book)

#5
print(book.get("publisher", "No such key"))