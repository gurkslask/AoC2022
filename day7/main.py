import re
import os
from collections import namedtuple, defaultdict


def main(data):
    file = namedtuple('file', ("name", "size"))
    directories = {}
    active_directory = ""
    res = 0
    for row in data:
        srow = row.split(' ')
        if row[0] == '$':

            if srow[1] == "ls":
                pass

            elif srow[1] == "cd":
                if srow[2] == "..":

                    try:
                        active_directory = directories[active_directory]["parent"]
                    except KeyError:
                        pass
                else:
                    directories[srow[2]] = {"name": srow[1], "parent": active_directory, "files": [], "subdirs": []} 
                    active_directory = srow[2]
        else:
            if srow[0] == "dir":
                directories[active_directory]["subdirs"].append(srow[1])
            else:
                act_file = file(srow[1], srow[0])
                directories[active_directory]["files"].append(act_file)

    for d in directories:
        s = sum_dirs(directories, d)
        # result = sum(int(i.size) for i in directories[d]["files"])
        # print(d + str(s))
        print(d + str(s))
        if s < 100_000:
            res += s
    return res

def sum_dirs(dirs, dir) -> int:
    result = 0
    # print(dir)

    for d in dirs[dir]["subdirs"]:
        result += sum_dirs(dirs, d)
    result += sum(int(i.size) for i in dirs[dir]["files"])
    return result


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
    # print(main(testdata))
    print(main(data))
