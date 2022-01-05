from collections import Counter


def read_file(file):
    with open(file) as fp:
        algo, img = fp.read().split("\n\n")

        algo = [0 if char == '.' else 1 for char in algo]

        pixels = {(r, c) for r, row in enumerate(img.split("\n"))
                  for c, char in enumerate(row) if char == '#'}
    return algo, pixels


def enhance(pixels, algo):
    out = set()

    height, width = list(zip(*pixels))
    min_height, max_height = min(height), max(height)
    min_width, max_width = min(width), max(width)

    for (r, c) in ((r, c) for r in range(min_height-2, max_height+3) for c in range(min_width-2, max_width+3)):
        bin = ""
        for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)):
            if (r+dr, c+dc) in pixels:
                bin += '1'                
            elif (min_height <= r + dr <= max_height and min_width <= c + dc <= max_width):
                bin += '0'
            else:
                bin += str(filler) 
        idx = int(bin, 2)

        if algo[idx]:
            out.add((r, c))

    return out


def print_img(pixels):
    height, width = list(zip(*pixels))
    min_height, max_height = min(height), max(height)
    min_width, max_width = min(width), max(width)

    grid = [["." for w in range(max_width-min_width+1)]
            for h in range(max_height-min_height+1)]

    for (r, c) in pixels:
        grid[r-min_height][c-min_width] = "#"

    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    algo, img = read_file("test.txt")

    print_img(img)
    filler = 0

    for i in range(2):
        img = enhance(img, algo)
        print(f"\nround {i+1}")
        print_img(img)
        filler = 0 if filler else 1

    c = Counter(img.values())
    print(c[1])
