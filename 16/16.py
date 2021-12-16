from os import read
from colorama import init, Fore
from time import time


def read_file(txt):
    with open(txt) as fp:
        inp = fp.read()
    return inp


def decode(hex_value):
    hex_2_bin = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111", }
    return hex_2_bin[hex_value]


def parse(packet, version_sum):
    if not packet:
        return 0, 0, version_sum
    version = int(packet[:3], 2)
    version_sum += version
    tid = int(packet[3:6], 2)
    packet = packet[6:]

    if tid == 4:
        # number
        num = ""
        while len(packet) >= 5:
            p = packet[0]
            num += packet[1:5]
            packet = packet[5:]
            if p == "0":
                break

        num = int(num, 2)

        return num, packet, version_sum

    else:
        # operator
        ltid = packet[0]
        values = []

        if ltid == "0":
            tlib = int(packet[1:16], 2)
            sub_packet = packet[16:16+tlib]

            while sub_packet:
                val, sub_packet, version_sum = parse(sub_packet, version_sum)
                values.append(val)
        
            sub_packet = packet[16+tlib:]

        elif ltid == "1":
            nosp = int(packet[1:12], 2)
            sub_packet = packet[12:]
            for i in range(nosp):
                val, sub_packet, version_sum = parse(sub_packet, version_sum)
                values.append(val)


        if tid == 0:
            return sum(values), sub_packet, version_sum
        elif tid == 1:
            return product(values), sub_packet, version_sum
        elif tid == 2:
            return min(values), sub_packet, version_sum
        elif tid == 3:
            return max(values), sub_packet, version_sum
        elif tid == 5:
            return (1 if values[0] > values[1] else 0), sub_packet, version_sum
        elif tid == 6:
            return (1 if values[0] < values[1] else 0), sub_packet, version_sum
        elif tid == 7:
            return (1 if values[0] == values[1] else 0), sub_packet, version_sum


def product(iterable):
    p = 1
    for i in iterable:
        p *= i
    return p

if __name__ == "__main__":
    # initalize colorama
    init()
    inp = read_file("test.txt")
    bits = "".join(map(decode, inp))
    version_sum = 0

    # execute
    st = time()

    n, v, vs = parse("".join(map(decode, "D2FE28")), 0)
    print("Test 1.1:", n == 2021)

    n, v, vs = parse("".join(map(decode, "38006F45291200")), 0)
    print("Test 1.2:", n == 30)

    n, v, vs = parse("".join(map(decode, "EE00D40C823060")), 0)
    print("Test 1.3:", n == 6)

    n, v, vs = parse("".join(map(decode, "8A004A801A8002F478")), 0)
    print("Test 1.4:", vs == 16)

    n, v, vs = parse("".join(map(decode, "620080001611562C8802118E34")), 0)
    print("Test 1.5:", vs == 12)

    n, v, vs = parse("".join(map(decode, "C0015000016115A2E0802F182340")), 0)
    print("Test 1.6:", vs == 23)

    n, v, vs = parse("".join(map(decode, "A0016C880162017C3686B18A3D4780")), 0)
    print("Test 1.7:", vs == 31)

    n, v, vs = parse("".join(map(decode, "C200B40A82")), 0)
    print("Test 2.1:", n == 3)

    n, v, vs = parse("".join(map(decode, "04005AC33890")), 0)
    print("Test 2.2:", n == 54)

    n, v, vs = parse("".join(map(decode, "880086C3E88112")), 0)
    print("Test 2.3:", n == 7)

    n, v, vs = parse("".join(map(decode, "CE00C43D881120")), 0)
    print("Test 2.4:", n == 9)

    n, v, vs = parse("".join(map(decode, "D8005AC2A8F0")), 0)
    print("Test 2.5:", n == 1)

    n, v, vs = parse("".join(map(decode, "F600BC2D8F")), 0)
    print("Test 2.6:", n == 0)

    n, v, vs = parse("".join(map(decode, "9C005AC2F8F0")), 0)
    print("Test 2.7:", n == 0)

    n, v, vs = parse("".join(map(decode, "9C0141080250320F1802104A08")), 0)
    print("Test 2.8:", n == 1)

    n, v, vs = parse("".join(map(decode, read_file("input.txt"))), 0)
    print("Part 1:", vs, "Part 2:", n)

    et = time()
    print(version_sum, et - st)
