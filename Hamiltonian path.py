import matplotlib.pyplot as plt
import networkx as nx

graph = {'A': ['B', 'C', 'F'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'D', 'F'],
         'D': ['B', 'C', 'E'],
         'E': ['D', 'F'],
         'F': ['A', 'C', 'E']}


def write_picture(graph):
    G = nx.DiGraph()
    G.add_edge('A', 'B')
    G.add_edge('A', 'C')
    G.add_edge('A', 'F')
    G.add_edge('B', 'A')
    G.add_edge('B', 'C')
    G.add_edge('B', 'D')
    G.add_edge('C', 'A')
    G.add_edge('C', 'B')
    G.add_edge('C', 'D')
    G.add_edge('C', 'F')
    G.add_edge('D', 'B')
    G.add_edge('D', 'C')
    G.add_edge('D', 'E')
    G.add_edge('E', 'D')
    G.add_edge('E', 'F')
    G.add_edge('F', 'A')
    G.add_edge('F', 'C')
    G.add_edge('F', 'E')
    nx.draw(G, node_color='r',
            with_labels=True,
            node_size=800,
            font_size=18,
            font_color='b',)
    plt.show()


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


if __name__ == '__main__':
    write_picture(graph)
    start = input('请输入你所希望的起点')
    start = start.upper()
    end = input('请输入你所希望的终点')
    end = end.upper()
    flag = False
    paths = find_all_paths(graph, start, end)
    for path in paths:
        if len(path) == 6 and start in graph[end]:
            print(path)
            flag = True
    if not flag:
        print('sorry!你指定的起点与终点在此图中没有符合哈密顿回路条件的路径')
    else:
        print("thank you!")
