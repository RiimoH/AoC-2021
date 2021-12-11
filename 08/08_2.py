DIGITS_2_SEG = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
    }
SEG_2_DIGITS = {v:k for k, v in DIGITS_2_SEG.items()}

if __name__ == "__main__":
    with open("input.txt") as fp:
        inp = fp.read().split('\n')

    indicators = {2:1,4:4,3:7,7:8}
    total = 0
    for line in inp:
        connections = {x: {y for y in "abcdefg"} for x in "abcdefg"}
        lit_cable, right_side = line.split(' | ')
        lit_cable_values = lit_cable.split()
        lit_cable_values.sort(key=lambda x: len(x))

        occurence_in_5 = {x: 0 for x in "abcdefg"}
        occurence_in_6 = {x: 0 for x in "abcdefg"}

        for cable in lit_cable_values:
            if len(cable) == 2:
                connections["c"].intersection_update(set(cable))
                connections["f"].intersection_update(set(cable))
            elif len(cable) == 3:
                connections["a"] = (set(cable)-connections["c"]).pop()
            elif len(cable) == 4:
                connections["b"] = set(cable)-connections["c"]
                connections["d"] = set(cable)-connections["c"]
            elif len(cable) == 5:
                for letter in cable:
                    occurence_in_5[letter] += 1
            elif len(cable) == 6:
                for letter in cable:
                    occurence_in_6[letter] += 1


        for key, value in occurence_in_5.items():
            if value == 2 and occurence_in_6[key] == 3:
                connections["f"] = key
                connections["c"].remove(key)
                connections["c"]= connections["c"].pop()

            elif value == 3 and occurence_in_6[key] == 2:
                connections["d"] = key
                connections["b"].remove(key)
                connections["b"] = connections["b"].pop()
                
        for key, value in occurence_in_5.items():
            if value == 3 and occurence_in_6[key] == 3 and key not in [connections["a"], connections["d"]]:
                connections["g"] = key

        
        connections["e"] = connections["e"].difference({v for v in connections.values() if type(v) is str}).pop()
        reverse_connections = {v: k for k, v in connections.items()}

        output = ""
        for display in right_side.split():
            part = []
            for k in display:
                part.append(reverse_connections[k])

            output += str(SEG_2_DIGITS[''.join(sorted(part))])

        total += int(output)
    print(total)                  
