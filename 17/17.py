from time import time
import re


def read_file(txt):
    with open(txt) as fp:
        # target area: x=20..30, y=-10..-5
        regex = r".+x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)"
        inp = tuple(map(int, re.search(regex, fp.read()).groups()))
    return inp


def part_one(ymin):
    return sum([x for x in range(abs(ymin))])


def part_two(xmin, xmax, ymin, ymax):
    sol = set()
    for x in range(xmax + 1):
        for y in range(ymin*2, -ymin*2):
            ix = x - 1
            iy = y - 1

            posx = x
            posy = y

            while posx <= xmax and posy >= ymin:
                if xmin <= posx <= xmax and ymin <= posy <= ymax:
                    sol.add((x, y))
                    break

                posx += ix
                ix -= 1 if ix > 0 else 0

                posy += iy
                iy -= 1

    return sol


if __name__ == "__main__":
    inp = (xmin, xmax, ymin, ymax) = read_file("test.txt")
    print("Test One:", part_one(ymin) == 45)
    print("Test Two:", len(part_two(*inp)) == 112)

    inp = (xmin, xmax, ymin, ymax) = read_file("input.txt")
    print("Test One:", part_one(ymin))
    print("Test Two:", len(part_two(*inp)))
