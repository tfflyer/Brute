"""

数字游戏问题

"""
import time

def pos_se(n):
    lists = [i for i in range(1, n + 1)]
    l_c = lists.count(0)
    i = 0
    k = 0
    t = 0
    while l_c < 15:
        if lists[i] != 0:
            k = k + 1
            if k == 9:
                lists[i] = 0
                print('第'+str(i)+'个跳海了')
                time.sleep(0.5)
                k = 0
            l_c = lists.count(0)
        i = i + 1
        if i == 30:
            i = 0
            t = t+1
            print('第'+str(t)+'圈结束了')
            time.sleep(0.5)
    print('教徒在以下位置比较保险：')
    for i in lists:
        if i != 0:
            print('第'+str(i)+'个位置')


if __name__ == '__main__':
    n = 30
    pos_se(n)