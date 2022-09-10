#!/usr/bin/python3
lp = []
with open("prime.txt", 'r') as file:
        """for line in file:
            lp.append(int(line[:-1]))"""
        lp = [int(line[:-1]) for line in file]
def check(n):
    for i in lp:
        if n % i == 0:
            return False
    return True
def factor(n):
    for i in lp:
        if n % int(i) == 0:
            return int(i)
    #lpi = [i for i in range (100001, int(n ** .5)+1) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0]
<<<<<<< HEAD
    for i in range (100000001, int(n ** .5)+1,2):
=======
    for i in range (1000000001, int(n ** .5)+1,2):
>>>>>>> f68cdb5ef6b40e6a858a4b745cbea3d8089c8ba6
        if n % i == 0:
            return i
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
