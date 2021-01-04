
def aoc_2020_day1():

    with open('./input.txt', 'r') as file:
        data = [int(line) for line in file]

    for k, i in enumerate(data):
        for j in data[k+1:]:
            if i+j == 2020:
                print("{} * {} = {}".format(i, j, i*j))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    aoc_2020_day1()


