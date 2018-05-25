# -*- coding:utf8 -*-


from game import Game, solve
from game import L, B, G
from pp import print_layout


class Game0(Game):
    title = '横刀立马'

    initial = L(
        B(G(0, 0), cap='甲'),
        B(G(3, 0), cap='乙'),
        B(G(0, 1), G(0, 2), cap='马'),
        B(G(1, 1), cap='丙'),
        B(G(2, 1), cap='丁'),
        B(G(3, 1), G(3, 2), cap='关'),
        B(G(1, 2), G(2, 2), cap='黄'),
        B(G(0, 3), G(0, 4), cap='张'),
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4), cap='曹'),
        B(G(3, 3), G(3, 4), cap='赵')
    )


class Game1(Game):
    title = '层拦叠障'

    initial = L(
        B(G(0, 0), G(0, 1), cap='马'),
        B(G(3, 0), G(3, 1), cap='黄'),
        B(G(1, 1), G(2, 1), cap='张'),
        B(G(0, 2), G(1, 2), cap='关'),
        B(G(2, 2), cap='甲'),
        B(G(3, 2), cap='乙'),
        B(G(0, 3), G(0, 4), cap='赵'),
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4), cap='曹'),
        B(G(3, 3), cap='丙'),
        B(G(3, 4), cap='丁')
    )


class Game2(Game):
    title = '层层设防'

    initial = L(
        B(G(1, 0), G(2, 0), cap='赵'),
        B(G(0, 1), cap='甲'),
        B(G(1, 1), G(2, 1), cap='张'),
        B(G(3, 1), cap='乙'),
        B(G(0, 2), cap='丙'),
        B(G(1, 2), G(2, 2), cap='关'),
        B(G(3, 2), cap='丁'),
        B(G(0, 3), G(0, 4), cap='马'),
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4), cap='曹'),
        B(G(3, 3), G(3, 4), cap='黄')
    )


class Game3(Game):
    title = '水泄不通'

    initial = L(
        B(G(0, 0), cap='甲'),
        B(G(3, 0), cap='乙'),
        B(G(0, 1), G(1, 1), cap='赵'),
        B(G(2, 1), G(3, 1), cap='马'),
        B(G(0, 2), G(1, 2), cap='关'),
        B(G(2, 2), G(3, 2), cap='张'),
        B(G(0, 3), G(0, 4), cap='黄'),
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4), cap='曹'),
        B(G(3, 3), cap='丙'),
        B(G(3, 4), cap='丁')
    )


class Game4(Game):
    title = '过五关'

    initial = L(
        B(G(1, 0), G(2, 0), cap='黄'),
        B(G(0, 1), G(1, 1), cap='赵'),
        B(G(2, 1), G(3, 1), cap='马'),
        B(G(0, 2), G(1, 2), cap='关'),
        B(G(2, 2), G(3, 2), cap='张'),
        B(G(0, 3), cap='甲'),
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4), cap='曹'),
        B(G(3, 3), cap='乙'),
        B(G(0, 4), cap='丙'),
        B(G(3, 4), cap='丁')
    )


class Game5(Game):
    title = '峰回路转'

    initial = L(
        B(G(1, 0), cap='甲'),
        B(G(2, 0), G(3, 0), cap='张'),
        B(G(1, 1), G(2, 1), cap='关'),
        B(G(3, 1), G(3, 2), cap='黄'),
        B(G(0, 2), G(1, 2), G(0, 3), G(1, 3), cap='曹'),
        B(G(2, 2), G(2, 3), cap='马'),
        B(G(3, 3), G(3, 4), cap='赵'),
        B(G(0, 4), cap='乙'),
        B(G(1, 4), cap='丙'),
        B(G(2, 4), cap='丁')
    )


class Game6(Game):
    title = '一路进军'

    initial = L(
        B(G(1, 0), G(2, 0), cap='关'),
        B(G(0, 1), G(0, 2), cap='赵'),
        B(G(1, 1), G(1, 2), cap='马'),
        B(G(2, 1), G(2, 2), cap='黄'),
        B(G(3, 1), cap='甲'),
        B(G(3, 2), cap='乙'),
        B(G(0, 3), G(0, 4), cap='张'),
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4), cap='曹'),
        B(G(3, 3), cap='丙'),
        B(G(3, 4), cap='丁')
    )


class Game7(Game):
    title = '井中之蛙'

    initial = L(
        B(G(1, 0), G(2, 0), cap='赵'),
        B(G(0, 1), cap='甲'),
        B(G(1, 1), G(2, 1), cap='张'),
        B(G(3, 1), cap='乙'),
        B(G(0, 2), G(0, 3), cap='马'),
        B(G(1, 2), G(2, 2), G(1, 3), G(2, 3), cap='曹'),
        B(G(3, 2), G(3, 3), cap='黄'),
        B(G(0, 4), cap='丙'),
        B(G(1, 4), G(2, 4), cap='关'),
        B(G(3, 4), cap='丁')
    )


class Game98(Game):
    title = '逗逼n国'

    width = 5
    height = 5

    initial = L(
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4), cap='曹'),
        B(G(0, 3), cap='董'),
        B(G(0, 2), G(0, 1), G(1, 2), cap='刘'),
        B(G(3, 2), G(4, 2), cap='吕'),
        B(G(3, 3), cap='陶'),
        B(G(4, 3), G(3, 4), G(4, 4), cap='袁'),
        B(G(3, 0), G(4, 1), G(4, 0), cap='孙'),
        B(G(1, 0), G(1, 1), cap='晋'),
        B(G(0, 4), cap='马')
    )


class Game99(Game):
    title = '逗逼三国'

    width = 5
    height = 5

    initial = L(
        B(G(1, 3), G(2, 3), G(1, 4), G(2, 4), cap='曹'),
        B(G(0, 2), G(0, 3), G(1, 2), G(1, 1), cap='刘'),
        B(G(3, 1), G(3, 2), G(4, 1), G(2, 1), G(3, 0), cap='孙'),
        # B(G(4, 3), cap='袁')
    )


if __name__ == '__main__':
    import sys
    num = sys.argv[1]

    gm_cls = locals()['Game' + str(num)]
    solve(gm_cls())
