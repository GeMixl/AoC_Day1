import itertools


def aoc_2020_day1():
    for (a, b) in itertools.combinations([int(n) for n in open('input.txt')], 2):
        if a + b == 2020:
            print(a * b)


if __name__ == '__main__':
    aoc_2020_day1()


