DIGITS = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
    }


    


if __name__ == "__main__":
    with open("input.txt") as fp:
        inp = fp.read().split('\n')

    inp = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    indicators = [2,4,3,7]
    unique = 0
    
    for line in inp:
        left, right = line.split(' | ')
        lefts = left.split()
        rights = right.split()

        for digit in rights:
            if len(digit) in indicators:
                unique += 1

    print(unique)
