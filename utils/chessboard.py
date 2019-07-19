import abc
from colorama import init, Fore
init(autoreset=True)


class ChessPiece(metaclass=abc.ABCMeta):
    _step = ('一', '二', '三', '四', '五', '六', '七', '八', '九')
    _dt = {'进': -1, '退': 1, '平': 0}

    def __init__(self, c, x, y, name):
        self.c = c  #1-red
        self.x = x  #(x, y) coordinate
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

    def filter(self, name):
        if self.c == 1 and self.name == name:
            return True
        return False

    @abc.abstractmethod
    def step(self, direct, step, board):
        """pawn king chariot cannon"""
        if direct not in self._dt.keys():
            return False, KeyError
        x_move, y_move = 0, 0
        if step in self._step:
            x_move = self._dt[direct] * (self._step.index(step) + 1)
            if direct == '平':
                y_move = 8 - self._step.index(step) - self.y
        else:
            try:
                x_move = self._dt[direct] * int(step)
                if direct == '平':
                    y_move = 9 - int(step) - self.y
            except ValueError:
                return False, ValueError
        return True, x_move, y_move

    @abc.abstractmethod
    def rule(self, x_move, y_move, board):
        """chess rule"""


class Pawn(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '卒' if c else '兵')

    def step(self, direct, step, board):
        st = super().step(direct, step, board)
        if st[0] and self.rule(st[1], st[2], board):
            return st
        return False, 'rule failed'

    def rule(self, x_move, y_move, board):
        if self.x > 4 and y_move != 0:
            return False
        if x_move != -1 and abs(y_move) != 1:
            return False
        if self.x + x_move < 0:
            return False
        return True


class King(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '将' if c else '帅')

    def step(self, direct, step, board):
        st = super().step(direct, step, board)
        if st[0] and self.rule(st[1], st[2], board):
            return st
        return False, 'rule failed'

    def rule(self, x_move, y_move, board):
        if abs(x_move) > 1 or abs(y_move) > 1:
            return False
        if not 7 <= self.x + x_move < 10:
            return False
        if not 3 <= self.y + y_move < 6:
            return False
        if y_move != 0:
            targets = [target[self.y+y_move] for target in board[0: self.x] if isinstance(target[self.y+y_move], ChessPiece)]
            if targets[-1].name == '帅':
                return False
        return True


class Chariot(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '车' if c else '車')

    def step(self, direct, step, board):
        st = super().step(direct, step, board)
        if st[0] and self.rule(st[1], st[2], board):
            return st
        return False, 'rule failed'

    def rule(self, x_move, y_move, board):
        if not 0 <= self.x + x_move < 10:
            return False
        if x_move == 0:
            if y_move > 0:
                targets = board[self.x][self.y: self.y+y_move][1:]
            else:
                targets = board[self.x][self.y+y_move: self.y][1:]
            for target in targets:
                if isinstance(target, ChessPiece):
                    return False
        else:
            if x_move > 0:
                targets = board[self.x: self.x+x_move][1:]
            else:
                targets = board[self.x+x_move: self.x][1:]
            for target in targets:
                if isinstance(target[self.y], ChessPiece):
                    return False
        return True


class Cannon(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '炮' if c else '砲')

    def step(self, direct, step, board):
        st = super().step(direct, step, board)
        if st[0] and self.rule(st[1], st[2], board):
            return st
        return False, 'rule failed'

    def rule(self, x_move, y_move, board):
        if not 0 <= self.x + x_move < 10:
            return False
        if x_move == 0:
            if y_move > 0:
                targets = board[self.x][self.y: self.y + y_move][1:]
            else:
                targets = board[self.x][self.y + y_move: self.y][1:]
            t = [0 for target in targets if isinstance(target, ChessPiece)]
            target = board[self.x][self.y+y_move]
            if isinstance(target, ChessPiece) and target.c == 0:
                if len(t) != 1:
                    return False
            else:
                if len(t) != 0:
                    return False
        else:
            if x_move > 0:
                targets = board[self.x: self.x + x_move][1:]
            else:
                targets = board[self.x + x_move: self.x][1:]
            t = [0 for target in targets if isinstance(target[self.y], ChessPiece)]
            target = board[self.x+x_move][self.y]
            if isinstance(target, ChessPiece) and target.c == 0:
                if len(t) != 1:
                    return False
            else:
                if len(t) != 0:
                    return False
        return True


class Horse(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '马' if c else '馬')

    def step(self, direct, step, board):
        if direct not in super()._dt.keys():
            return False
        if step in super()._step:
            y_move = 8 - self._step.index(step) - self.y
        else:
            try:
                y_move = 9 - int(step) - self.y
            except ValueError:
                return False, ValueError
        x_move = super()._dt[direct] * (3 - abs(y_move))
        if self.rule(x_move, y_move, board):
            return True, x_move, y_move
        return False, 'rule failed'

    def rule(self, x_move, y_move, board):
        if (abs(x_move), abs(y_move)) == (1, 2) or (abs(x_move), abs(y_move)) == (2, 1):
            pass
        else:
            return False
        if not 0 <= self.x + x_move < 10:
            return False
        if abs(x_move) > abs(y_move):
            x = self.x + int(int(x_move)/2)
            y = self.y
        else:
            x = self.x
            y = self.y + int(int(y_move)/2)
        if isinstance(board[x][y], ChessPiece):
            return False
        return True


class Elephant(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '象' if c else '相')

    def step(self, direct, step, board):
        if direct not in super()._dt.keys():
            return False
        x_move = super()._dt[direct] * 2
        if step in super()._step:
            y_move = 8 - self._step.index(step) - self.y
        else:
            try:
                y_move = 9 - int(step) - self.y
            except ValueError:
                return False, ValueError
        if self.rule(x_move, y_move, board):
            return True, x_move, y_move
        return False, 'rule failed'

    def rule(self, x_move, y_move, board):
        if abs(y_move) != 2:
            return False
        if not 5 <= self.x + x_move < 10:
            return False
        if isinstance(board[self.x + int(int(x_move)/2)][self.y + int(int(y_move)/2)], ChessPiece):
            return False
        return True


class Adviser(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '士' if c else '仕')

    def step(self, direct, step, board):
        if direct not in super()._dt.keys():
            return False
        x_move = super()._dt[direct] * 1
        if step in super()._step:
            y_move = 8 - self._step.index(step) - self.y
        else:
            try:
                y_move = 9 - int(step) - self.y
            except ValueError:
                return False, ValueError
        if self.rule(x_move, y_move, None):
            return True, x_move, y_move
        return False, 'rule failed'

    def rule(self, x_move, y_move, board):
        if abs(x_move) != 1 or abs(y_move) != 1:
            return False
        if not 7 <= self.x + x_move < 10:
            return False
        if not 3 <= self.y + y_move < 6:
            return False
        return True
