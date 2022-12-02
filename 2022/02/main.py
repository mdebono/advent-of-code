def get1(line):
    return line.split(' ')[0]

def get2(line):
    return line.split(' ')[1]

f= open("2022/02/smallinput.txt")


for line in f:
    line = line.strip()
    print(line)
    print(get1(line), get2(line))
