#!/usr/bin/python3
import sys
from prime import factor, primef

if __name__ == "__main__":
    lp = []
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
        for line in lines:
            lp.append(int(line))
    for i in lp:
        j = factor(i)
        print("{}={:d}*{}".format(i,int(i/j),j))

