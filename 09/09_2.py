from colorama import init, Back

def all_around(inp):
    risk_level = 0

    for y, row in enumerate(inp):
        for x, char in enumerate(row):
            if char == 0:
                risk_level+= 1
            else:

                x_min = max(x-1, 0)
                x_max = min(x+2, len(row))
                y_min = max(y-1, 0)
                y_max = min(y+2, len(inp))

                lowest = True
                for ix in range(x_min, x_max):
                    for iy in range(y_min, y_max):
                        if inp[iy][ix] < char:
                            lowest = False
                            break
                    else:
                        continue
                    break

                if lowest:
                    risk_level += char + 1

            return risk_level


def adj(inp):
    lowest_points = []
    dirs = ((1,0), (0, 1) , (-1, 0), (0,-1))
    s = ""
    for y, row in enumerate(inp):
        for x, char in enumerate(row):
            if char != 9:
                lowest = True
                for d in dirs:
                    try: 
                        if inp[y+d[0]][x+d[1]] < char:
                            lowest = False
                    except IndexError:
                        continue
            else:
                lowest = False
            if lowest:
                lowest_points.append((x, y))
                s += Back.RED + str(char) + Back.RESET
            else:
                s += str(char)
        s+= '\n'

    # print(s)

    return lowest_points


def generate_basin(x, y, basin, inp):
    dirs = ((1,0), (0,1) , (-1,0), (0,-1))
    for dx, dy in dirs:
        nx = x+dx
        ny = y+dy
        
        if ny < 0 or nx < 0:
            continue
        else:
            try:
                inp_value = inp[ny][nx]
            except IndexError:
                continue

            if inp_value == 9:
                continue
            elif (nx, ny) not in basin:
                basin.add((nx, ny)) 
                generate_basin(nx, ny, basin, inp)
    
def product(iterable):
    p = 1
    for i in iterable:
        p *= i
    return p

if __name__ == "__main__":
    init() # initiate colorama
    with open("input.txt") as fp:
        inp = fp.read().split('\n')

    inp = [[int(x) for x in list(y)] for y in inp]

    lowest_points = adj(inp)
    basins = {lp: {lp, } for lp in lowest_points}
    
    for lp in lowest_points:
        generate_basin(lp[0], lp[1], basins[lp], inp)
    
    basin_sizes = []
    for k, v in basins.items():
        basin_sizes.append(len(v))
    basin_sizes.sort(reverse=True)

    print(basin_sizes[:3], product(basin_sizes[:3]))
