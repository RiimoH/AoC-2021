

if __name__ == "__main__":
    with open("input.txt") as fp:
        inp = list(map(int, fp.read().split(',')))


    spawncycle = [inp.count(x) for x in range(9)]
    print(spawncycle)

    for day in range(256):
        spawncycle = [*spawncycle[1:7], spawncycle[7] + spawncycle[0], spawncycle[8], spawncycle[0]]
        
    print(sum(spawncycle))
