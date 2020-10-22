def empty_graph(n):
    res = []
    for i in range(n):
        res.append([0]*n)
    return res
def convert(graph):
    matrix = []
    for i in range(len(graph)): 
        matrix.append([0]*len(graph))
        for j in graph[i]:
            matrix[i][j] = 1
    return matrix
def prims_algo(graph):
    graph1 = convert(graph)
    n = len(graph1)
    tree = empty_graph(n)
    con =[0]
    while len(con) < n :
        found = False
        for i in con:
            for j in range(n):
                if j not in con and graph1[i][j] == 1:
                    tree[i][j] =1
                    tree[j][i] =1
                    con += [j]
                    found  = True
                    break
            if found :
                break
    return tree
matrix = [[0, 1, 1, 1, 0, 1, 1, 0, 0],
          [1, 0, 0, 1, 0, 0, 1, 1, 0],
          [1, 0, 0, 1, 0, 0, 0, 0, 0],
          [1, 1, 1, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 1, 0, 0, 1],
          [1, 0, 0, 0, 1, 0, 0, 0, 1],
          [1, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 0, 0, 0]]

lst = [[1,2,3,5,6],[0,3,6,7],[0,3],[0,1,2,4],[3,5,8],[0,4,8],[0,1],[1],[4,5]]
print("From graph to spanning tree:\n")
print(prims_algo(lst))
