

with open("01_inp.txt") as fp:
##with open("01_test.txt") as fp:
    readings = list(map(lambda x: int(x.strip()), fp.readlines()))

increase = 0
for i in range(1, len(readings)):
    if readings[i-1] <= readings[i]:
        increase += 1

print(increase)
