with open("input.txt") as fp:
    inp = fp.read().split('\n')

z = map(lambda x: ''.join(x), zip(*inp))

gamma = ''
epsilon = ''

for l in z:
    if l.count('0') > l.count('1'):
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

gamma = int(gamma, base=2)
epsilon = int(epsilon, base=2)

print(gamma * epsilon)
