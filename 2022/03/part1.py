def get_parts(line):
    size = len(line.strip())
    half = size // 2
    return line[0:half], line[half:size]

def get_common(part1, part2):
    for c in part1:
        if c in part2:
            return c

def get_priority(char):
    if ord(char) >= ord('a'):
        return ord(char) - ord('a') + 1
    return ord(char) - ord('A') + 27

f = open("2022/03/input.txt")
sum = 0
for line in f:
    parts = get_parts(line)
    common = get_common(parts[0], parts[1])
    priority = get_priority(common)
    sum = sum + priority
    print(line.strip(), parts, common, priority)
print(sum)