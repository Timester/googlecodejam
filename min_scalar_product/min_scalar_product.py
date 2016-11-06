__author__ = 'imre'

cases = []


class Case:
    def __init__(self, vector_a, vector_b, size):
        self.vector_a = vector_a
        self.vector_b = vector_b
        self.size = size

    def min_scalar_product(self):
        self.vector_a = sorted(self.vector_a)
        self.vector_b = sorted(self.vector_b, reverse=True)

        added = [self.vector_a[i] * self.vector_b[i] for i in range(self.size)]

        return sum(added)


def read_input(filename):
    file = open(filename, "r")

    fsize = int(file.readline())

    for i in range(fsize):
        size = int(file.readline())

        vector_a = [int(n) for n in file.readline().split()]
        vector_b = [int(n) for n in file.readline().split()]

        cases.append(Case(vector_a, vector_b, size))

read_input('./A-large-practice.in')

for i in range(len(cases)):
    print('Case #' + str(i + 1) + ': ' + str(cases[i].min_scalar_product()))