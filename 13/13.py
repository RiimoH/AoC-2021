def read_file(txt):
    with open(txt) as fp:
        inp = fp.read()
    
    dots, folds = inp.split("\n\n")
    return dots, folds

def print_grid(loc, size = 30):
    grid = [['.' for x in range(size)] for y in range(size)]
    for x, y in loc:
        grid[y][x] = "#"
    
    for row in grid:
        print("".join(row))

def part_one(txt):
    dots, folds = read_file(txt)
    loc = set()
    
    for dot in dots.split("\n"):
        x, y = dot.split(',')
        x = int(x)
        y = int(y)
        loc.add((x,y))
    
    for fold in folds.split("\n"):
        fold = fold.lstrip("fold along ")
        orientation, value = fold.split("=")
        value = int(value)
        
        print(orientation, value)
        
        new_loc = set()
        for x, y in loc:
            if "x" in orientation:
                x = value - (x - value) if x > value else x
            else:
                y = value - (y - value) if y > value else y
            
            new_loc.add((x, y))
        
        loc = new_loc
    
        print(len(loc))
        
def part_two(txt):
    dots, folds = read_file(txt)
    loc = set()
    
    for dot in dots.split("\n"):
        x, y = dot.split(',')
        x = int(x)
        y = int(y)
        loc.add((x,y))
    
    for fold in folds.split("\n"):
        fold = fold.lstrip("fold along ")
        orientation, value = fold.split("=")
        value = int(value)
        
        size = 0
        new_loc = set()
        for x, y in loc:
            if "x" in orientation:
                x = value - (x - value) if x > value else x
            else:
                y = value - (y - value) if y > value else y
            size = max(size, x, y)
            new_loc.add((x, y))
        
        loc = new_loc
    
    print_grid(loc, size*2)
    
if __name__ == "__main__":
    part_one("test.txt")
    part_one("input.txt")
    part_two("input.txt")