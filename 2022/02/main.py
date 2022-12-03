def tokenize(line):
    array = line.strip().split(' ')
    return array[0], array[1]

def shape(shape):
    if shape in ['A', 'X']:
        return 1
    if shape in ['B', 'Y']:
        return 2
    if shape in ['C', 'Z']:
        return 3
    raise ValueError

def outcome(other, you):
    if shape(you) == shape(other):
        return 3
    if ((shape(you) == 1 and shape(other) == 3) # Rock defeats Scissors
        or (shape(you) == 3 and shape(other) == 2) # Scissors defeats Paper
        or (shape(you) == 2 and shape(other) == 1)): # Paper defeats Rock
        return 6
    return 0

def get_score(other, you):
    return shape(you) + outcome(other, you)

f = open("2022/02/input.txt")

sum = 0
for line in f:
    line = tokenize(line)
    other = line[0]
    you = line[1]
    score = get_score(other, you)
    print(other, you, score)
    sum = sum + score
print(sum)