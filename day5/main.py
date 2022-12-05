import re
import os
import string
import collections


def main(data):
    move = collections.namedtuple('move', ['fromm', 'too', 'num'])
    moves = []
    crates = collections.defaultdict(list)

    second_half = False
    for row in data:
        print(row)
        if not second_half:
            if len(row) < 1:
                second_half = True
                continue
            if row[1] in string.digits:
                continue
            else: 
                for i in range(int(len(row)/3)):
                    print(i)
                    try:
                        letter = row[(i * 4) + 1]
                    except IndexError:
                        print("ie")
                    print(letter)
                    if letter in string.ascii_uppercase:
                        crates[i + 1].append(letter)
        if second_half:
            for key, char in enumerate(row):
                if char in string.digits:
                    if key <= 9:
                        num = int(char)
                    if key <= 16:
                        fromm = int(char)
                    if key > 16:
                        too = int(char)
            m = move(fromm, too, num)
            moves.append(m)
    
    for c in crates:
        crates[c].reverse()

    # print(crates)
    for m in moves:
        crates = crane(crates=crates, move=m)
    # print(crates)

    res = []

    for i in range(len(crates)):
        res.append(crates[i+1][-1]) 

    return "".join(res)

def crane(crates: collections.defaultdict(list), move: collections.namedtuple) -> collections.defaultdict:
    # print("BBRRRRR CRANE GO")
    # print(f"move {move}")
    for i in range(int(move.num)):
        # print(f"Crates before move {crates}")
        c = crates[move.fromm].pop()
        crates[move.too].append(c)
        # print(f"Crates after move {crates}")
    return crates

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
