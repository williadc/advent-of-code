#!/usr/bin/env python3

with open('input') as fh:
    sum = 0
    for line in fh:
        letters = list(line.strip())
        half = len(letters) // 2
        h1 = letters[:half]
        h2 = letters[half:]
        if len(h1) != half or len(h2) != half:
            print(f'Bad line: {letters}, {len(h1)}, {len(h2)}, {half}')
            continue
        common = set(h1).intersection(set(h2))
        if len(common) != 1:
            print(f'Bad common: {line}\n\t{common}')
            continue
        char = list(common)[0]
        # Value of capital letters is 38 less than the ASCII value
        if char.isupper():
            delta = 38
        # Value of lower-case letters is 96 less than the ASCII value
        else:
            delta = 96
        sum += ord(char) - delta

print(sum)
