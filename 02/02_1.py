

with open("02_inp.txt") as fp:
##with open("01_test.txt") as fp:
    inp = list(map(lambda x: x.strip(), fp.readlines()))

position = 0
aim = 0
depth = 0

for instr in inp:
    cmd, value = instr.split()
    value = int(value)

    if cmd == "forward":
        position += value
        depth += aim * value
    elif cmd == "down":
        aim += value
    elif cmd == "up":
        aim -= value
    else:
        print("error", cmd, value)

print(position * depth)
