import abc
from colorama import init, Fore
init(autoreset=True)


class ChessPiece(metaclass=abc.ABCMeta):
    _step = ('一', '二', '三', '四', '五', '六', '七', '八', '九')
    _dt = {'进': -1, '退': 1, '平': 0}

    def __init__(self, c, x, y, name):
        self.c = c # 1-red
        self.x = x # (x, y) coordinate
        self.y = y
        self.name = name

    def move(self, x_move, y_move):
        """ chess piece move methon"""
        self.x += x_move
        self.y += y_move

    def __repr__(self):
        if self.c == 1:
            return Fore.LIGHTRED_EX + self.name + Fore.RESET
        return self.name

    def coord(self):
        return self.x, self.y

    def filter(self, y, name):
        if self.c == 1 and self.y==y and self.name==name:
            return True
        return False

    @abc.abstractmethod
    def step(self, direct, step):
        """pawn king chariot cannon"""
        if direct not in self._dt.keys():
            return False
        x_move, y_move = 0, 0
        if step in self._step:
            x_move = self._dt[direct] * (self._step.index(step) + 1)
            if direct == '平':
                y_move = (8-self._step.index(step)) - self.y
        else:
            try:
                x_move = self._dt[direct] * int(step)
                if direct == '平':
                    y_move = (9-int(step)) - self.y
            except ValueError:
                return False
        return True, x_move, y_move


class Pawn(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '卒' if c else '兵')

    def step(self, direct, step):
        return super().step(direct, step)


class King(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '将' if c else '帅')

    def step(self, direct, step):
        return super().step(direct, step)


class Chariot(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '车' if c else '車')

    def step(self, direct, step):
        return super().step(direct, step)

class Horse(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '马' if c else '馬')

    def step(self, direct, step):
        if direct not in super()._dt.keys():
            return False
        x_move = super()._dt[direct] * 2
        y_move = super()._dt[direct] * 1
        return True, x_move, y_move


class Elephant(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '象' if c else '相')

    def step(self, direct, step):
        if direct not in super()._dt.keys():
            return False
        x_move = super()._dt[direct] * 2
        y_move = super()._dt[direct] * 2
        return True, x_move, y_move


class Adviser(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '士' if c else '仕')

    def step(self, direct, step):
        if direct not in super()._dt.keys():
            return False
        x_move = super()._dt[direct] * 2
        y_move = super()._dt[direct] * 2
        return True, x_move, y_move


class Cannon(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '炮' if c else '砲')

    def step(self, direct, step):
        return super().step(direct, step)