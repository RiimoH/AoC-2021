from colorama import init, Fore

def read_file(file):
    with open(file) as fp:
        inp = fp.read().split('\n')
        inp = [[int(char) for char in row] for row in inp]
        print(inp)
    return inp

def part_one(inp):

    total_flashes = 0


    while True:
        # step one: increase all values
        for row in inp:
            for octopuss in row:
                octopuss += 1

        # step two: flash all octopusses with a value higher than 9
        flashed = True
        
        while flashed:
            flashed = False
            for row, line in enumerate(inp):
                for col, octopuss in enumerate(line):
                    if octopuss > 9:
                        total_flashes += 1
                        octopuss -= octopuss
                        for dr, dc in ((1,0), (0,1), (0,-1), (-1,0)):
                            cr = dr+row
                            cc = dc+col
                            if 0 <= cr < 10 and 0 <= cc < 10:
                                if inp[cr][cc] > 0:
                                    inp[cr][cc] += 1
                                    flashed = True

        yield inp



if __name__ == "__main__":
    # initiate colorama
    init()
    
    # load inputs/test data
    inp = read_file("./input.txt")
    test = read_file("./test.txt")

    p1 = part_one(test)
    for _ in range(2):
        next(p1)

    
    for row in test:
        print(''.join(map(str, row)))
        