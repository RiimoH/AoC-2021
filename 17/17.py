from time import time
import re


def read_file(txt):
    with open(txt) as fp:
        inp = list(map(eval, fp.read().split('\n')))
    return inp






if __name__ == "__main__":
    inp = read_file("test.txt")