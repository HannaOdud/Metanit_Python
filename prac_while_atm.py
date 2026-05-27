print("На рахунку є 1000. Користувач вводить суму зняття. Поки гроші є — дозволяти знімати. Якщо недостатньо коштів:")
limit = 1000
while True:
    order = int(input("Write your amount of cash: "))
    if limit >= order:
        limit = limit - order
    else: 
        print("Not enough money") 
        break
print(f"Your limit now: {limit}")    
