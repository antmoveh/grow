from launch import Launch
from chessboard import  ChessPiece


red_name = ('将', '车', '马', '象', '士', '炮', '卒')
black_name = ('帅', '車', '馬', '相', '仕', '砲', '兵')
__step = ('一', '二', '三', '四', '五', '六', '七', '八', '九')
__direct = ('进', '退', '平')
special = ('前', '后')

laun = Launch()

def analysis(pace):
    if len(pace) != 4:
        return False, 'error Please input again'
    if pace[0] in special:
        pass
    # chess name
    try:
        name = pace[0] if pace[0] in red_name else red_name[black_name.index(pace[0])]
    except ValueError:
        return False, 'name error'
    # location y
    if pace[1] in __step:
        y = 8 - __step.index(pace[1])
    else:
        try:
            y = 9 - int(pace[1])
        except ValueError:
            return False, 'value error'
        else:
            if 0< y > 8:
                return False, 'out of range'
    # target chess
    target = [i[y] for i in laun.chessboard if isinstance(i[y], ChessPiece) and i[y].filter(y, name)]
    if len(target) != 1:
        return False, 'multiple matching'
    tar = target[0].step(pace[2], pace[3])
    if tar[0]:
        return True, target[0], tar[1], tar[2]
    else:
        return False, 'step error'



if __name__ == "__main__":
    pace = '炮2平6'
    a = analysis(pace)
    print(a)