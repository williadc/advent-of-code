#!/usr/bin/env python3

with open('input') as fh:
    biggest = (0, 0, 0)
    tmpsum = 0
    for line in fh:
        if line == '\n':
            biggest = sorted([*biggest, tmpsum], reverse=True)[0:3]
            tmpsum = 0
        else:
            tmpsum += int(line)
print(biggest)
print(sum(biggest))
