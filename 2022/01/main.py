f = open("2022/01/input.txt", "r")

sum = 0
largest = 0

for line in f:
    line = line.strip()
    if (line == ''):
        if sum > largest:
            largest = sum
            print('largest = ', largest)
        sum = 0
    else:
        x = int(line)
        sum = sum + x

if sum > largest:
    largest = sum

print('final largest = ', largest)
