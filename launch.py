from chessboard import *


class Launch:
    row = '{}__' * 8 + '{}'
    line = '|   ' * 8 + '|'
    confine = "|      楚河             汉界    |"

    red_name = ('将', '车', '马', '象', '士', '炮', '卒')
    black_name = ('帅', '車', '馬', '相', '仕', '砲', '兵')
    __step = ('一', '二', '三', '四', '五', '六', '七', '八', '九')
    __direct = ('进', '退', '平')
    special = ('前', '后')

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

    def analysis(self, pace):
        if len(pace) != 4:
            return False, 'error Please input again'
        if pace[0] in self.special:
            pass
        # chess name
        try:
            name = pace[0] if pace[0] in self.red_name else self.red_name[self.black_name.index(pace[0])]
        except ValueError:
            return False, 'name error'
        # location y
        if pace[1] in self.__step:
            y = 8 - self.__step.index(pace[1])
        else:
            try:
                y = 9 - int(pace[1])
            except ValueError:
                return False, 'value error'
            else:
                if 0 < y > 8:
                    return False, 'out of range'
        # target chess
        target = [i[y] for i in self.chessboard if isinstance(i[y], ChessPiece) and i[y].filter(y, name)]
        if len(target) != 1:
            return False, 'multiple matching'
        tar = target[0].step(pace[2], pace[3])
        if tar[0]:
            return True, target[0], tar[1], tar[2]
        else:
            return False, 'step error'

    def move(self, m, x_move, y_move):
        self.chessboard[m.x][m.y] = '__'
        m.move(x_move, y_move)
        self.chessboard[m.x][m.y] = m




if __name__ == "__main__":
    l = Launch()
    an = l.analysis('车一进一')
    if an[0]:
        _, m, x_move, y_move = an
        l.move(m, x_move, y_move)
    an = l.analysis('马二进三')
    if an[0]:
        _, m, x_move, y_move = an
        l.move(m, x_move, y_move)
    an = l.analysis('炮二平五')
    if an[0]:
        _, m, x_move, y_move = an
        l.move(m, x_move, y_move)
    l.show()