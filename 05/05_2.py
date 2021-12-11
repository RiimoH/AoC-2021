from collections import defaultdict

if __name__ == "__main__":
    with open("input.txt") as fp:
        inp = fp.read().split('\n')

    grid = defaultdict(int)
    #grid = [[0 for x in range(10)] for y in range(10)]

    for line in inp:
        start, end = line.split(' -> ')
        sx, sy = map(int, start.split(','))
        ex, ey = map(int, end.split(','))


        if (sx == ex):
            for iy in range(min(sy, ey), max(sy, ey)+1):
                grid[(sx, iy)] += 1
        elif (sy == ey):
            for ix in range(min(sx, ex), max(sx, ex)+1):
                grid[(ix, sy)] += 1
        else:
            if sx > ex:
                x_values = range(sx, ex-1, -1)
            else:
                x_values = range(sx, ex +1)

            if sy > ey:
                y_values = range(sy, ey-1, -1)
            else:
                y_values = range(sy, ey +1)

            for ix, iy in zip(x_values, y_values):
                grid[(ix, iy)] += 1

    count = 0
    for k, v in grid.items():
        if v > 1:
            count += 1
    print(count)
        
