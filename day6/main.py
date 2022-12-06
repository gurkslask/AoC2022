import re
import os


def main(data):
    data = data[0]
    res = 0
    for k, v in enumerate(data):
        # print(f"key: {k}, value{v}")
        done = True
        m = max(0, k - 14)
        # print(data[m:k])
        s = set(data[m:k])
        if len(s) == 14:
            done = True
            res = k
            break
    return res

        # print(data[k, k-4, -1])



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

    print(main(testdata))
    print(main(data))
