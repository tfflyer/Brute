"""

约瑟夫问题

"""


def judge_killer(n):
    lists = [i for i in range(1, n+1)]
    l_c = lists.count(0)
    i = 0
    k = 0
    while l_c < 39:
        if lists[i] != 0:
            k = k+1
            if k == 3:
                print('第', lists[i], '个被杀了')
                lists[i] = 0

                k = 0
            l_c = lists.count(0)
        i = i+1
        if i == 41:
            i = 0
    print('剩下的两位叛徒是：')
    for i in lists:
        if i != 0:
            print('第', i, '个')


if __name__ == '__main__':
    # num=input('请输入人的个数')
    num = 41
    judge_killer(num)
