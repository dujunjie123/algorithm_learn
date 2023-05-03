# -*- coding: utf-8 -*-
# @Time : 2023/3/26 22:33
# @Author : 杜俊杰
# @File : 爬楼梯.py
# @Project : algorithm_learn
# @File Description :

action = {}

action[1] = 1
action[2] = 2


def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:

        if n not in action:
            r = solution(n - 1) + solution(n - 2)
            action[n] = r
            return r
        else:
            return action[n]


if __name__ == '__main__':
    import time
    s = time.time()
    # 16.510226249694824
    print(solution(10))
    e = time.time()
    print(e - s)