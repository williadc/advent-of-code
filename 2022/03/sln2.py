#!/usr/bin/env python3

with open('input') as fh:
    sum = 0
    line_count = 0
    common = set()
    for line in fh:
        line_count += 1
        letters = set(list(line.strip()))

        # For the first line in the trio, populate common
        if common:
            common = common.intersection(letters)
        else:
            common = letters

        # Only increment the sum every third line
        if line_count % 3:
            continue

        if len(common) != 1:
            print(f'Error: long common {common}')
            continue
        char = list(common)[0]
        # Value of capital letters is 38 less than the ASCII value
        if char.isupper():
            delta = 38
        # Value of lower-case letters is 96 less than the ASCII value
        else:
            delta = 96
        sum += ord(char) - delta
        common = set()

print(sum)
