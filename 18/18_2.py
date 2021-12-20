from time import time
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


def magnitude(depths, values):
    for d in [3, 2, 1, 0]:
        while d in depths:
            idx = depths.index(d)
            values = values[:idx] + [values[idx] *
                                     3+values[idx+1]*2] + values[idx+2:]
            depths = depths[:idx] + [d-1] + depths[idx+2:]

    return values[0]


if __name__ == "__main__":
    lines = list(map(parse, read_file("test.txt")))

    max_mag = 0
    st = time()
    for l1 in lines:
        for l2 in lines:
        
            d, v = add(*l1, *l2)
            d, v = reduce(d, v)
            max_mag = max(max_mag, magnitude(d, v))
    print(max_mag)
    print(time()-st)
    
    lines = list(map(parse, read_file("input.txt")))

    max_mag = 0
    st = time()
    for l1 in lines:
        for l2 in lines:
        
            d, v = add(*l1, *l2)
            d, v = reduce(d, v)
            max_mag = max(max_mag, magnitude(d, v))
    print(max_mag)
    print(time()-st)