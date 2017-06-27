from chessboard import *
import collections
import logging


class Launch:

    def __init__(self):
        self.chessboard = None
        pass


    def initialization(self):
        chess = collections.namedtuple('chess',
                                       ['soldier', 'general', 'vehicle', 'horse', 'elephant', 'officer', 'cannon'])
        cinit = chess(
            soldier=((0, 3, 0), (0, 3, 2), (0, 3, 4), (0, 3, 6), (0, 3, 8), (1, 6, 0), (1, 6, 2), (1, 6, 4),
                     (1, 6, 6), (1, 6, 8)), general=((0, 0, 4), (1, 9, 4)),
            vehicle=((0, 0, 0), (0, 0, 8), (1, 9, 0), (1, 9, 8)),
            horse=((0, 0, 1), (0, 0, 7), (1, 9, 1), (1, 9, 7)),
            elephant=((0, 0, 2), (0, 0, 6), (1, 9, 2), (1, 9, 6)),
            officer=((0, 0, 3), (0, 0, 5), (1, 9, 3), (1, 9, 5)),
            cannon=((0, 2, 1), (0, 2, 7), (1, 7, 1), (1, 7, 7)))
        s = [Soldier(c, x, y) for c, x, y in cinit.soldier]
        v = [Vehicle(c, x, y) for c, x, y in cinit.vehicle]
        g = [General(c, x, y) for c, x, y in cinit.general]
        h = [Horse(c, x, y) for c, x, y in cinit.horse]
        e = [Elephant(c, x, y) for c, x, y in cinit.elephant]
        o = [Officer(c, x, y) for c, x, y in cinit.officer]
        c = [Cannon(c, x, y) for c, x, y in cinit.cannon]
        self.chessboard = [['__' for i in range(9)] for i in range(10)]
        for ms in s, v, g, h, e, o, c:
            for m in ms:
                self.chessboard[m.x][m.y] = m


    def show(self):
        sh = """
        {0[0]}__{0[1]}__{0[2]}__{0[3]}__{0[4]}__{0[5]}__{0[6]}__{0[7]}__{0[8]}
        |   |   |   |   |   |   |   |   |
        {1[0]}__{1[1]}__{1[2]}__{1[3]}__{1[4]}__{1[5]}__{1[6]}__{1[7]}__{1[8]}
        |   |   |   |   |   |   |   |   |
        {2[0]}__{2[1]}__{2[2]}__{2[3]}__{2[4]}__{2[5]}__{2[6]}__{2[7]}__{2[8]}
        |   |   |   |   |   |   |   |   |
        {3[0]}__{3[1]}__{3[2]}__{3[3]}__{3[4]}__{3[5]}__{3[6]}__{3[7]}__{3[8]}
        |   |   |   |   |   |   |   |   |
        {4[0]}__{4[1]}__{4[2]}__{4[3]}__{4[4]}__{4[5]}__{4[6]}__{4[7]}__{4[8]}
        |      楚河             汉界     |
        {5[0]}__{5[1]}__{5[2]}__{5[3]}__{5[4]}__{5[5]}__{5[6]}__{5[7]}__{5[8]}
        |   |   |   |   |   |   |   |   |
        {6[0]}__{6[1]}__{6[2]}__{6[3]}__{6[4]}__{6[5]}__{6[6]}__{6[7]}__{6[8]}
        |   |   |   |   |   |   |   |   |
        {7[0]}__{7[1]}__{7[2]}__{7[3]}__{7[4]}__{7[5]}__{7[6]}__{7[7]}__{7[8]}
        |   |   |   |   |   |   |   |   |
        {8[0]}__{8[1]}__{8[2]}__{8[3]}__{8[4]}__{8[5]}__{8[6]}__{8[7]}__{8[8]}
        |   |   |   |   |   |   |   |   |
        {9[0]}__{9[1]}__{9[2]}__{9[3]}__{9[4]}__{9[5]}__{9[6]}__{9[7]}__{9[8]} 
        """
        from colorama import init, Fore

        init(autoreset=True)
        print(Fore.RED+sh.format(*self.chessboard))




if __name__ == "__main__":
    l = Launch()
    l.initialization()
    l.show()