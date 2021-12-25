def read_file(file):
    with open(file) as fp:
        inp = compile_inp(fp.read())
    return inp

def compile_inp(inp):
    return list(map(list, inp.split('\n')))

def move(inp):
    height = len(inp)
    width = len(inp[0])

    new = []

    for r, row in enumerate(inp):
        new_row = row[:]
        for c, char in enumerate(row):
            if char == '>':
                if c + 1 == width:
                    if row[0] == '.':
                        new_row[c] = '.'
                        new_row[0] = '>'
                else:
                    if row[c+1] == '.':
                        new_row[c] = '.'
                        new_row[c+1] = '>'
        new.append(new_row)
    
    inp = new
    new = [row[:] for row in inp]

    for r, row in enumerate(inp):
        for c, char in enumerate(row):
            if char == 'v':
                if r + 1 == height:
                    if inp[0][c] == '.':
                        new[r][c] = '.'
                        new[0][c] = 'v'
                else:
                    if inp[r+1][c] == '.':
                        new[r][c] = '.'
                        new[r+1][c] = 'v'
                    
    return new

def pp(inp, s = 0):
    print(f"After {str(s).rjust(3,' ')} steps:")
    for row in inp:
        print(''.join(row))

if __name__ == "__main__":
    inp = read_file("input.txt")
    i = 0
    while True:
        i += 1
        new = move(inp)

        if inp == new:
            print(i)
            break
        else:
            inp = new
    
