#!/usr/bin/env python3

def score(p1, outcome):
    opp = {
            'A': 1,
            'B': 2,
            'C': 3,
            }[p1]

    # Draw
    if outcome == 'Y':
        return opp + 3

    # Win
    if outcome == 'Z':
        # Opponent chose Scissors, so return Rock victory
        if opp == 3:
            return 7
        # Final score is opponent value + 1 + 6
        return opp + 7

    # Lose
    if outcome == 'X':
        # Opponent chose Rock, so return Scissors loss
        if opp == 1:
            return 3
        # Final score is opponent value - 1
        return opp - 1

with open('input') as fh:
    total_score = 0
    for line in fh:
        total_score += score(*line.split())
print(total_score)
