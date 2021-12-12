from colorama import init, Fore
from collections import defaultdict


def read_file(file):
    with open(file) as fp:
        inp = fp.read().split('\n')
    return inp


def create_nodes(inp):

    nodes = defaultdict(list)
    for line in inp:
        l, r = line.split("-")
        nodes[l].append(r)
        nodes[r].append(l)

    return nodes


def part_one(pos, path, nodes, paths):
    if pos == "end":
        paths.append(tuple([*path, pos]))
        return

    for next_node in nodes[pos]:
        if next_node.lower() != next_node or next_node not in path:
            part_one(next_node, [*path, pos], nodes, paths)

    return


if __name__ == "__main__":
    # initiate colorama
    init()

    # load inputs/test data
    inp = read_file("./input.txt")
    test = read_file("./test1.txt")

    paths = []
    nodes = create_nodes(test)
    part_one("start", list(), nodes, list())
    print("Part One TEST: ", paths)
    # print("Part One: ", part_one(inp, 100))

    # print("Part Two TEST: ", part_two(test) == 195)
    # print("Part Two: ", part_two(inp))
