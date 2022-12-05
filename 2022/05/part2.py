import re
regex = re.compile(r'\d+')

def parse_stack_line(line):
    line = line.replace('\n','')
    if line == '':
        return line
    line = line[1::4]
    print(line)
    return line

def parse_move_line(line):
    return tuple(int(x) for x in regex.findall(line))

def stack_fill(stacks, line):
    # init stacks
    if stacks == []:
        for x in line:
            stacks.append([])
    # fill stack line
    for i, x in enumerate(line):
        if x >= 'A' and x <= 'Z':
            stacks[i].insert(0, x)

def move(stacks, n, a, b):
    mover = []
    for _ in range(n):
        item = stacks[a-1].pop()
        mover.append(item)
    for _ in range(n):
        item = mover.pop()
        stacks[b-1].append(item)

def tops(stacks):
    return [stack[-1] for stack in stacks]

f = open("2022/05/input.txt")

stack_mode = True
stacks = []
for line in f:
    if (stack_mode):
        line = parse_stack_line(line)
        stack_fill(stacks, line)
        if len(line) == 0:
            stack_mode = False
    else:
        print(stacks)
        params = parse_move_line(line)
        move(stacks, params[0], params[1], params[2])

print(stacks)
print(''.join(tops(stacks)))
