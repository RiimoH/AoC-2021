def median(iterable):
    s = sorted(iterable)

    median = s[len(iterable) // 2]

    return median

def average(iterable):
    avg = sum(iterable) / len(iterable)
    return avg

def calc_steps(target, iterable):
    total_steps = 0
    for value in iterable:
         total_steps += abs(target-value)
    return total_steps

if __name__ == "__main__":
    with open("input.txt") as fp:
        inp = list(map(int, fp.read().strip('\n').split(',')))
        print(inp[:10], len(inp))

    test = [16,1,2,0,4,2,7,1,2,14]

    med = median(inp)
    fuel_spent = calc_steps(med, inp)
    print(fuel_spent)
