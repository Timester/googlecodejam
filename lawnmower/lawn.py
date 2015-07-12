__author__ = 'imre'


matrices = []


def readinput(filepath):
    file = open(filepath, "r")

    fsize = int(file.readline())

    for i in range(fsize):
        matdimensions = file.readline().split()

        rows = int(matdimensions[0])
        cols = int(matdimensions[1])
        matrix = [[0 for x in range(cols)] for x in range(rows)]

        for j in range(rows):
            currentrow = file.readline().split()
            matrix[j] = [int(k) for k in currentrow]

        matrices.append(matrix)


def checkmatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != max(mat[i]): # if the row is wrong
                for k in range(len(mat)):
                    if mat[k][j] > mat[i][j]: # if the column is also wrong
                        return False

    return True


def write_case(f, i, res):
    f.write('Case #%d: ' % i)
    f.write('%s' % res)
    f.write('\n')


def checkmatrices():
    with open("result.out", "a") as fo:

        for i in range(len(matrices)):
            res = checkmatrix(matrices[i])

            if res:
                write_case(fo, i + 1, "YES")
            else:
                write_case(fo, i + 1, "NO")

readinput("B-small-practice.in")

checkmatrices()
