# -*- coding: utf8 -*-

# from typing import Tuple, FrozenSet
#
# Grid = Tuple[int, int]  # 格子
# Block = FrozenSet[Grid]  # 块
# Layout = FrozenSet[Block]  # 布局
#
# Move = Tuple[int, int]  # 走一步
from time import sleep


class Grid(object):
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y


G = Grid


class Move(tuple):
    def __new__(cls, x, y):
        return super(Move, cls).__new__(cls, [x, y])

    def __str__(self):
        x, y = self
        if x == 0 and y > 0:
            return '向上'
        if x == 0 and y < 0:
            return '向下'
        if x > 0 and y == 0:
            return '向右'
        if x < 0 and y == 0:
            return '向左'


M = Move


steps = [
    M(1, 0),  # 右
    M(-1, 0),  # 左
    M(0, 1),  # 上
    M(0, -1)  # 下
]


class Block(frozenset):
    def __new__(cls, *grids, **kwargs):
        assert all(map(lambda x: isinstance(x, Grid), grids))
        return super(Block, cls).__new__(cls, grids)

    def __init__(self, *grids, **kwargs):
        if 'cap' in kwargs:
            self.cap = kwargs['cap']
        else:
            self.cap = ''

        if 'adj' in kwargs:
            self.adj = kwargs['adj']
        else:
            if len(self) == 1:
                self.adj = '小'
            elif len(self) == 2:
                if len(set(g.x for g in self)) == 1:
                    self.adj = '站'
                elif len(set(g.y for g in self)) == 1:
                    self.adj = '矮'
                else:
                    self.adj = '分'
            elif len(self) == 3:
                self.adj = '怪'
            elif len(self) == 4:
                self.adj = '大'
            elif len(self) > 4:
                self.adj = '巨'

    def __str__(self):
        if self.cap:
            return self.adj + self.cap
        else:
            return super(Block, self).__str__()


B = Block


class Layout(frozenset):
    def __new__(cls, *blocks):
        assert all(map(lambda x: isinstance(x, Block), blocks))
        return super(Layout, cls).__new__(cls, blocks)


L = Layout


def move_to(grid: Grid, move: Move) -> Grid:
    return G(grid.x + move[0], grid.y + move[1])


class Game(object):
    width = 4
    height = 5

    initial = L(
        B(G(0, 0)),
        B(G(3, 0)),
        B(G(0, 1), G(0, 2)),
        B(G(1, 1)),
        B(G(2, 1)),
        B(G(3, 1), G(3, 2)),
        B(G(1, 2), G(2, 2)),
        B(G(0, 3), G(0, 4)),
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4)),
        B(G(3, 3), G(3, 4))
    )

    exit = B(G(1, 0), G(2, 0), G(1, 1), G(2, 1))

    def all_grids(self):
        for w in range(self.width):
            for h in range(self.height):
                yield G(w, h)

    def is_done(self, layout: Layout):
        u"""胖曹是否走出去了"""
        return self.exit in layout

    def is_valid_layout(self, layout):
        game = self

        # x, y 超边界不行
        for block in layout:
            for grid in block:
                x, y = grid.x, grid.y

                if x < 0 or x >= game.width:
                    return False
                if y < 0 or y >= game.height:
                    return False

        # 各块有重叠不行

        # 覆盖的总区域
        cover = set()
        for block in layout:
            cover = cover | block

        # 总块数和覆盖区域块数相比较
        if sum(map(len, layout)) == len(cover):
            return True
        else:
            return False


def move_block(game, layout, block, move):
    """把 {layout} 当中的 {block} 按照 {move} 所指进行移动
    返回移动后的 layout
    如果不能移动 则返回 None
    """
    nblock = B(*[move_to(g, move) for g in block], cap=block.cap, adj=block.adj)
    nlayout = L(*[b for b in layout if b != block] + [nblock])

    # 移动之后如果 block 数量变少 则不能移动
    if len(nlayout) != len(layout):
        return

    if game.is_valid_layout(nlayout):
        return nlayout
    else:
        return


def solve(game):
    from pp import print_layout

    layout_q = [game.initial]
    known_layouts = set(layout_q)
    layout_from = {}  # {to: (from, block, move)}

    print('正在搜索 请稍候')

    while layout_q:
        print(len(layout_q))
        cur_layout = layout_q.pop(0)

        if game.is_done(cur_layout):
            cnt = 0
            l = cur_layout
            while l in layout_from:
                print_layout(game, l, gap='')
                l, b, m = layout_from[l]
                print(str(b) + str(m))
                cnt += 1
            print_layout(game, l)
            print('\n解{title} 共 {n} 步 请倒序查看'.format(title=game.title, n=cnt))
            break

        for block in cur_layout:
            for move in steps:
                nlayout = move_block(game, cur_layout, block, move)

                if nlayout:
                    if nlayout in known_layouts:
                        pass
                    else:
                        # print_layout(game, cur_layout)
                        # print_layout(game, nlayout)
                        # print('#' * 10)

                        layout_q.append(nlayout)
                        known_layouts.add(nlayout)
                        layout_from[nlayout] = (cur_layout, block, move)

                        # sleep(3)
    else:
        print_layout(game, game.initial)
        print('死路一条')


if __name__ == '__main__':
    solve(Game())
