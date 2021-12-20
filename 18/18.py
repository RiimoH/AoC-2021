def read_file(txt):
    with open(txt) as fp:
        inp = fp.read().split("\n")
    return inp

def parse(line):
    depth = []
    values = []
    level = -1

    for char in line:
        if char == "[":
            level += 1
        elif char == "]":
            level -= 1
        elif char == ",":
            continue
        else:
            values.append(int(char))
            depth.append(level)

    return depth, values

def explode(depth, values):
    if 4 in depth:
        idx = depth.index(4)
        if idx == 0:
            values = [0, values[1] + values[2]] + values[3:]
            depth = [3, depth[2]] + depth[3:]
        elif idx == len(depth) - 2:
            values = values[:idx-1] + [values[idx-1] + values[idx], 0]
            depth = depth[:idx-1] + [depth[idx-1]] * 2
        else:
            values = values[:idx-1] + [values[idx-1] + values[idx],
                                       0, values[idx+1] + values[idx+2]] + values[idx+3:]
            depth = depth[:idx] + [3] + depth[idx+2:]
        return True, depth, values
    else:
        return False, depth, values

def split(depth, values):
    for idx, val in enumerate(values):
        if val >= 10:
            break
    else:
        return False, depth, values

    l = val // 2
    r = val - l

    depth = depth[:idx] + [depth[idx]+1] * 2 + depth[idx+1:]
    values = values[:idx] + [l, r] + values[idx+1:]

    return True, depth, values


def add(depth1, value1, depth2, value2):
    depth = list(map(lambda x: x+1, depth1 + depth2))
    value = value1 + value2
    return depth, value

def reduce(depth, values):
    b = True
    while b:
        while b:
            b, depth, values = explode(depth, values)
        b, depth, values = split(depth, values)

    return depth, values

def magnitude(depth, values):
    
    pass

if __name__ == "__main__":
    tests = ["""[[[[4,3],4],4],[7,[[8,4],9]]]
[1,1]""",
"""[1,1]
[2,2]
[3,3]
[4,4]""",
"""[1,1]
[2,2]
[3,3]
[4,4]
[5,5]""",
"""[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]""",
"""[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]""",]

    for tn, test in enumerate(tests):
        print("\n\n", tn)
        lines = test.split("\n")
        d, v = parse(lines[0])

        for line in lines[1:]:
            d, v = add(d, v, *parse(line))
            d, v = reduce(d, v)
        print(d, v)
