import sys
import math



# check for number on command line
if (len(sys.argv) == 1):
    number = input('Please type a number and I will tell you if it is prime: ')
    number = int(number)

if (len(sys.argv) == 2):
    number = sys.argv[1]
    number = int(number)

if number == 1:
    print(f'{number} is a composite number')
elif number == 0:
    print(f'{number} is neither prime nor composite')
else:
    # instantiate a list of the base prime numbers
    base_primes = [2, 3, 5, 7]

    # we assume that the number is prime
    switch = True

    # find the modulus for each base prime
    # if the modulus is 0 when dividing by any of the baseprimes, 
    # the number not prime
    for prime in base_primes:
        if number % prime == 0:
            switch = False

    # check to see if the number is one of the base prime numbers
    # If it is, change the switch back to True        
    for prime in base_primes:
        if number == prime:
            switch = True

    if switch == True:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is a composite number')


