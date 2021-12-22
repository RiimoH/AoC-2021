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
                        cubes.discard((x,y,z))
    
    return len(cubes)
    

def part_two(inp):
    total = 0
    ons = []
    offs = []
    
    for cmd, ranges in inp:
        if cmd:
            ons.append(ranges)
        else:
            offs.append(ranges)
    
    print(ons)
    print(offs)
    
    for ranges in tqdm(ons):
        for x in range(ranges[0], ranges[1]+1):
            for y in range(ranges[2], ranges[3]+1):
                
                for off_ranges in offs:
                    if not((off_ranges[0] < ranges[0] < off_ranges[1] or off_ranges[0] < ranges[1] < off_ranges[1]) and (off_ranges[2] < ranges[2] < off_ranges[3] or off_ranges[2] < ranges[3] < off_ranges[2]) and (off_ranges[4] < ranges[4] < off_ranges[5] or off_ranges[4] < ranges[5] < off_ranges[5])):
                        break
                else:
                    
                    cubes = {(x, y, z)  for z in range(ranges[4], ranges[5]+1)}
                    for off_ranges in offs:
                        for x in range(max(off_ranges[0], ranges[0]), min(off_ranges[1], ranges[1])+1):
                            for y in range(max(off_ranges[2], ranges[2]), min(off_ranges[3], ranges[3])+1):
                                for z in range(max(off_ranges[4], ranges[4]), min(off_ranges[5], ranges[5])+1):
                                    cubes.discard((x, y, z))
                        
                    total += len(cubes)
    
    return total


if __name__ == "__main__":
    tests = (("test.txt", 39), ("test2.txt", 590784))
    for test, target in tests:
        result = part_one(read_file(test))
        print(f"Test {result == target}: {result}")
    st = time()
    print(f"Part One {part_one(read_file('input.txt'))} : {time()-st:.4f}")
    st = time()
    print(f"Test Two {part_two(read_file('test3.txt'))} : {time()-st:.4f}")