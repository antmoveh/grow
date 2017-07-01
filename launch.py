from chessboard import *
import os


class Launch:
    row = '{}__' * 8 + '{}'
    line = '|   ' * 8 + '|'
    confine = "|      楚河             汉界    |"

    red_name = ('将', '车', '马', '象', '士', '炮', '卒')
    black_name = ('帅', '車', '馬', '相', '仕', '砲', '兵')
    __step = ('一', '二', '三', '四', '五', '六', '七', '八', '九')
    __special = {'前': 1, '后': -1}

    def __init__(self):
        self.chessboard = self.board()

    def board(self):
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
        board = [['__' for i in range(9)] for i in range(10)]
        for ms in pa, ki, ch, ho, el, ad, ca:
            for m in ms:
                board[m.x][m.y] = m
        return board

    def show(self):
        while True:
            os.system('cls')
            # output chess board
            for i in range(10):
                print(self.row.format(*self.chessboard[i]))
                if i == 4:
                    print(self.confine)
                elif i != 9:
                    print(self.line)
            print("\n"*2)
            pace = input("请输入步法: ")
            if pace == 'exit':
                break
            self.move(self.conversion(pace))

    # 将术语转换为操作对象和坐标
    def conversion(self, pace):
        if len(pace) != 4:
            return False, 'error Please input again'
        if pace[0] in self.__special.keys():
            pace0 = pace[1]
        else:
            pace0 = pace[0]
        # chess name
        try:
            name = pace0 if pace0 in self.red_name else self.red_name[self.black_name.index(pace0)]
        except ValueError:
            return False, 'name error'
        if pace[0] in self.__special.keys():
            for i in list(range(0, 10)[::self.__special[pace[0]]]):
                for j in self.chessboard[i]:
                    if isinstance(j, ChessPiece) and j.filter(name):
                        target = j
                        return True, target, pace[2], pace[3]
            return False, KeyError
        # location y
        if pace[1] in self.__step:
            y = 8 - self.__step.index(pace[1])
        else:
            try:
                y = 9 - int(pace[1])
            except ValueError:
                return False, 'value error'
        # target chess
        target = [i[y] for i in self.chessboard if isinstance(i[y], ChessPiece) and i[y].filter(name)]
        if len(target) != 1:
            return False, 'multiple matching'
        return True, target[0], pace[2], pace[3]


    def move(self, con):
        if not con[0]:
            return
        _, m, pace2, pace3 = con
        tar = m.step(pace2, pace3)
        if tar[0]:
            _, x_move, y_move = tar
            self.chessboard[m.x][m.y] = '__'
            m.move(x_move, y_move)
            self.chessboard[m.x][m.y] = m


if __name__ == "__main__":
    Launch().show()
