from math import sqrt,ceil

n = int(input('please enter a number: '))

for i in range(2, ceil(sqrt(n))):

    if n % i == 0:
        print('not prime, can be divisible by :', i)
        break
else:
    print('prime number')
