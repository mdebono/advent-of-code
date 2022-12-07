def is_marker(quartet):
    dict = {}
    for x in quartet:
        if dict.get(x):
            dict[x] += 1
            if dict[x] > 1:
                return False
        else:
            dict[x] = 1
    return True

def process(line):
    line = line.strip()
    print(line)
    for i, x in enumerate(line[3:]):
        quartet = line[i:i+4]
        #print(i, i+3, quartet)
        if is_marker(quartet):
            return i+4

f = open("2022/06/input.txt")
for line in f:
    print(process(line))
