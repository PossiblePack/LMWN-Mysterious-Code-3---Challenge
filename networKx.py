import networkx as nx
import time
import heapq

def setEdge(arr,row,column):
    # edgesList = []
    m = len(arr)-1
    n = len(arr[0])-1
    source = (n)*row + row + column
    if row != 0: #check T
        heapq.heappush(edges, (source, (n)*(row-1) + (row-1) + column, int(arr[row-1][column])))
    if column != 0: #check L  
        heapq.heappush(edges, (source, (n)*(row) + (row) + (column-1), int(arr[row][column-1])))
    if row != m: #check D  
        heapq.heappush(edges, (source, (n)*(row+1) + (row+1) + (column), int(arr[row+1][column])))
    if column != n: #check R  
        heapq.heappush(edges, (source, (n)*(row) + (row) + (column+1), int(arr[row][column+1])))
    # print(edges)
    return edges

if __name__ == "__main__":
    start = time.time()
    file = open("in-4.txt", "r").read()
    way = filter(None,file.split("\n"))
    arr = [l.split(" ") for l in [l for l in way]]

    m = len(arr)
    n = len(arr[0])
    n_vertices = m*n
    first_weight = int(arr[1][1])

    edges = []
    for row in range(0, m):
        for column in range(0, n):
            edges.append(setEdge(arr,row,column).pop())
    
    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    # print(nx.dijkstra_path(G, 0, n_vertices-1, weight="weight"))
    result = nx.dijkstra_path_length(G, 0, n_vertices-1, weight="weight")+1

    print("The distance of shortest path is",result)

    end = time.time()
    print("runtime: {} seconds".format(str(end - start)))