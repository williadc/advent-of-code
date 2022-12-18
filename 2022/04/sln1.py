#!/usr/bin/env python3

with open('input') as fh:
    count = 0
    for line in fh:
        first, second = line.split(',')
        start1, end1 = first.split('-')
        start2, end2 = second.split('-')
        if int(start1) <= int(start2) and int(end1) >= int(end2):
            print(line.strip())
            count += 1
        elif int(start2) <= int(start1) and int(end2) >= int(end1):
            print(line.strip())
            count += 1
print(count)
