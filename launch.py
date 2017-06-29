from chessboard import *


class Launch:
    row = '{}__' * 8 + '{}'
    line = '|   ' * 8 + '|'
    confine = "|      楚河             汉界    |"

    def __init__(self):
        self.chessboard = [['__' for i in range(9)] for i in range(10)]
        self.initialization()


    def initialization(self):
        pawn=((0, 3, 0), (0, 3, 2), (0, 3, 4), (0, 3, 6), (0, 3, 8), (1, 6, 0), (1, 6, 2), (1, 6, 4), (1, 6, 6), (1, 6, 8))
        king=((0, 0, 4), (1, 9, 4))
        chariot=((0, 0, 0), (0, 0, 8), (1, 9, 0), (1, 9, 8))
        horse=((0, 0, 1), (0, 0, 7), (1, 9, 1), (1, 9, 7))
        elephant=((0, 0, 2), (0, 0, 6), (1, 9, 2), (1, 9, 6))
        adviser=((0, 0, 3), (0, 0, 5), (1, 9, 3), (1, 9, 5))
        cannon=((0, 2, 1), (0, 2, 7), (1, 7, 1), (1, 7, 7))
        pa = [Pawn(c, x, y) for c, x, y in pawn]
        ki = [King(c, x, y) for c, x, y in king]
        ch = [Chariot(c, x, y) for c, x, y in chariot]
        ho = [Horse(c, x, y) for c, x, y in horse]
        el = [Elephant(c, x, y) for c, x, y in elephant]
        ad = [Adviser(c, x, y) for c, x, y in adviser]
        ca = [Cannon(c, x, y) for c, x, y in cannon]
        for ms in pa, ki, ch, ho, el, ad, ca:
            for m in ms:
                self.chessboard[m.x][m.y] = m


    def show(self):
        for i in range(10):
            print(self.row.format(*self.chessboard[i]))
            if i == 4:
                print(self.confine)
            elif i != 9 :
                print(self.line)



if __name__ == "__main__":
    l = Launch()
    l.show()