
def aoc_2020_day1():

    fp = open('./input.txt', 'r')
    data = fp.read()
    fp.close()

    data = data.split('\n')

    for i in range(len(data)):
        data[i] = int(data[i])

    k = 0
    for i in range(len(data)):
        for j in range(k, len(data)):
            if data[i]+data[j] == 2020:
                a = i
                b = j
                print(str(data[a]) + " * " + str(data[b]) + " = " + str(data[a]*data[b]))
        k = k + 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    aoc_2020_day1()


