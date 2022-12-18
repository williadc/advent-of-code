#!/usr/bin/env python3
import collections
import re

def move(stacks, count, frm, to):
    stacks[to].extend(list(stacks[frm])[-count:])
    tmp = list(stacks[frm])[0:-count]
    stacks[frm] = collections.deque(tmp)
    return stacks

# Move instructions are "move <count> from <src> to <dest>"
move_re = re.compile(r'^move (\d+) from (\d+) to (\d+)$')

# Stacks are defined as [#] [#] ...
stack_re = re.compile(r'^[A-Z \[\]]+$')
with open('input') as fh:
    stacks = list()
    for line in fh:
        if m := move_re.search(line):
            count, frm, to = m.groups()
            stacks = move(stacks, int(count), int(frm) - 1, int(to) - 1)
        elif m := stack_re.search(line):
            # Stacks are every 4th character with offset of 1
            in_stacks = line[1::4]
            # Initialize stacks based on the number of stacks in input
            if not len(stacks):
                stacks = [collections.deque() for i in range(len(in_stacks))]
            for i, letter in enumerate(in_stacks):
                if letter == ' ':
                    continue
                stacks[i].appendleft(letter)
            in_stacks = ''

for stack in stacks:
    print(stack.pop(), end='')

print()
