from colorama import init, Fore
from time import time

import heapq

def read_file(txt):
    with open(txt) as fp:
        inp = fp.read().split("\n")
    return {(x,y): int(n) for y, row in enumerate(inp) for x, n in enumerate(row)}
    
def solve(puzzle):
    maxX, maxY = map(max, zip(*puzzle))
    part1 = dijkstra(puzzle, (maxX, maxY))
    
    puzzle2 = {}
    for j in range(5):
        for i in range(5):
            for (x,y), value in puzzle.items():
                newXY = (x + (maxX + 1) * i, y+(maxY+1)*j)
                newVal = value + j + i
                puzzle2[newXY] = newVal if newVal < 10 else newVal % 9
    maxX, maxY = map(max, zip(*puzzle2))
    part2 = dijkstra(puzzle2, (maxX, maxY))
    
    return part1, part2


def dijkstra(grid, target, start=(0,0), risk = 0):
    pq, visited = [(risk, start)], {start}
    
    while pq:
        risk, (x, y) = heapq.heappop(pq)
        if (x, y) == target:
            return risk
        
        for neighb in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
            if neighb not in grid or neighb in visited: continue
            
            newRisk = risk + grid[neighb]
            visited.add(neighb)
            heapq.heappush(pq, (newRisk, neighb))
    return visited
    
if __name__ == "__main__":
    # initalize colorama
    init()
    
    # prepare execution
    grid = read_file("input.txt")
    
    # execute
    st = time()
    print(solve(grid))
    et = time()
    print(et- st)
    
