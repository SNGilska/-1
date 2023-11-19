number = int(input())
def is_prime(is_number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime:
        print("Простое!")
    else:
        print("Сложное!")

is_prime(number)