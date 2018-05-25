
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
        grid = list(grids)[0]
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
            return sum(map(G.x, gs)) + 1, sum(map(G.y, gs)) + 1

        def grid_pos(grid):
            """计算出格子中央在字符阵列中的位置

            (0,0) -> (1,1)
            (1,0) -> (3,1)
            (1,1) -> (3,3)

            (x,y) -> (2x+1, 2y+1)
            """
            return 2 * G.x(grid) + 1, 2 * G.y(grid) + 1

        # 字符点阵的总大小
        w = self.width * 2 + 1
        h = self.height * 2 + 1

        # 初始化字符点阵
        array = []
        for j in range(h):

            row = []
            for i in range(w):
                row.append(' ')

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
                    array[j][i] = '+'

                # 格子中间
                elif odd(j) and odd(i):
                    pass

                # 格子竖边
                elif odd(j) and even(i):
                    if (i, j) in side_poss:
                        array[j][i] = '|'

                elif even(j) and odd(i):
                    if (i, j) in side_poss:
                        array[j][i] = '-'

        return '\n'.join(reversed([''.join(row) for row in array]))

    def __str__(self):
        return self.format()


def print_layout(game: Game, layout: Layout, gap=None):
    lp = LayoutPrinter(game.width, game.height)

    # 补充上所有的格子
    for blocks in layout:
        lp.add_grids(blocks)

    # 计算并补充上空格子
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


if __name__ == '__main__':
    g = Game()
    print_layout(g, g.initial)

    print()
    print()

    print_layout(g, L(
        B(G(0, 0), G(0, 1), G(1, 0), G(1, 1))
    ))

    print()
    print()

    print_layout(g, L(
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4))
    ))
