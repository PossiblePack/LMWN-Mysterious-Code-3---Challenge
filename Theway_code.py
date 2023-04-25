import sys
  
class Graph():
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
  
    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])
  
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
  
        # Initialize minimum distance for next node
        min = sys.maxsize
  
        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
  
        return min_index
  
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src, weight):
  
        dist = [sys.maxsize] * self.V
        dist[src] = weight
        sptSet = [False] * self.V
  
        for cout in range(self.V):
  
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)
  
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True
  
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
  
        # self.printSolution(dist)
        print("result distance is {}".format(dist[len(dist)-1]))

def setWayArray(txt):
    way = filter(None,txt.split("\n"))
    arr = [l.split(" ") for l in [l for l in way]]
    return arr

def checkNeighbor(arr,row,column):
    neighborList = []
    m = len(arr)-1
    n = len(arr[0])-1
    if row != 0: #check T
        neighborList.append((int(arr[row-1][column]), (row-1,column)))
    if column != 0: #check L  
        neighborList.append((int(arr[row][column-1]), (row,column-1)))
    if row != m: #check D  
        neighborList.append((int(arr[row+1][column]), (row+1,column)))
    if column != n: #check R  
        neighborList.append((int(arr[row][column+1]), (row,column+1)))
    return neighborList

# Driver's code
if __name__ == "__main__":
    file = open("in-1.txt", "r").read()
    way = filter(None,file.split("\n"))
    arr = [l.split(" ") for l in [l for l in way]]

    # get array size and initial adjacency list
    m = len(arr)
    n = len(arr[0])
    n_vertices = m*n
    first_weight = int(arr[0][0])
    g = Graph(n_vertices)

    # create adjacency list from array
    count = 0
    for row in range(0, m):
        for column in range(0, n):
            # print(arr[row][column])
            nexts = checkNeighbor(arr,row,column)
            for i in nexts:
                index = (n-1)*i[1][0] + i[1][0] + i[1][1]
                # print(index)
                # print(i[0],i[1][0],i[1][1])
                g.graph[count][index] = i[0]
            count+=1
    # print(g.graph)
    
    g.dijkstra(0,first_weight)