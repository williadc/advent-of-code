#!/usr/bin/env python3

def score(p1, p2):
    base = {
            'X': 1,
            'Y': 2,
            'Z': 3,
            }[p2]
    
    opp = {
            'A': 1,
            'B': 2,
            'C': 3,
            }[p1]

    # Draw
    if opp == base:
        return base + 3

    diff = base - opp
    # Victory (-2 => won with Rock over Scissors)
    if diff == 1 or diff == -2:
        return base + 6

    # Loss (2 => loss with Scissors to Rock)
    if diff == -1 or diff == 2:
        return base


with open('input') as fh:
    total_score = 0
    for line in fh:
        total_score += score(*line.split())
print(total_score)
