from heap import Heap
from time import sleep, time
from collections import defaultdict

COSTS = {
    "A":1,
    "B":10,
    "C":100,
    "D":1000,
}

TARGET_COLUMNS = {
    3:"A",
    5:"B",
    7:"C",
    9:"D"
}

GRID = """#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #########""".split("\n")


def read_file(inp):
    with open(inp) as fp:
        return fp.read().split('\n')


def print_sit(positions):
    p = GRID.copy()
    for (r, c), l in positions.items():
        p[r] = p[r][:c] + l + p[r][c+1:]
    for l in p:
        print(l)


def create_nodes(inp):
    nodes = defaultdict(list)
    positions = {}

    for r, row in enumerate(inp):
        for c, col in enumerate(row):
            if col == '.':
                nodes[r,c] = path_finder(r, c, inp)

                for path in nodes[r,c]:
                    trgt = path[-1]
                    nodes[trgt].append(path[:-1][::-1] + ((r,c),))
            elif col in "ABCD":
                positions[r,c] = col
    return nodes, positions
                    
                    
def path_finder(r, c, inp, path = None, valid_paths = None, visited = None):
    if valid_paths is None:
        valid_paths = []
    if visited is None:
        visited = [(r, c),]
    if path is None:
        path = tuple()
        
    for dr, dc in ((1,0), (0,1), (-1,0), (0,-1)):
        nr, nc = r+dr, c+dc
        if (nr, nc) not in visited:
            visited.append((nr, nc))
            np = path + ((nr, nc),)
            if inp[nr][nc] == "#":
                continue
            elif inp[nr][nc] in "ABCD":
                valid_paths.append(np)
            
            valid_paths = path_finder(
                nr, nc, inp,
                path = np,
                valid_paths = valid_paths,
                visited = visited
                )
    return valid_paths


def solve(nodes, positions):
    queue = Heap([(0, positions, set()),])
    cache = set()
    
    while True:
        try:
            cost, positions, fixed = queue.pop()
        except Exception as e:
            print_sit(positions)
            print(queue._data, fixed)
            raise e
        
        hashable = tuple(sorted(positions.items()))
        if hashable in cache:
            continue
        else:
            cache.add(hashable)
        
        if check_solved(positions):
            return cost
        
        for pos, amphipod in positions.items():
            if pos not in fixed:
                r, c = pos
                for ppath in nodes[pos]:
                    
                    new_pos = ppath[-1]
                    
                    # check if this is a valid move
                    if check_obstacles(positions, ppath):
                        # check if it wants to go into it's final spot
                        tofix = False
                        if new_pos[1] in TARGET_COLUMNS:
                            # check if others are here and this is the right room for our amphipod
                            if check_room(new_pos[1], amphipod, positions):
                                # check how low it can go -> extend ppath
                                if GRID[r][c] == '.' and (r+1, c) in positions and positions[r+1, c] == amphipod:
                                    # would not go to the very bottom and thus will be better handled by another path.
                                    continue
                                tofix = True
                            else:
                                # wrong room
                                continue

                        # if valid move, push to queue
                        npositions = positions.copy()
                        del npositions[pos]
                        npositions[new_pos] = amphipod
                        ncost = cost + (len(ppath) * COSTS[amphipod])
                        nfixed = fixed.union({new_pos,}) if tofix else fixed.copy()

                        queue.push((ncost, npositions, nfixed))


def check_solved(positions):
    for (r,c), amphipod in positions.items():
        if c not in [3,5,7,9] or amphipod != TARGET_COLUMNS[c]:
            return False
    return True


def check_depth(ppath, positions):
    ir, ic = ppath[-1]
    
    while (ir+1, ic) not in positions and GRID[ir+1][ic] == '.':
        ppath = ppath + ((ir+1, ic),)
        ir += 1
    
    return ppath


def check_room(tc, amphipod, positions):
    if amphipod != TARGET_COLUMNS[tc]:
        return False
    
    for (ipr, ipc), occupant in positions.items():
        if ipc == tc and amphipod != occupant:
            return False
    
    return True
    
    
def check_obstacles(positions, ppath):
    for p in ppath:
        if p in positions:
            return False
    return True
   

if __name__ == "__main__":
    # nodes, positions = create_nodes(read_file("test.txt"))
    # nodes, positions = create_nodes(read_file("input.txt"))
    # nodes, positions = create_nodes(read_file("test_2.txt"))
    nodes, positions = create_nodes(read_file("input_2.txt"))
    st = time()
    cost = solve(nodes, positions)
    print(cost, f'{time()-st:.3f} s')
