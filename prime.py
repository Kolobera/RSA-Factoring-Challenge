#!/usr/bin/python3
lp = []
with open("primes.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            lp.append(int(line))
def check(n):
    for i in lp:
        if n % i == 0:
            return False
    return True
def factor(n):
    for i in lp:
        if n % int(i) == 0:
            return int(i)
<<<<<<< HEAD
    #lpi = [i for i in range (100001, int(n ** .5)+1) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0]
    for i in range (10000001, int(n ** .5)+1):
        if n % i == 0:
            return i
=======
    """lpi = [i for i in range (100001, int(n ** .5)+1,2) if check(i)]"""
    for i in range (1000001, int(n ** .5) + 1, 2):
        if n % i == 0:
            return i
        
>>>>>>> 26ca85b57e7b7cf2ff86897d96a5a4a86aef13af
def primef(n):
    if n <= 3:
        return int(n)
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    else:
        for i in range(5, int((n)**0.5) + 1, 6):
            if n % i == 0:
                return int(i)
            if n % (i + 2) == 0:
                return primef(n/(i+2))
    return int(n)
