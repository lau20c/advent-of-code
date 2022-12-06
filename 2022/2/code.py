import csv

"""
Rock > Scissors
Scissors > Paper
Paper > Rock

Column 0: Opponent's move
- A: Rock
- B: Paper
- C: Scissors

Column 1: My move
- X: Rock
- Y: Paper
- Z: Scissors

Points:
- Outcome + Play
- Outcome: {Lost: 0; Draw: 3; Win: 6}
- Play: {Rock: 1; Paper: 2; Scissors: 3}

Column 1: Ending Requirement
- X: Lose
- Y: Draw
- Z: Win
"""

outcomes = {
    'CX' : 6,
    'BZ' : 6,
    'AY' : 6,
    'AX' : 3,
    'BY' : 3,
    'CZ' : 3}
plays = {'X' : 1, 'Y' : 2, 'Z' : 3}
ending = {'X' : 'Lose', 'Y': 'Draw', 'Z': 'Win'}
counter = {
    'Win': {'A':'Y', 'B':'Z', 'C':'X'}, 
    'Lose': {'A':'Z', 'B':'X', 'C':'Y'},
    'Draw': {'A':'X', 'B':'Y', 'C':'Z'}}

total1, total2 = 0, 0
with open('input.csv', newline='') as input:
    csv_reader = csv.reader(input, delimiter=' ')
    for row in csv_reader:
        # Part 1
        round = ''.join(row)
        outcome_points = outcomes[round] if round in outcomes.keys() else 0
        play_points = plays[row[1]]
        total1 += outcome_points + play_points
        # Part 2
        opp_play = row[0]
        end = ending[row[1]]
        my_play = counter[end][opp_play]
        round_2 = opp_play + my_play
        outcome_points_2 = outcomes[round_2] if round_2 in outcomes.keys() else 0
        play_points_2 = plays[my_play]
        total2 += outcome_points_2 + play_points_2

print(f"Part one: {total1}")
print(f"Part two: {total2}")