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

def mainadv(data):
    win = 6
    draw = 3
    # X = Rock, Y = Paper, Z = Scissor
    shape = {'X': 1, 'Y': 2, 'Z': 3}
    outcomes = {
        'A': {'X': 3, 'Y': 6, 'Z': 0}, # rock
        'B': {'X': 0, 'Y': 3, 'Z': 6}, # paper
        'C': {'X': 6, 'Y': 0, 'Z': 3}, # Scissor
    }
    needToDo = {
        'Y' : 3, # Draw
        'X' : 0, # Lose
        'Z' : 6, # Win
    }
    score = 0
    for row in data:
        rr = row.split(' ')

        need = needToDo[rr[1]]
        key = get_key(need, outcomes[rr[0]])
        chosenShape = outcomes[rr[0]][key]

        print(key)
        score += shape[key]
        score += outcomes[rr[0]][key]


    return score


def getdata(path):
    with open(path) as f:
        data = f.readlines()
        data = [i.replace('\n', '') for i in data]
    return data

def get_key(val, d):
    for key, value in d.items():
        if val == value:
            return key

if __name__ == '__main__':

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    data = getdata('./input.txt')
    testdata = getdata('./testinput.txt')
    print("Test: {}", main(testdata))
    print("Main: {}", main(data))
    print("Advanced Test: {}", mainadv(testdata))
    print("Advanced main: {}", mainadv(data))
