from os import link
from colorama import init, Fore

def read_file(file):
    with open(file) as fp:
        inp = fp.read().split('\n')
        grid = [[int(c) for c in row] for row in inp]
    return grid

def part_one(grid, steps):

    total_flashes = 0

    
    links = {}
    for r in range(10):
        for c in range(10):
            links[r, c] = []
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1),(-1,1), (-1,-1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < 10 and 0 <= nc < 10:
                    links[r, c].append((nr, nc))

    for _ in range(steps):
        # step one: increase all values
        for i in range(10):
            for j in range(10):
                grid[i][j] = grid[i][j] + 1

        # step two: flash all octopusses with a value higher than 9
        flashed = True
        
        while flashed:
            flashed = False
            for i in range(10):
                for j in range(10):
                    if grid[i][j] > 9:
                        total_flashes += 1
                        grid[i][j] = 0
                        
                        for m, n in links[(i, j)]:
                            if grid[m][n] > 0:
                                grid[m][n] = grid[m][n] + 1
                                flashed = True
        
        print("\n\n")
        for r in range(10):
            line = ""
            for c in range(10):
                if grid[r][c] == 0:
                    line += Fore.RED + str(grid[r][c]) + Fore.RESET
                else:
                    line += str(grid[r][c])
            print(line)

    return total_flashes


def part_two(grid):

    total_flashes = 0

    
    links = {}
    for r in range(10):
        for c in range(10):
            links[r, c] = []
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1),(-1,1), (-1,-1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < 10 and 0 <= nc < 10:
                    links[r, c].append((nr, nc))

    step = 0
    while True:
        step += 1

        # step one: increase all values
        for i in range(10):
            for j in range(10):
                grid[i][j] = grid[i][j] + 1

        # step two: flash all octopusses with a value higher than 9
        flashed = True
        this_flash = 0

        while flashed:
            flashed = False
            for i in range(10):
                for j in range(10):
                    if grid[i][j] > 9:
                        total_flashes += 1
                        this_flash += 1
                        grid[i][j] = 0
                        
                        for m, n in links[(i, j)]:
                            if grid[m][n] > 0:
                                grid[m][n] = grid[m][n] + 1
                                flashed = True
        if this_flash > 99:
            
            for r in range(10):
                line = ""
                for c in range(10):
                    if grid[r][c] == 0:
                        line += Fore.RED + str(grid[r][c]) + Fore.RESET
                    else:
                        line += str(grid[r][c])
                print(line)
            return step
                

if __name__ == "__main__":
    # initiate colorama
    init()
    
    # load inputs/test data
    inp = read_file("./input.txt")
    test = read_file("./test.txt")

    # print("Part One TEST: ", part_one(test, 100) == 1656)
    # print("Part One: ", part_one(inp, 100))
    
    print("Part Two TEST: ", part_two(test) == 195)
    print("Part Two: ", part_two(inp))
        