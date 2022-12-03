from enum import Enum

class Shape(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'

def tokenize(line):
    array = line.strip().split(' ')
    return array[0], array[1]

def get_shape_score(shape):
    if shape == Shape.ROCK:
        return 1
    if shape == Shape.PAPER:
        return 2
    if shape == Shape.SCISSORS:
        return 3
    raise ValueError

def get_outcome_score(other, you):
    if you == other:
        return 3
    if ((you == Shape.ROCK and other == Shape.SCISSORS)
        or (you == Shape.SCISSORS and other == Shape.PAPER)
        or (you == Shape.PAPER and other == Shape.ROCK)):
        return 6
    return 0

def get_shape_from_outcome(other, outcome):
    if outcome == 'Y': # draw
        return other
    if outcome == 'X': # lose
        if other == Shape.SCISSORS:
            return Shape.PAPER
        if other == Shape.PAPER:
            return Shape.ROCK
        if other == Shape.ROCK:
            return Shape.SCISSORS
    if outcome == 'Z': # win
        if other == Shape.SCISSORS:
            return Shape.ROCK
        if other == Shape.PAPER:
            return Shape.SCISSORS
        if other == Shape.ROCK:
            return Shape.PAPER

def get_score(other, you):
    return get_shape_score(you) + get_outcome_score(other, you)

f = open("2022/02/input.txt")

sum = 0
for line in f:
    line = tokenize(line)
    other = Shape(line[0])
    outcome = line[1]
    you = get_shape_from_outcome(other, outcome)
    score = get_score(other, you)
    print(other, outcome, you, score)
    sum = sum + score
print(sum)