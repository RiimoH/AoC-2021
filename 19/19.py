from time import time
from collections import defaultdict

def read_file(file):
    with open(file) as fp:
        inp = fp.read().split("\n\n")
    scanners = {}
    for s in inp:
        scanner, *beacons = s.split("\n")
        scanner = int(scanner.split()[2])
        scanners[scanner] = []
        
        for line in beacons:
            x,y,z = line.split(',')
            scanners[scanner].append((int(x), int(y), int(z)))
        print(scanner, len(scanners[scanner]))
    return scanners
   
def generate_distances(scanners):
    scan_dist = {}
    for num, beacons in scanners.items():
        distances = {}
        for idx, (x1,y1,z1) in enumerate(beacons):
            for (x2,y2,z2) in beacons[idx:]:
                dist = round(((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5, 12)
                distances[dist] = ((x1,y1,z1),(x2,y2,z2))

        scan_dist[num] = distances
        print(num, len(distances))
    return scan_dist

def find_matches(scan_dist):
    matched_beacons = {}
    for di, beacons in scan_dist[0].items():
        if di in scan_dist[1]:
            pass

    for i in matched_beacons.items():
        print(i)

if __name__ == "__main__":
    print("---TEST---")
    scanners = read_file('test.txt')
    st = time()
    scan_dist = generate_distances(scanners)
    print(f"Generated distances in: {time()-st:.5f} s")
    find_matches(scan_dist)