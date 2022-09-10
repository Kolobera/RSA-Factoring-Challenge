lp = []
with open('2T_part1.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        for j in list(i.split()):
            lp.append(int(j))
with open("primes.py", "w") as file:
    file.write("[")
    for i in lp:
        if i < 50000000:
            file.write(str(i)+",")
    file.write("]")



