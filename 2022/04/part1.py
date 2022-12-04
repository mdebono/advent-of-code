def parse_pair(pair):
    return tuple([int(p) for p in pair.split('-')])

def parse_line(line):
    return tuple([parse_pair(p) for p in line.strip().split(',')])

def contains(small, large):
    return small[0] >= large[0] and small[1] <= large[1]

f = open("2022/04/input.txt")
count = 0
for line in f:
    pairs = parse_line(line)
    fully_contains = contains(pairs[0], pairs[1]) or contains(pairs[1], pairs[0])
    if fully_contains:
        count += 1
    print(pairs, fully_contains)
print(count)