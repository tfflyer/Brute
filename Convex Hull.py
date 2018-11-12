import random
import itertools
import matplotlib.pyplot as plt
import networkx as nx
from itertools import permutations
import numpy
import math


def generate_num(n):  # 生成n个随机的点
    random_list = list(itertools.product(range(1, 50), range(1, 50)))
    lists = random.sample(random_list, n)
    return lists


def judge_num(m):  # 把正负数分别对应+1、—1
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


def judge_hull(lists):  # 判断是不是凸包边界上的点
    global hull_poit, flag_2
    for arr in permutations(lists, 2):  # 全排列
        flag_arr = []
        if arr[:1] not in hull_poit:
            for test_point in lists:
                if test_point not in arr[:1]:
                    arr_test = numpy.array([[arr[0][0], arr[0][1], 1],
                                            [arr[1][0], arr[1][1], 1],
                                            [test_point[0], test_point[1], 1]])  # 构建矩阵
                    flag = numpy.linalg.det(arr_test)
                    flg = judge_num(flag)
                    flag_arr.append(flg)
                    if flg != flag_arr[0]:          # 判断剩余所有点是否全在直线的一侧
                        flag_2 = False
                        break
                    else:
                        flag_2 = True

            if 1 not in flag_arr or -1 not in flag_arr and flag_2:
                hull_poit.append(arr[0])
                hull_poit.append(arr[1])
    return hull_poit



def min_dis(w_p, w_list):
    global sorted_hull

    w_list.remove(w_p)
    min=99999
    if len(w_list)>0:
        # print(w_list)
        min_id=0
        for i in range(0, len(w_list)):
            dis=math.hypot(w_p[0]-w_list[i][0], w_p[1]-w_list[i][1])
            if dis< min:
                min=dis
                min_id=i
        # print(w_list[i])
        sorted_hull.append(w_list[min_id])
        min_dis(w_list[min_id],w_list)
    else:

        return


def draw_picture():
    for i in range(0, 49):
        # print(poit_list[i][0], poit_list[i][1])
        plt.scatter(poit_list[i][0], poit_list[i][1])           # 绘图，添加所有的点
    line_y = []
    line_x = []
    # plt.show()
    for h in sorted_hull:
        line_x.append(h[0])
        line_y.append(h[1])
    # print(line_x,line_y,'\n')
    line_x.append(line_x[0])
    line_y.append(line_y[0])
    G = nx.Graph()
    for h in range(len(sorted_hull)):
        G.add_node(h)
    edge_arr = []
    for i in range(0, len(hull_poit)):
        edge_arr.append(i)
    for i in permutations(edge_arr, 2):
        # print(i)
        G.add_edge(i[0], i[1])
    pos = sorted_hull
    nx.draw(G, pos, node_size=36)
    plt.plot(line_x,line_y)
    plt.show()


if __name__ == '__main__':
    global hull_poit
    global sorted_hull
    poit_list = generate_num(50)
    lowest = judge_lowes(poit_list)
    low_new = judge_hull(poit_list)
    hull_poit = list(set(hull_poit))
    # hull_poit.sort()
    print('凸包边界上的点包括：\n')
    print(hull_poit)
    print('\n')
    sorted_hull=[lowest]

    min_dis(lowest, hull_poit)
    draw_picture()
    # print(sorted_hull)

