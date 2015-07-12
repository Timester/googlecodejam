__author__ = 'szeiler'


class Matrix:

    def __init__(self, rows, cols):
        self.matrix = [[0 for x in range(cols)] for x in range(rows)]
        self.rows = rows
        self.cols = cols


def read_file():
    inputfile = open("/home/imre/PycharmProjects/googlecodejam/lawnmower/B-small-practice.in", "r")

    number_of_matrices = int(inputfile.readline())

    matrices = []

    for i in range(number_of_matrices):
        size = inputfile.readline()
        rows = int(size.split(" ")[0])
        cols = int(size.split(" ")[1])

        matrix = Matrix(rows, cols)
        for j in range(rows):
            row = inputfile.readline().split()

            for k in range(cols):
                matrix.matrix[j][k] = row[k]

        matrices.append(matrix)

    return matrices


def examine_matrix(matrix):
    for i in range(matrix.rows):
            for j in range(matrix.cols):
                vertical = True
                horizontal = True

                for k in range(matrix.cols):
                    if matrix.matrix[i][k] > matrix.matrix[i][j]:
                        horizontal = False
                        break

                for k in range(matrix.rows):
                    if matrix.matrix[k][j] > matrix.matrix[i][j]:
                        vertical = False
                        break

                if not horizontal and not vertical:
                    return "NO"

    return "YES"


def solve(matrices):

    out_file = open("output.txt", "w")

    for i in range(len(matrices)):
        out_file.write(str(i+1) + ": " + str(examine_matrix(matrices[i])) + "\n")


def main():
    matrices = read_file()

    solve(matrices)


main()
