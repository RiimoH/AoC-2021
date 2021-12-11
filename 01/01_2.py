

with open("01_inp.txt") as fp:
#with open("01_test.txt") as fp:
    readings = list(map(lambda x: int(x.strip()), fp.readlines()))

windows = []
for i in range(len(readings) -2):
    windows.append(readings[i]+readings[i+1]+readings[i+2])

print()

increases = 0
last = 10_000_000
for w in windows:
    if w > last:
        increases += 1

    last = w

print(increases)
