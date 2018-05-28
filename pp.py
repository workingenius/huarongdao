
from collections import namedtuple
from game import Layout, L, move_to
from game import Grid, G
from game import steps
from game import Game
from game import Block, B


class Side(frozenset):
    pass


def S(g0, g1):
    return Side([g0, g1])


def odd(i):
    return i % 2 == 1


def even(i):
    return i % 2 == 0


class LayoutPrinter(object):
    CHAR_CONNER = '+'
    CHAR_SIDE_HOR = '-'
    CHAR_SIDE_HOR_0 = ' '
    CHAR_SIDE_VER = '|'
    CHAR_SIDE_VER_0 = ' '
    CHAR_CONTENT_0 = ' '

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        # 要画的边
        self.sides = set()
        # 要画的格子说明
        self.caps = {}  # {grid: cap}

    def add_grids(self, grids, cap=' '):
        # caption 必须是一个字符长度的 ascii 字符串
        # 打印出来才能对齐
        assert isinstance(cap, str) and len(cap) == 1

        border = set()

        for grid in grids:

            # 一个格子的四个边
            sides = set()
            for adjacent in [move_to(grid, step) for step in steps]:
                side = S(grid, adjacent)
                sides.add(side)

            # 共有的边去掉，不同的边留下
            border = (border | sides) - (border & sides)

        # 把边界添加到要画的边里
        self.sides = self.sides | border

        # 在第一个格子里 记录下格子说明
        grid = sorted(list(grids), key=lambda g: (g.x, g.y))[0]
        self.caps[grid] = cap

    def format(self):

        def side_pos(side):
            """根据边算出在字符阵列中的位置

            [(0,0),(1,0)] -> (2,1)
            [(1,0),(2,0)] -> (4,1)
            [(1,1),(2,1)] -> (4,3)

            [(x0,y0),(x1,y1)] -> (x0+x1+1, y0+y1+1)
            """
            gs = list(side)
            return sum(map(lambda g: g.x, gs)) + 1, sum(map(lambda g: g.y, gs)) + 1

        def grid_pos(grid):
            """计算出格子中央在字符阵列中的位置

            (0,0) -> (1,1)
            (1,0) -> (3,1)
            (1,1) -> (3,3)

            (x,y) -> (2x+1, 2y+1)
            """
            return 2 * grid.x + 1, 2 * grid.y + 1

        # 字符点阵的总大小
        w = self.width * 2 + 1
        h = self.height * 2 + 1

        # 初始化字符点阵
        array = []
        for j in range(h):

            row = []
            for i in range(w):
                row.append(None)

            array.append(row)

        # 要画的边 转化为 字符点阵中的位置
        side_poss = set()
        for side in self.sides:
            side_poss.add(side_pos(side))

        # 把要画的格子说明 转化为点阵中的位置
        # 并画在阵列上
        for grid, cap in self.caps.items():
            x, y = grid_pos(grid)
            array[y][x] = cap

        for j, row in enumerate(array):
            for i, char in enumerate(row):
                # 格子角
                if even(j) and even(i):
                    array[j][i] = self.CHAR_CONNER

                # 格子中间
                elif odd(j) and odd(i):
                    if array[j][i] is None:
                        array[j][i] = self.CHAR_CONTENT_0

                # 格子竖边
                elif odd(j) and even(i):
                    if (i, j) in side_poss:
                        array[j][i] = self.CHAR_SIDE_VER
                    else:
                        array[j][i] = self.CHAR_SIDE_VER_0

                # 格子横边
                elif even(j) and odd(i):
                    if (i, j) in side_poss:
                        array[j][i] = self.CHAR_SIDE_HOR
                    else:
                        array[j][i] = self.CHAR_SIDE_HOR_0

        return '\n'.join(reversed([''.join(row) for row in array]))

    def __str__(self):
        return self.format()


class ChineseLayoutPrinter(LayoutPrinter):
    CHAR_CONNER = '+'
    CHAR_SIDE_HOR = '--'
    CHAR_SIDE_HOR_0 = '  '
    CHAR_SIDE_VER = '|'
    CHAR_SIDE_VER_0 = ' '
    CHAR_CONTENT_0 = '  '


def print_layout(game: Game, layout: Layout, gap=None, chinese=True):
    lp_cls = ChineseLayoutPrinter if chinese else LayoutPrinter
    lp = lp_cls(game.width, game.height)

    # 补充上所有的格子
    if chinese:
        for block in layout:
            lp.add_grids(block, cap=block.cap)
    else:
        for block in layout:
            lp.add_grids(block)

    # 计算并补充上空格子
    if not chinese:
        empties = set(game.all_grids())
        for block in layout:
            empties = empties - block

        for empty_grid in empties:
            lp.add_grids([empty_grid], cap='0')

    print(lp.format())
    if gap is not None:
        print(gap)


"""
+-+-+-+-+
| |   | |
+ + + + +
| |   | |
+-+-+-+-+
| |   | |
+ +-+-+ +
| | | | |
+-+-+-+-+
| |0|0| |
+-+-+-+-+
"""

"""
+--+-+-+-+
|张|   | |
+ + + + +
| |   | |
+-+-+-+-+
| |   | |
+ +-+-+ +
| | | | |
+-+-+-+-+
| |0|0| |
+-+-+-+-+
"""


if __name__ == '__main__':
    g = Game()
    print_layout(g, g.initial, chinese=False)

    print()
    print()

    print_layout(g, L(
        B(G(0, 0), G(0, 1), G(1, 0), G(1, 1))
    ), chinese=False)

    print()
    print()

    print_layout(g, L(
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4))
    ), chinese=False)
