from colorama import init, Fore

def read_file(file):
    with open(file) as fp:
        inp = fp.read().split('\n')
    return inp

def check_line(line):
    ledger = []

    for i, char in enumerate(line):
        if char == ")":
            target = "("
            points = 3
        elif char == "]":
            target = "["
            points = 57
        elif char == "}":
            target = "{"
            points = 1197
        elif char == ">":
            target = "<"
            points = 25137
        else:
            ledger.append(char)
            continue
            
        if ledger[-1] != target:
            # corrupted character!
            # print(line[:i]+Fore.RED+line[i]+Fore.RESET+line[i+1:])
            return (points, ledger)
        else:
            ledger.pop(-1)
    return (0, ledger)

def part_one(inp):
    score = 0
    for line in inp:
        points,_ = check_line(line)
        score += points
    return score

def part_two(inp):
    scores = []
    for line in inp:
        score = 0
        corrupt, ledger = check_line(line)
        if not corrupt:
            # this line is not corrupt.
            value_ledger = []
            for char in reversed(ledger):
                score *= 5
                if char == "(":
                    score += 1
                elif char == "[":
                    score += 2
                elif char == "{":
                    score += 3
                elif char == "<":
                    score += 4
            scores.append(score)
    scores.sort()
    return scores[int(round(len(scores)//2, 0))]

if __name__ == "__main__":
    # initiate colorama
    init()
    
    # load inputs/test data
    inp = read_file("input.txt")
    test = read_file("test.txt")

    print("Part One Test: ", part_one(test) == 26397)
    print("Part One: ", part_one(inp))
    print("Part Two Test: ", part_two(test) == 288957)
    print("Part Two: ", part_two(inp))