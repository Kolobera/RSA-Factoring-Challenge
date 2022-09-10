lp = []
with open("prime.txt", 'r') as file:
        for line in file:
            lp=line[:-1].split(",")
            break
"""with open('primes.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        #for j in list(i.split()):
        lp.append(int(i))
with open("prime.txt", "w") as file:
    for i in lp:
        file.write(str(i)+",")"""
for i in range(10):
    print(lp[-i])



