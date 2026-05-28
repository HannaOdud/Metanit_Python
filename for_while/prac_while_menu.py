print(". Меню. Створи нескінченне меню:")
print("1 - Say Hello")
print("2 - Show number")
print("0 - Exit")
while True:
    
    num = int(input("Choose a number: ")) 
    if num == 0:
        print("Goodbye!")
        break
    if num == 1:
        print("Say Hello")
    elif num == 2:
        print("2")
