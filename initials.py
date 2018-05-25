# -*- coding:utf8 -*-


from game import Game, solve
from game import L, B, G
from pp import print_layout


class Game0(Game):
    title = '横刀立马'


class Game1(Game):
    title = '层拦叠障'

    initial = L(
        B(G(0, 0), G(0, 1)),
        B(G(3, 0), G(3, 1)),
        B(G(1, 1), G(2, 1)),
        B(G(0, 2), G(1, 2)),
        B(G(2, 2)),
        B(G(3, 2)),
        B(G(0, 3), G(0, 4)),
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4)),
        B(G(3, 3)),
        B(G(3, 4))
    )


class Game2(Game):
    title = '层层设防'

    initial = L(
        B(G(1, 0), G(2, 0)),
        B(G(0, 1)),
        B(G(1, 1), G(2, 1)),
        B(G(3, 1)),
        B(G(0, 2)),
        B(G(1, 2), G(2, 2)),
        B(G(3, 2)),
        B(G(0, 3), G(0, 4)),
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4)),
        B(G(3, 3), G(3, 4))
    )


class Game3(Game):
    title = '水泄不通'

    initial = L(
        B(G(0, 0)),
        B(G(3, 0)),
        B(G(0, 1), G(1, 1)),
        B(G(2, 1), G(3, 1)),
        B(G(0, 2), G(1, 2)),
        B(G(2, 2), G(3, 2)),
        B(G(0, 3), G(0, 4)),
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4)),
        B(G(3, 3)),
        B(G(3, 4))
    )


class Game4(Game):
    title = '过五关'

    initial = L(
        B(G(1, 0), G(2, 0)),
        B(G(0, 1), G(1, 1)),
        B(G(2, 1), G(3, 1)),
        B(G(0, 2), G(1, 2)),
        B(G(2, 2), G(3, 2)),
        B(G(0, 3)),
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4)),
        B(G(3, 3)),
        B(G(0, 4)),
        B(G(3, 4))
    )


class Game5(Game):
    title = '峰回路转'

    initial = L(
        B(G(1, 0)),
        B(G(2, 0), G(3, 0)),
        B(G(1, 1), G(2, 1)),
        B(G(3, 1), G(3, 2)),
        B(G(0, 2), G(1, 2), G(0, 3), G(1, 3)),
        B(G(2, 2), G(2, 3)),
        B(G(3, 3), G(3, 4)),
        B(G(0, 4)),
        B(G(1, 4)),
        B(G(2, 4))
    )


class Game6(Game):
    title = '一路进军'

    initial = L(
        B(G(1, 0), G(2, 0)),
        B(G(0, 1), G(0, 2)),
        B(G(1, 1), G(1, 2)),
        B(G(2, 1), G(2, 2)),
        B(G(3, 1)),
        B(G(3, 2)),
        B(G(0, 3), G(0, 4)),
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4)),
        B(G(3, 3)),
        B(G(3, 4))
    )


class Game7(Game):
    title = '井中之蛙'

    initial = L(
        B(G(1, 0), G(2, 0)),
        B(G(0, 1)),
        B(G(1, 1), G(2, 1)),
        B(G(3, 1)),
        B(G(0, 2), G(0, 3)),
        B(G(1, 2), G(2, 2), G(1, 3), G(2, 3)),
        B(G(3, 2), G(3, 3)),
        B(G(0, 4)),
        B(G(1, 4), G(2, 4)),
        B(G(3, 4))
    )


if __name__ == '__main__':
    import sys
    num = sys.argv[1]

    gm_cls = locals()['Game' + str(num)]
    solve(gm_cls())