import random
import itertools
import matplotlib.pyplot as plt
from itertools import permutations
import numpy


def generate_num(n):  # 生成n个随机的点
    random_list = list(itertools.product(range(1, 50), range(1, 50)))
    lists = random.sample(random_list, n)
    return lists


def judge_num(m):
    if m >= 0:
        return 1
    else:
        return -1


def judge_lowes(lists):
    global hull_poit
    y_list = [x[1] for x in lists]
    y_min = min(y_list)
    y_id = y_list.index(y_min)  # 寻找纵坐标最低的那个点
    hull_poit = [lists[y_id]]  # 边界点的集合
    # print(hull_poit)
    lowst = lists[y_id]
    # print(lowst)
    return lowst


def judge_hull(lists):
    global hull_poit
    for arr in permutations(lists, 2):
        flag_arr = []
        if arr[:1] not in hull_poit:
            for test_point in lists:
                if  test_point not in arr[:1]:
                    arr_test = numpy.array([[arr[0][0], arr[0][1], 1], [arr[1][0], \
                            arr[1][1], 1], [test_point[0], test_point[1], 1]])
                    flag = numpy.linalg.det(arr_test)
                    flg = judge_num(flag)
                    flag_arr.append(flg)
                    if flg != flag_arr[0]:
                        flag_2=False
                        break
                    else:
                        flag_2 = True

            if 1 not in flag_arr or -1 not in flag_arr and flag_2:
                hull_poit.append(arr[0])
                hull_poit.append(arr[1])
    return hull_poit


if __name__ == '__main__':
    global hull_poit
    poit_list = generate_num(20)
    lowest=judge_lowes(poit_list)
    low_new=judge_hull(poit_list)
    hull_poit=list(set(hull_poit))
    hull_poit.sort()
    print(hull_poit)
    print('\n')
    for i in range(0,20):
        print(poit_list[i][0],poit_list[i][1])
        plt.scatter(poit_list[i][0],poit_list[i][1])

    line_y=[]
    line_x=[]
    for h in hull_poit:
        line_x.append(h[0])
        line_y.append(h[1])
    # print(line_x,line_y,'\n')
    plt.plot(line_x,line_y,color='r')
    plt.show()

