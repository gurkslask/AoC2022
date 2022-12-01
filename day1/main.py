import re
import os


def main(data) -> str:
    elves = []
    tmp = 0
    for row in data:
        if row:
            tmp += int(row)
        else:
            elves.append(tmp)
            tmp = 0

    top = []
    for i in range(3):
        print(max(elves))
        top.append(max(elves))
        elves.remove(max(elves))


    return str(sum(top))


def getdata(path):
    with open(path) as f:
        data = f.readlines()
        data = [i.replace('\n', '') for i in data]
    return data


if __name__ == '__main__':

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    data = getdata('./input.txt')
    testdata = getdata('./testinput.txt')

    print("main" + main(data))
    print("test" + main(testdata))
