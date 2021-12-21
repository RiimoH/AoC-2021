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
        self.distances = self._generate_distances(scanned_beacons)

    def _generate_distances(self):
        beacons = list(self.beacons)
        distances = {}
        for idx, (x1, y1, z1) in enumerate(beacons):
            for (x2, y2, z2) in beacons[idx:]:
                dist = round(((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5, 12)
                distances[dist] = ((x1, y1, z1), (x2, y2, z2))

        return distances

    def find_transformation(self, matched_beacons):
        for transformer in self.transformer_functions:
            for phaser in self.phase_functions:
                for origin, target in matched_beacons:
                    if phaser(transformer(origin)) != target:
                        break
                else:
                    self.transformer = transformer
                    self.phaser = phaser
                    return True
            return False

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

        for (t2, m2) in matches[i:]:
            if t1_1 in matched_beacons:
                pass
            else:
                if t1_1 in t2:
                    matched_beacons[t1_1] = set(m1).intersection(set(m2)).pop()
                    matched_beacons[t1_2] = set(
                        m1).remove(matched_beacons[t1_1])

                    t2_2 = t2.remove(t1_1).pop()
                    matched_beacons[t2_2] = set(
                        m2).remove(matched_beacons[t1_1])

    return matched_beacons


if __name__ == "__main__":
    print("---TEST---")
    scanners = read_file('test.txt')
    st = time()
    original_reference = Scanner(0, scanners[0])

    scanner_nums = {k for k in scanners.keys() if k != 0}

    while scanner_nums:
        print("Trying to fit {scanner_num}")
        scanner_num = scanner_num.pop(0)

        # Generate all distances
        # dict -> key: distance rounded to 12 after comma, value: ((x1,y1,z1)(x2,y2,z2))
        scanner = Scanner(scanners[scanner_num])

        # Find 2 distances that match -> allows to assign 3 nodes
        matches = find_matches(original_reference, scanner)

        # If not match was possible, visit this scanner later again
        if not matches:
            scanner_nums.append(scanner_num)
            continue

        # Try to find a transformation that matches all the nodes
        # Transform all nodes to new reference
        scanner.find_transformation()
        scanner.transform_all()

        # Add all transformed beacons to frame of reference
        original_reference.add_beacons(scanner.beacons)

    print(f"Finished in: {time()-st:.5f} s")
    print("Part One:", len(original_reference.beacons))
