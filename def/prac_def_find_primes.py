"""print("Створи функцію: яка повертає всі прості числа до limit. ")
def find_primes(limit):
    for i in range(2,limit):
        if limit % i == 0:
            print(f"{limit}: is not prime ")
            break
    print(f" {limit} is a prime" )

find_primes(4)   """

def find_primes(limit):
    primes = []

    for num in range(2, limit + 1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes


print(find_primes(20))