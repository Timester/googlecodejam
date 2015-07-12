__author__ = 'imre'


size = 0
cases = []


def readinput(filepath):
    file = open(filepath, "r")

    fsize = int(file.readline())

    for i in range(0, fsize):
        case = {}
        line = file.readline().split()

        case["C"] = float(line[0])
        case["F"] = float(line[1])
        case["X"] = float(line[2])

        cases.append(case)


def computecase(case):
    runs = 0
    currentrate = 2
    finishtime = case["X"] / currentrate
    finishforc = case["C"] / currentrate

    while runs <= 100:
        currentrate += case["F"]
        finishtimetemp = (case["X"] / currentrate) + finishforc
        finishforc += case["C"] / currentrate

        if finishtimetemp < finishtime:
            finishtime = finishtimetemp

        runs += 1

    return finishtime


def computecases():
    caseno = 0
    for a in cases:
        res = computecase(a)

        with open("result.out", "a") as fo:
            write_case(fo, caseno, res)

        caseno += 1


def write_case(f, i, res):
    f.write('Case #%d: ' % i)
    f.write('%s' % res)
    f.write('\n')

readinput("/home/imre/PycharmProjects/googlecodejam/tiny")
computecases()
