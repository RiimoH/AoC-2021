from time import time
from collections import defaultdict


class Scanner():

    transformer_functions = [
        lambda node: (node[0], node[1], node[2]),
        lambda node: (node[0], node[2], node[1]),
        lambda node: (node[1], node[0], node[2]),
        lambda node: (node[1], node[2], node[0]),
        lambda node: (node[2], node[0], node[1]),
        lambda node: (node[2], node[1], node[0]),
    ]
    phase_functions = [
        lambda node: (node[0], node[1], node[2]),
        lambda node: (node[0], -node[1], -node[2]),
        lambda node: (node[0], node[1], -node[2]),
        lambda node: (node[0], -node[1], node[2]),
        lambda node: (-node[0], node[1], node[2]),
        lambda node: (-node[0], -node[1], node[2]),
        lambda node: (-node[0], node[1], -node[2]),
        lambda node: (-node[0], -node[1], -node[2]),
    ]

    def __init__(self, id, scanned_beacons):
        self.id = id
        self.phaser = self.phase_functions[0]
        self.transformer = self.transformer_functions[0]
        self._original_beacons = set(scanned_beacons)
        self.beacons = set(scanned_beacons)
        self.distances = self._generate_distances()

    def _generate_distances(self):
        beacons = list(self.beacons)
        distances = {}
        for idx, (x1, y1, z1) in enumerate(beacons):
            for (x2, y2, z2) in beacons[idx:]:
                if (x1, y1, z1) != (x2, y2, z2):
                    dist = round(((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5, 12)
                    distances[dist] = ((x1, y1, z1), (x2, y2, z2))

        return distances

    def find_transformation(self, matched_beacons):
        for transformer in self.transformer_functions:
            for phaser in self.phase_functions:

                origin = list(matched_beacons.keys())[0]
                target = phaser(transformer(matched_beacons[origin]))

                self.translation = (origin[0] - target[0], origin[1] - \
                    target[1], origin[2] - target[2])

                print(origin, target, self.translation)

                for origin, target in matched_beacons.items():
                    if self.translate(phaser(transformer(target))) != origin:
                        break
                else:
                    self.transformer = transformer
                    self.phaser = phaser
                    return True
            return False

    def translate(self, node):
        tx, ty, tz = self.translation
        return (node[0]+tx, node[1] + ty, node[2] + tz)

    def transform_all(self):
        self.beacons = set(map(self.phaser, map(
            self.transformer, self._original_beacons)))

    def add_beacons(self, beacons):
        self.beacons.update(beacons)
        self.distances = self._generate_distances()


def read_file(file):
    with open(file) as fp:
        inp = fp.read().split("\n\n")
    scanners = {}
    for s in inp:
        scanner, *beacons = s.split("\n")
        scanner = int(scanner.split()[2])
        scanners[scanner] = set()

        for line in beacons:
            x, y, z = line.split(',')
            scanners[scanner].add((int(x), int(y), int(z)))
    return scanners


def find_matches(distances1, distances2):
    matches = []
    for di, beacons in distances1.items():
        if di in distances2:
            matches.append((beacons, distances2[di]))

    matched_beacons = {}
    for i, (t1, m1) in enumerate(matches):
        t1_1, t1_2 = t1

        for (t2, m2) in matches[i+1:]:

            if t1_1 in t2:
                matched_beacons[t1_1] = set(m1).intersection(set(m2)).pop()
                res = set(m1)
                res.remove(matched_beacons[t1_1])
                matched_beacons[t1_2] = res.pop()

                t2_2 = t2[0] if t2[0] != t1_1 else t2[1]

                res = set(m2)
                res.remove(matched_beacons[t1_1])
                matched_beacons[t2_2] = res.pop()

    return matched_beacons


if __name__ == "__main__":
    print("---TEST---")
    scanners = read_file('test.txt')
    st = time()
    original_reference = Scanner(0, scanners[0])

    scanner_nums = [k for k in scanners.keys() if k != 0]

    while scanner_nums:
        scanner_num = scanner_nums.pop(0)
        print(f"Trying to fit {scanner_num}")

        # Generate all distances
        # dict -> key: distance rounded to 12 after comma, value: ((x1,y1,z1)(x2,y2,z2))
        scanner = Scanner(scanner_num, scanners[scanner_num])

        # Find 2 distances that match -> allows to assign 3 nodes
        matches = find_matches(original_reference.distances, scanner.distances)

        # If not match was possible, visit this scanner later again
        if len(matches)<3:
            scanner_nums.append(scanner_num)
            continue

        # Try to find a transformation that matches all the nodes
        # Transform all nodes to new reference
        scanner.find_transformation(matches)
        scanner.transform_all()

        print(scanner.translation)

        # Add all transformed beacons to frame of reference
        original_reference.add_beacons(scanner.beacons)

    print(f"Finished in: {time()-st:.5f} s")
    print("Part One:", len(original_reference.beacons))
    for b in sorted(list(original_reference.beacons)):
        print(b)
