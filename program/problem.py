import re
from data import *

def read_instance(filename):
    return CAInstance.from_file(filename)

def evaluate(instance, solution, verbose=False):
    return instance.evaluate(solution)

def test():
    instance = read_instance('instances/rc_201.1.txt')
    opt = [14, 18, 13, 9, 5, 4, 6, 8, 7, 16, 19, 11, 17, 1, 10, 3, 12, 2, 15]
    violations, distance = evaluate(instance, opt, True)
    assert violations == 0
    assert abs(444.542 - distance) < 0.001

if __name__ == '__main__': 
    test()
