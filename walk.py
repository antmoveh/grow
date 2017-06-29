import collections
from launch import Launch
from chessboard import  ChessPiece


pieces = collections.namedtuple('pieces', ['pawn', 'king', 'chariot', 'horse', 'elephant', 'adviser', 'cannon', 'front'])
pie = pieces(pawn=('兵', '卒'), king=('将', '帅'), chariot=('车', '車'), horse= ('马', '馬'), elephant=('象', '相'),
       adviser=('士', '仕'), cannon=('炮', '砲'), front=('前', '后'))

symbol = {'进': '-'}


laun = Launch()

wal = '车一进一'

if len(wal) != 4:
    print('error Please input again:')


row = [x[8] for x in laun.chessboard if isinstance(x[8], ChessPiece) and x[8].filter(8, wal[0])]
print(row)







