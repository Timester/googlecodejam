__author__ = 'imre'

cases = []

class Case:
    def __init__(self, field):
        self.field = field

    def print_game_state(self):
        for c in ['X', 'O']:
            windiagonal1 = True
            windiagonal2 = True
            
            for x in range(4):
                winhorizontal = True
                winvertical = True
                
                for y in range(4):
                    if self.field[y][x] != c and self.field[y][x] != 'T': 
                        winvertical = False
                        
                    if self.field[x][y] != c and self.field[x][y] != 'T': 
                        winhorizontal = False
                        
                if winhorizontal or winvertical: 
                    print(c + ' won')
                
                if self.field[x][x] != c and self.field[x][x] != 'T': 
                    windiagonal1 = False
                    
                if self.field[3 - x][x] != c and self.field[3 - x][x] != 'T': 
                    windiagonal2 = False
                    
            if windiagonal1 or windiagonal2: 
                print(c + ' won')

        for x in range(4):
            for y in range(4):
                if self.field[y][x] == '.': 
                    print('Game has not completed')

        print('Draw')


def read_input(filename):
    file = open(filename, "r")

    fsize = int(file.readline())

    for i in range(fsize):
        field = []
        for j in range(4):
            field.append(list(file.readline()))

        cases.append(Case(field))
        file.readline()


read_input('./A-small-practice.in')

for case in cases:
    case.print_game_state()