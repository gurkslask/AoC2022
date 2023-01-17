import re
import os


def main(data):
    # x, y
    # row, col
    l = 5
    H = [l,0]
    T = [l,0]
    grid = [["" for k in range(l + 1)] for i in range(l + 1)]
    grid[H[0]][H[1]] = "H"
    grid[T[0]][T[1]] = "T"
    for inputs in data:
        print(inputs)
        spl = inputs.split(" ")
        spl[1] = int(spl[1])
        old_pos = H
        if grid[old_pos[0]][old_pos[1]] == "H":
            grid[old_pos[0]][old_pos[1]] = ""
        # Up
        if spl[0] == "U":
            H[0] -= spl[1]
        elif spl[0] == "D":
            H[0] += spl[1]
        elif spl[0] == "L":
            H[1] -= spl[1]
        elif spl[0] == "R":
            H[1] += spl[1]
        
        grid[H[0]][H[1]] = "H"
        for row in range(l):
            print(grid[row])
        
        # Tail logic

        # Check if we are diagonal

        if not(H[0] == T[0] or H[1] == T[1]):
            if spl[0] in ["L", "R"]:
                T[0] = H[0]
            if spl[0] in ["D", "U"]:
                T[1] = H[1]


        # Head is too high
        if H[0] < T[0] - 1:
            T[0] = T[0] + ((T[0] - H[0]) - 1)
        # Head is too low
        if H[0] > T[0] + 1:
            T[0] = T[0] - ((T[0] - H[0]) + 1)
        # Horizontal
        if H[1] < T[1] - 1:
            T[1] = T[1] + ((T[1] - H[1]) - 1)
        if H[1] > T[1] + 1:
            T[1] = T[1] - ((T[1] - H[1]) + 1)
        


        Last_step = spl[0]


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
    main(testdata)
