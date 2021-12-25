from time import time
from collections import defaultdict

transformations = {
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (y, -z, -x),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-z, -x, y),
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-z, -y, -x),
}


def read_file(file):
    with open(file) as fp:
        inp = fp.read().split("\n\n")

    scanners = []
    for s in inp:
        scanner, *beacons = s.split("\n")
        b = set()
        for line in beacons:
            x, y, z = line.split(',')
            b.add((int(x), int(y), int(z)))
        scanners.append(b)
    return scanners


if __name__ == "__main__":
    scanners = read_file('test.txt')
    st = time()
    ocean = set(scanners.pop(0))
    scanner_coords = [(0, 0, 0)]

    while scanners:
        test_scanner = scanners.pop(0)
        match = False
        for transform in transformations:
            offsets = defaultdict(int)

            for beacon in ocean:
                rotated_points = set()
                for point in test_scanner:
                    rotated_point = transform(*point)
                    x1, y1, z1 = beacon
                    x2, y2, z2 = rotated_point
                    offset = (x1-x2, y1-y2, z1-z2)
                    offsets[offset] += 1
            for (xo, yo, zo), count in offsets.items():
                if count >= 12:
                    match = True
                    scanner = (xo, yo, zo) = (-xo, -yo, -zo)
                    scanner_coords.append(scanner)
                    for point in test_scanner:
                        xp, yp, zp = transform(*point)
                        ocean.add(
                            (xp+xo, yp+yo, zp+zo))
        if not match:
            scanners.append(test_scanner)

    print(f"Part One: {len(ocean)}, {time()-st:.2f}")
