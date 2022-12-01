f = open("2022/01/input.txt", "r")

sum = 0
largest = 0
list = []

for line in f:
    line = line.strip()
    if (line == ''):
        if sum > largest:
            largest = sum
            print('largest =', largest)
        list.append(sum)
        sum = 0
    else:
        x = int(line)
        sum = sum + x

if sum > largest:
    largest = sum
list.append(sum)

print('final largest =', largest)

list.sort(reverse=True)
print(list[0:3])
total = list[0] + list[1] + list[2]
print('total =', total)
