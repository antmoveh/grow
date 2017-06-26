import abc


class ChessPiece(metaclass=abc.ABCMeta):

    def __init__(self, c, x, y, name):
        self.c = c # 0-red, 1-black
        self.x = x # (x, y) coordinate
        self.y = y
        self.name = name

    @abc.abstractmethod
    def move(self, x_move, y_move):
        """ chess piece move methon"""

    def __repr__(self):
        return self.name


class Soldier(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '卒' if c else '兵')


    def move(self, x_move, y_move):
        pass


class General(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '将' if c else '帅')


    def move(self, x_move, y_move):
        pass


class Vehicle(ChessPiece):

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


class Officer(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '士' if c else '仕')

    def move(self, x_move, y_move):
        pass


class Cannon(ChessPiece):

    def __init__(self, c, x, y):
        super().__init__(c, x, y, '炮')

    def move(self, x_move, y_move):
        pass

if __name__ == '__main__':
    s = Soldier(0, 1, 2)
    g = General(0, 0, 4)
    v = Vehicle(1, 0, 0)
    h = Horse(0, 0, 1)
    e = Elephant(0, 0, 3)
    o = Officer(0, 0, 4)
    c = Cannon(0, 0, 5)
    print(s, g, v, h, e, o, c)