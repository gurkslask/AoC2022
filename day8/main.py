import re
import os


def main(data):
    trees = [[f for f in c]for c in data]
    vis = [[False for f in c]for c in data]
    # [rad][kolumn]
    tl = len(trees) - 1

    # Check from left
    for row in range(len(trees)):
        for col in range(len(trees)):
            if col == 0:
                vis[row][col] = True
                continue
            if max(trees[row][0:col]) < trees[row][col]:
                vis[row][col] = True
    # Check from right
    for row in range(len(trees)):
        for col in range(len(trees)):
            inverted_col = tl - col 
            if col == 0:
                vis[row][inverted_col] = True
                continue
            if max(trees[row][inverted_col + 1 : len(trees)]) < trees[row][inverted_col]:
                vis[row][inverted_col] = True
    # Check from top
    for row in range(len(trees)):
        for col in range(len(trees)):
            if row == 0:
                vis[row][col] = True
            else:
                mm = max([trees[i][col] for i in range(row)])
                num = trees[row][col]
                if mm < num:
                    vis[row][col] = True

    # Check from bottom
    for col in range(len(trees)):
        for row in range(len(trees)):
            inverted_row = tl - row 
            if row == 0:
                vis[inverted_row][col] = True
            else:
                mm = max([trees[tl - i][col] for i in range(row)])
                num = trees[inverted_row][col]
                if mm < num:
                    vis[inverted_row][col] = True

    res = 0
    # print(" HERE COMES GRID")
    for row in vis: 
        # print("-------")
        # print(row)
        for col in row:
            if col: res+=1
    return res

def mainadv(data):
    trees = [[f for f in c]for c in data]
    vis = [[0 for f in c]for c in data]
    viss = [[[] for f in c]for c in data]
    lt = len(trees)
    # [rad][kolumn]
    for row in range(lt):
        for col in range(lt):
            l = []
            l.append(checkUp(trees, row, col))
            l.append(checkDown(trees, row, col))
            l.append(checkRight(trees, row, col))
            l.append(checkLeft(trees, row, col))
            vis[row][col] = l[0] * l[1] * l[2] * l[3]
            viss[row][col].append(l)


    """for row in range(lt):
        print("--------")
        print(viss[row])
    for row in range(lt):
        print("--------")
        print(vis[row])"""
    m = []
    for i in range(lt):
        for j in range(lt):
            m.append(vis[i][j])
    return max(m)

            

def checkUp(trees, row, col):
    height = trees[row][col]
    nrow = row - 1
    lt = len(trees)
    res = 0
    done = False
    while not done:
        if 0 <= nrow < lt:
            new_tree = trees[nrow][col]
            res += 1
            if new_tree >= height and not done:
                done = True
            elif not done:
                nrow -= 1
        else:
            done = True
    return res
def checkDown(trees, row, col):
    height = trees[row][col]
    nrow = row + 1
    lt = len(trees)
    res = 0
    done = False
    while not done:
        if 0 <= nrow < lt:
            new_tree = trees[nrow][col]
            res += 1
            if new_tree >= height and not done:
                done = True
            elif not done:
                nrow += 1
        else:
            done = True
    return res
def checkLeft(trees, row, col):
    height = trees[row][col]
    ncol = col + 1
    lt = len(trees)
    res = 0
    done = False
    while not done:
        if 0 <= ncol < lt:
            new_tree = trees[row][ncol]
            res += 1
            if new_tree >= height and not done:
                done = True
            elif not done:
                ncol += 1
        else:
            done = True
    return res
def checkRight(trees, row, col):
    height = trees[row][col]
    ncol = col - 1
    lt = len(trees)
    res = 0
    done = False
    while not done:
        if 0 <= ncol < lt:
            new_tree = trees[row][ncol]
            res += 1
            if new_tree >= height and not done:
                done = True
            elif not done:
                ncol -= 1
        else:
            done = True
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
