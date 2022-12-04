import re
import os
import string
from collections import defaultdict


def main(data):
    res = 0
    same = []
    pointsdict = {}
    for v,k in enumerate ( string.ascii_lowercase):
        pointsdict[k] = v + 1

    for v,k in enumerate ( string.ascii_uppercase):
        pointsdict[k] = v + 27

    for row in data:
        l = int(len(row) / 2)
        first = row[0:l] 
        second = row[l:]
        chartoadd = ""
        for c1 in first:
            for c2 in second:
                if c1 == c2:
                    chartoadd = c1
        same.append(chartoadd)
    
    for c in same:
        res += pointsdict[c]

    return res

def mainadv(data):
    res = 0
    pointsdict = {}
    for v,k in enumerate ( string.ascii_lowercase):
        pointsdict[k] = v + 1

    for v,k in enumerate ( string.ascii_uppercase):
        pointsdict[k] = v + 27
    
    low = 0
    high = 3
    
    for i in range(0, int(len(data) / 3)):
        rows = data[low:high]
        samedict = defaultdict(int)
        print(rows)
        for row in rows:
            srow = set(row)
            for c in srow:
                samedict[c] += 1
        for c in samedict:
            if samedict[c] == 3:
                print(c)
                print(samedict)
                res += pointsdict[c]
        low += 3
        high += 3

    return res


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
    print(mainadv(testdata))
    print(mainadv(data))
