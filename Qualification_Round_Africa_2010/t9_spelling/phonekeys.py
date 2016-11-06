__author__ = 'imre'

keys = {}
keys_smaller = {}
messages = []


def initkeys():
    keys["a"] = "2"
    keys["b"] = "22"
    keys["c"] = "222"
    keys["d"] = "3"
    keys["e"] = "33"
    keys["f"] = "333"
    keys["g"] = "4"
    keys["h"] = "44"
    keys["i"] = "444"
    keys["j"] = "5"
    keys["k"] = "55"
    keys["l"] = "555"
    keys["m"] = "6"
    keys["n"] = "66"
    keys["o"] = "666"
    keys["p"] = "7"
    keys["q"] = "77"
    keys["r"] = "777"
    keys["s"] = "7777"
    keys["t"] = "8"
    keys["u"] = "88"
    keys["v"] = "888"
    keys["w"] = "9"
    keys["x"] = "99"
    keys["y"] = "999"
    keys["z"] = "9999"
    keys[" "] = "0"

    keys_smaller["abc"] = 2
    keys_smaller["def"] = 3
    keys_smaller["ghi"] = 4
    keys_smaller["jkl"] = 5
    keys_smaller["mno"] = 6
    keys_smaller["pqrs"] = 7
    keys_smaller["tuv"] = 8
    keys_smaller["wxyz"] = 9
    keys_smaller[" "] = 0


def cehckifsamekey(a, b):
    key_for_a = ""
    key_for_b = ""

    for key in keys_smaller.keys():
        if a in key:
            key_for_a = key

        if b in key:
            key_for_b = key

    if key_for_a == key_for_b:
        return True

    return False


def translate(string):
    result = ""
    prevletter = "1"
    for letter in string:
        if cehckifsamekey(letter, prevletter):
            result += " "

        result += keys[letter]
        prevletter = letter

    return result


def write_case(f, i, res):
    f.write('Case #%d: ' % i)
    f.write('%s' % res)
    f.write('\n')


def translate_all():
    with open("result.out", "a") as fo:

        for i in range(0, len(messages)):
            write_case(fo, i + 1, translate(messages[i]))


def read_input(filepath):
    file = open(filepath, "r")

    fsize = int(file.readline())

    for i in range(0, fsize):
        messages.append(file.readline().rstrip('\n'))


initkeys()
read_input("./C-small-practice.in")
translate_all()