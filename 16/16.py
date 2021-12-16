from colorama import init, Fore
from time import time

def read_file(txt):
    with open(txt) as fp:
        inp = fp.read()
    return inp


def decode(hex_value):
    hex_2_bin = {
"0" : "0000",
"1" : "0001",
"2" : "0010",
"3" : "0011",
"4" : "0100",
"5" : "0101",
"6" : "0110",
"7" : "0111",
"8" : "1000",
"9" : "1001",
"A" : "1010",
"B" : "1011",
"C" : "1100",
"D" : "1101",
"E" : "1110",
"F" : "1111",}
    return hex_2_bin[hex_value]


def parse(packet, version_sum):
    version = int(packet[:3], 2)
    version_sum += version
    tid = int(packet[3:6], 2)
    packet = packet[6:]
            
    if tid == 4:
        # number
        num = ""
        while True:
            p = packet[0]
            num += packet[1:5]
            packet = packet[6:]
            if p == "0":
                break
                
        num = int(self.num, 2)
            
        return num, packet
        
    else:
        # operator
        ltid = packet[7]
        values = []
        
        if ltid == "0":
            tlib = int(packet[8:23], 2)
            sub_packet = packet[23:23+tlib]
            
            while sub_packet:
                val, sub_packet = parse(sub_packet, version_sum)
                values.append(val)
        
        elif ltid == "1":
            nosp = int(packet[8:19], 2)
            sub_packet = packet[19:]
            for i in range(nosp):
                val, sub_packet = parse(sub_packet, version_sum)
                values.append(val)

        return sum(values), sub_packet
    

if __name__ == "__main__":
    # initalize colorama
    init()
    inp = read_file("test.txt")
    bits = "".join(map(decode, inp))
    version_sum = 0

    # execute
    st = time()
    parse(bits, version_sum)
    et = time()
    print(version_sum, et- st)
    
