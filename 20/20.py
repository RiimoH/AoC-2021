from collections import Counter


def read_file(file):
    with open(file) as fp:
        algo, img = fp.read().split("\n\n")

        algo = [0 if char == "." else 1 for char in algo]

        pixels = {}
        for r, row in enumerate(img.split("\n")):
            for c, char in enumerate(row):
                pixels[r, c] = 1 if char == "#" else 0
    return algo, pixels


def enhance(pixels, algo):
    out = {}

    height, width = list(zip(*[c for c, v in pixels.items() if v == 1]))
    min_height, max_height = min(height), max(height)
    min_width, max_width = min(width), max(width)

    for (r, c) in (
        (r, c)
        for r in range(min_height - 2, max_height + 3)
        for c in range(min_width - 2, max_width + 3)
    ):
        bin = ""
        for dr, dc in (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 0),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ):
            if (r + dr, c + dc) in pixels:
                bin += str(pixels[(r + dr, c + dc)])
            else:
                bin += str(filler)
                pixels[(r + dr, c + dc)] = filler
        idx = int(bin, 2)

        out[(r, c)] = algo[idx]

    return out


def print_img(pixels):
    height, width = list(zip(*[key for key, value in pixels.items() if value == 1]))
    min_height, max_height = min(height), max(height)
    min_width, max_width = min(width), max(width)

    grid = [
        ["." for w in range(max_width - min_width + 1)]
        for h in range(max_height - min_height + 1)
    ]

    for (r, c), v in pixels.items():
        if v == 1:
            grid[r - min_height][c - min_width] = "#"

    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    algo, img = read_file("input.txt")

    print_img(img)
    filler = 0

    for i in range(50):
        img = enhance(img, algo)
        print(f"\nround {i+1}")
        print_img(img)
        if algo[0] == 1:
            filler = 0 if filler else 1

    c = Counter(img.values())
    print(c[1])
