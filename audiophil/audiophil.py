__author__ = 'imre'

class Task:
    def __init__(self, lines):
        self.lines = lines


def read_input(filename):
    file = open(filename, "r")

    fsize = int(file.readline())

    lines = []

    for i in range(fsize):
        lines.append(file.readline())


tasks = []
