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

def get_marker(line, diff_num, start):
    for i, x in enumerate(line[diff_num-1:]):
        quartet = line[start+i:start+i+diff_num]
        #print(start+i, start+i+diff_num, quartet)
        if is_marker(quartet):
            return start+i+diff_num

f = open("2022/06/input.txt")
for line in f:
    line = line.strip()
    print("line:", line)
    packet_marker = get_marker(line, 4, 0)
    print("packet marker:", packet_marker)
    message_marker = get_marker(line, 14, 0)
    print("message marker:", message_marker)

