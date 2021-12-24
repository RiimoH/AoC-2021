def read_file(file):
    with open(file) as fp:
        inp = fp.read().split("\n")
    return inp
    
def part_one(inp, *inp_values):
    vars = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    inp_values = list(inp_values)

    for line in inp:
        instr, *vals = line.split(' ')
        if instr == "inp":
            a = vals.pop()
            vars[a] = inp_values.pop(0)
        elif instr == "add":
            a, b = vals
            vars[a] += int(b) if not b.isalpha() else vars[b]
        elif instr == "mul":
            a, b = vals
            vars[a] *= int(b) if not b.isalpha() else vars[b]
        elif instr == "div":
            a, b = vals
            vars[a] = int(vars[a] / (int(b) if not b.isalpha() else vars[b]))
        elif instr == "mod":
            a, b = vals
            vars[a] %= int(b) if not b.isalpha() else vars[b]
        elif instr == "eql":
            a, b = vals
            vars[a] = 1 if vars[a] == (int(b) if not b.isalpha() else vars[b]) else 0

    return vars
    
if __name__ == "__main__":

    inp = read_file("test1.txt")
    v = part_one(inp, 1)
    print(v["x"])
    inp = read_file("test2.txt")
    v = part_one(inp, 1, 3)
    print(v["z"])
    inp = read_file("test3.txt")
    v = part_one(inp, 1)
    print(v["z"])