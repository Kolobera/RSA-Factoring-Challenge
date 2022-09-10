lp = []
with open('primes.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        """for j in list(i.split()):"""
        lp.append(int(i))
with open("prime.txt", "w") as file:
    for i in lp:
        file.write(str(i)+",")




