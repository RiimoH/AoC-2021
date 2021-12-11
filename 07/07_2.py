def median(iterable):
    s = sorted(iterable)

    median = s[len(iterable) // 2]

    return median

def rounded_average(iterable, n_digits=0):
    avg = sum(iterable) / len(iterable)
    print(avg)
    return round(avg, n_digits)

def calc_steps(target, iterable):
    total_steps = 0
    for value in iterable:
         total_steps += abs(target-value)
    return total_steps

def fuel_spending(target, pos):
    goal = int(abs(target-pos) + 1)
    return sum(range(goal))
        

if __name__ == "__main__":
    with open("input.txt") as fp:
        inp = list(map(int, fp.read().strip('\n').split(',')))

    # inp = [16,1,2,0,4,2,7,1,2,14]

    avg = rounded_average(inp)
    fuel_lookup = {}

    fuel_spent = 0
    for pos in inp:
        if pos not in fuel_lookup:
            fuel_lookup[pos] = fuel_spending(avg, pos)

        fuel_spent += fuel_lookup[pos]

    print(avg, fuel_spent)

    fuel_lookup = {}
    fuel_spent = 0
    for pos in inp:
        if pos not in fuel_lookup:
            fuel_lookup[pos] = fuel_spending(avg-1, pos)

        fuel_spent += fuel_lookup[pos]

    print(avg, fuel_spent)
