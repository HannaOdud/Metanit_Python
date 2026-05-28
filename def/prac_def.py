'''def print_person(name ="Tom", age = 18):
    print(f"Name: {name} Age: {age}")
print_person()
print_person("Bob")
print_person("Sam", 37)  '''

def sum(*numbers):
    result = 0
    for i in numbers:
        result += i
    print(f"Sum = {result}")    
sum(1, 2, 3, 4, 5)   
sum(3, 4, 5, 6) 