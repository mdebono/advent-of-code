def get_common(lines):
    for c in lines[0]:
        if c in lines[1] and c in lines[2]:
            return c

def get_priority(char):
    if ord(char) >= ord('a'):
        return ord(char) - ord('a') + 1
    return ord(char) - ord('A') + 27

f = open("2022/03/input.txt")
sum = 0
count = 0
lines = []
for line in f:
    count = count + 1
    lines.append(line.strip())
    if count == 3:
        common = get_common(lines)
        priority = get_priority(common)
        sum = sum + priority
        print(lines, common, priority)
        count = 0
        lines = []
print(sum)