numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []

for i in numbers:

    if  i % 2 == 0 and i != 2 or i % 3 == 0 and i != 3:
        not_primes.append(i)

    else:
        primes.append(i)
        if i == 1:
            primes.remove(i)


print(primes)
print(not_primes)