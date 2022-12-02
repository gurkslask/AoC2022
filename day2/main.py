import re
import os


def main(data):
    win = 6
    draw = 3
    # X = Rock, Y = Paper, Z = Scissor
    shape = {'X': 1, 'Y': 2, 'Z': 3}
    outcomes = {
        'A': {'X': 3, 'Y': 6, 'Z': 0}, # rock
        'B': {'X': 0, 'Y': 3, 'Z': 6}, # paper
        'C': {'X': 6, 'Y': 0, 'Z': 3}, # Scissor
    }
    score = 0
    for row in data:
        rr = row.split(' ')
        score += shape[rr[1]]
        score += outcomes[rr[0]][rr[1]]
    return score

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
    print("Test: {}", main(testdata))
    print("Main: {}", main(data))
