
def most_common(idx, zipped_values, equal_one=True):
    zipped_values = list(zipped_values)
    
    if zipped_values[idx].count('0') > zipped_values[idx].count('1'):
        return '0'
    elif zipped_values[idx].count('0') < zipped_values[idx].count('1'):
        return '1'
    else:
        return '1' if equal_one else '0'


if __name__ == "__main__":
    with open("input.txt") as fp:
        inp = fp.read().split('\n')

    ogr = inp[:]
    co2sr = inp[:]

    idx = 0
    while len(ogr) > 1:
        ogr = list(filter(lambda x: x[idx] == most_common(idx, zip(*ogr)), ogr))
        idx += 1
        print(ogr)

    idx = 0
    while len(co2sr) > 1:
        co2sr = list(filter(lambda x: x[idx] != most_common(idx, zip(*co2sr)), co2sr))
        idx += 1
        print(co2sr)

    ogr = int(ogr[0], base=2)
    print(ogr)
    co2sr = int(co2sr[0], base=2)
    print(co2sr)
    print(ogr*co2sr)
