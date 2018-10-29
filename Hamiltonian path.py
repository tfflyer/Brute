graph = {'A': ['B', 'C', 'F'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'D', 'F'],
         'D': ['B', 'C', 'E'],
         'E': ['D', 'F'],
         'F': ['A', 'C', 'E']}


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
    start = input('请输入你所希望的起点')
    start = start.upper()
    end = input('请输入你所希望的终点')
    end = end.upper()
    paths = find_all_paths(graph,start,end)
    for path in paths:
        if len(path) == 6 and start in graph[end]:
            print(path)

