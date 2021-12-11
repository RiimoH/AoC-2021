

if __name__ == "__main__":
    with open("input.txt") as fp:
        inp = list(map(int, fp.read().split(',')))

    for day in range(80):
        new_fish = 0
        new_list = []
        for fish in inp:
            if fish == 0:
                new_list.append(6)
                new_fish += 1
            else:
                new_list.append(fish-1)
        for i in range(new_fish):
            new_list.append(8)

        inp = new_list

    print(len(inp))
