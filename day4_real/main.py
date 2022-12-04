import re
import os


def main(data):
    pair = [i.split(',') for i in data]
    # print(pair)
    pp = []

    for p in pair:
        plist = []
        for e in p:
            elist = []
            s = e.split('-')
            for i in range(int(s[0]), int(s[1]) + 1):
                elist.append(i)
                # print(i)
            plist.append(elist)
        pp.append(plist)

    res = 0
    for pair in pp:
        overlap = True
        # print("First")
        for first_elf in pair[0]:
            # print(first_elf)
            if first_elf not in pair[1]:
                overlap = False
        if overlap:
            res += 1
            continue
        # print("Second")
        overlap = True
        for first_elf in pair[1]:
            # print(first_elf)
            if first_elf not in pair[0]:
                overlap = False
        
        if overlap: res += 1


    return str(res)


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

    print("Test: " + main(testdata))
    print("Test: " + main(data))
