__author__ = 'imre'

cases = []


class Case:
    def __init__(self, idx, lines):
        self.idx = idx
        self.lines = lines


def read_input(filename):
    file = open(filename, "r")

    fsize = int(file.readline())

    for i in range(fsize):
        song_count = int(file.readline())
        lines = []

        for j in range(song_count):
            lines.append(file.readline())

        cases.append(Case(i + 1, lines))


read_input('./B-small-practice-1.in')

print(cases)
