print("Просте число.Перевір, чи є число простим.")

num = int(input("Write the number: "))
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime num")
        break
else: print(f"{num} is a prime num")