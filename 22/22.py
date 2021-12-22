import re
from time import time
from tqdm import tqdm

def read_file(file):
    with open(file) as fp:
        inp = fp.read().split("\n")
        inp = list(map(extract, inp))
    return inp


def extract(line):
    regex = r".+([nf]+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)"
    cmd, *groups = re.search(regex, line).groups()
    return cmd == 'n', tuple(map(int, groups))


def part_one(inp):
    cubes = set()

    for cmd, ranges in inp:
        for x in range(max(-50, ranges[0]), min(50, ranges[1])+1):
            for y in range(max(-50, ranges[2]), min(50, ranges[3])+1):
                for z in range(max(-50, ranges[4]), min(50, ranges[5])+1):
                    if cmd:
                        cubes.add((x, y, z))
                    else:
                        cubes.discard((x, y, z))

    return len(cubes)

def overlapping_box(box_a, box_b):
    max_x, max_y, max_z = [max(box_a[i], box_b[i]) for i in (0, 2, 4)]
    min_xp, min_yp, min_zp = [min(box_a[i], box_b[i]) for i in (1, 3, 5)]
    if min_xp - max_x >= 0 and min_yp - max_y >= 0 and min_zp - max_z >= 0:
        return max_x, min_xp, max_y,  min_yp, max_z, min_zp

def part_two(inp):
    total = 0
    counted_zones = []
    for x in list(reversed(inp)):
        try:
            cmd, box = x
        except:
            print(x)

        x1, x2, y1, y2, z1, z2 = box

        if cmd:
            dead_cubes = []
            for overlap_box in [overlapping_box(zone, box) for zone in counted_zones]:
                if overlap_box:
                    dead_cubes.append((True, overlap_box))
            total += (x2-x1+1) * (y2-y1+1) * (z2-z1+1)
            total -= part_two(dead_cubes)
        counted_zones.append(box)
    return total


if __name__ == "__main__":
    # tests = (("test.txt", 39), ("test2.txt", 590784))
    # for test, target in tests:
    #     result = part_one(read_file(test))
    #     print(f"Test {result == target}: {result}")
    # st = time()
    # print(f"Part One {part_one(read_file('input.txt'))} : {time()-st:.4f}")
    st = time()
    print(f"Test Two {part_two(read_file('test3.txt'))} : {time()-st:.4f}")
    st = time()
    print(f"Part Two {part_two(read_file('input.txt'))} : {time()-st:.4f}")
