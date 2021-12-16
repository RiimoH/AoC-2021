from collections import Counter, defaultdict

def read_file(txt):
    with open(txt) as fp:
        inp = fp.read()
    
    origin, instructions = inp.split("\n\n")
    instr = {}
    for i in instructions.split("\n"):
        k, v = i.split(" -> ")
        instr[k] = v
    return origin, instr

def part_one(txt, steps):
    origin, instr = read_file(txt)
    
    for _ in range(steps):
        new = ""
        for idx in range(len(origin)):
            new += origin[idx]
            if origin[idx:idx+2] in instr:
                new += instr[origin[idx:idx+2]]
        origin = new
    
    c = Counter(origin)
    values = c.values()
    return max(values) - min(values)

def part_two(txt, steps):
    origin, instr = read_file(txt)

    p = Counter([a+b for a,b in zip(origin, origin[1:])])
    
    for _ in range(steps):
        np = defaultdict(int)
        
        for pair, count in p.items():
            for new_pair in [pair[0]+instr[pair], instr[pair]+pair[1]]:
                np[new_pair] += count
        p = np
    
    count = []
    for char in set(''.join(p.keys())):
        c = max(sum(v for k, v in p.items() if k[0] == char), sum(v for k, v in p.items() if k[1] == char))
        count.append(c)
    return max(count) - min(count)
    
    

        
if __name__ == "__main__":
    print("Test Sol 2:", part_one("test.txt", 10))
    print("Test Sol 2:", part_two("test.txt", 10))
    print("Sol Part 1:", part_two("input.txt", 10))
    print("Sol Part 2:", part_two("input.txt", 40))
    