import abc
from colorama import init, Fore
init(autoreset=True)


class ChessPiece(metaclass=abc.ABCMeta):

    def __init__(self, c, x, y, name):
        self.c = c # 1-red
        self.x = x # (x, y) coordinate
        self.y = y
        self.name = name

    @abc.abstractmethod
    def move(self, x_move, y_move):
        """ chess piece move methon"""

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


class Pawn(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '卒' if c else '兵')


    def move(self, x_move, y_move):
        self.x += x_move
        self.y += y_move


class King(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '将' if c else '帅')


    def move(self, x_move, y_move):
        pass


class Chariot(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '车' if c else '車')


    def move(self, x_move, y_move):
        pass


class Horse(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '马')

    def move(self, x_move, y_move):
        pass


class Elephant(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '象' if c else '相')

    def move(self, x_move, y_move):
        pass


class Adviser(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '士' if c else '仕')

    def move(self, x_move, y_move):
        pass


class Cannon(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '炮')

    def move(self, x_move, y_move):
        pass