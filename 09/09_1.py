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
    risk_level = 0
    dirs = ((1,0), (0, 1) , (-1, 0), (0,-1))
    s = ""
    for y, row in enumerate(inp):
        for x, char in enumerate(row):
            if char == 9:
                continue
            
            lowest = True
            for d in dirs:
                try: 
                    if inp[y+d[0]][x+d[1]] < char:
                        lowest = False
                except IndexError:
                    continue
                
            if lowest:
                risk_level += char + 1
                s += Back.RED + str(char) + Back.RESET
            else:
                s += str(char)
        s+= '\n'

    print(s)

    return risk_level

if __name__ == "__main__":
    init()
    with open("input.txt") as fp:
        inp = fp.read().split('\n')

    inp = [[int(x) for x in list(y)] for y in inp]

    print(adj(inp))
