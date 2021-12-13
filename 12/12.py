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

def part_two(pos, path, nodes, paths, double = False):
    if pos == "end":
        paths.append(tuple([*path, pos]))
        return

    for next_node in nodes[pos]:
        if next_node.lower() != next_node or next_node not in path:
            part_two(next_node, [*path, pos], nodes, paths, double = double)
        elif next_node.lower() == next_node and not double and next_node != "start":
            part_two(next_node, [*path, pos], nodes, paths, double = True)

    return

def setup_and_run_one(txt):
    inp = read_file(txt)
    nodes = create_nodes(inp)
    paths = []
    part_one("start", list(), nodes, paths)
    return paths

def setup_and_run_two(txt):
    inp = read_file(txt)
    nodes = create_nodes(inp)
    paths = []
    part_two("start", list(), nodes, paths)
    return paths

if __name__ == "__main__":
    # initiate colorama
    init()

    # run tests
    for test, target in [("test1.txt",10), ("test2.txt",19),("test3.txt",226),]:
        paths = setup_and_run_one(test)
        print("Test: ", len(paths) == target, len(paths))
    
    paths = setup_and_run_one("input.txt")
    print("Part One: ", len(paths))
    
    # run tests
    for test, target in [("test1.txt",36), ("test2.txt",103),("test3.txt",3509),]:
        paths = setup_and_run_two(test)
        print("Test: ", len(paths) == target, len(paths))
    
    paths = setup_and_run_two("input.txt")
    print("Part Two: ", len(paths))