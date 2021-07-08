# Primality test
import math

def is_prime(number):
    if number == 2:
        return True
    elif number < 2 or number %2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

def run():
    # number = int(input('Select a number: '))
    primes = range(1000)
    for number in primes:
        if is_prime(number):
            print('It is prime: ' + str(number))
        else:
            print('It is not prime: ' + str(number))


if __name__ == '__main__':
    run()