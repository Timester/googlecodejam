__author__ = 'imre'

cases = []


class Case:
    def __init__(self, paths, existing):
        self.paths = paths
        self.existing = paths[:existing]
        self.to_be_created = paths[existing:]

    def count_mkdirs(self):
        all_needed_paths = set()

        for path in self.to_be_created:
            folders = list(filter(None, path.split('/')))
            for i in range(len(folders)):
                all_needed_paths.add('/' + '/'.join(folders[:i+1]).rstrip())

        mkdirs = 0

        for path in all_needed_paths:
            if path not in self.existing:
                mkdirs += 1

        return mkdirs


def read_input(filename):
    file = open(filename, "r")

    fsize = int(file.readline())

    for i in range(fsize):
        path_counts = file.readline().split()
        paths = []
        for j in range(int(path_counts[0]) + int(path_counts[1])):
            paths.append(file.readline())

        cases.append(Case(paths, int(path_counts[0])))


read_input('A-small-practice.in')

for case in cases:
    print(str(case.count_mkdirs()))