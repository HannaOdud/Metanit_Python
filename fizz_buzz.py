num = int(input("Input the number: "))

if num % 3 == 0 and num % 5 == 0:
    print ("FizzBuzz")
elif num % 3 == 0:
    print(f"Fizz: {num}")
elif num % 5 == 0:
     print(f"Buzz: {num}")
else:print ("No way....):")