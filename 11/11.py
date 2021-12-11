from colorama import init, Fore

def read_file(file):
    with open(file) as fp:
        inp = fp.read().split('\n')
    return inp



if __name__ == "__main__":
    # initiate colorama
    init()
    
    # load inputs/test data
    inp = read_file("input.txt")
    test = read_file("test.txt")

    print("Part One Test: ", part_one(test))
    print("Part One: ", part_one(inp))