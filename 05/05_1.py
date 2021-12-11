from collections import defaultdict

if __name__ == "__main__":
    with open("test.txt") as fp:
        inp = fp.read().split('\n')

    # grid = defaultdict(int)
    grid = [[0 for x in range(10)] for y in range(10)]

    for line in inp:
        start, end = line.split(' -> ')
        sx, sy = map(int, start.split(','))
        ex, ey = map(int, end.split(','))

        if sx > ex:
            x_values = range(sx, ex-1, -1)
        else:
            x_values = range(sx, ex +1)

        print(line, x_values)
        

        for ix, iy in zip(range(sx, ex+1), range(sy, ey+1)):
            print(line, ix, iy)
            grid[iy][ix] += 1

    for row in grid:
        print(row)
        


    count = 0
    for k, v in grid.items():
        if v > 1:
            count += 1
    print(count)
        
