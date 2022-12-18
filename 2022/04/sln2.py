#!/usr/bin/env python3

with open('input') as fh:
    count = 0
    for line in fh:
        first, second = line.split(',')
        start1, end1 = [int(x) for x in first.split('-')]
        start2, end2 = [int(x) for x in second.split('-')]
        if start1 > end2 or start2 > end1:
            continue
        count += 1
print(count)
