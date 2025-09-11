import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]
        self.paths = [[] for _ in range(self.V)]

    def printSolution(self,dist):
        print("Vertex \tDistance from Source \tPath")
        for node in range(self.V):
            print(node, "\t", dist[node], "\t\t\t", self.paths[node])

    # A helper function to find the vertex with 
    # the lowest distance value, from the unvisited
    # vertices (ie a vertex whose value in sptSet is 
    # False)
    def minDistance(self, dist, sptSet):
        # Initialize minimum distance as a practically
        # infinitive value
        min = sys.maxsize

        # iterate through the range of vertices
        for v in range(self.V): 
            # find the closest vertex that is reachable
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v]
                min_index = v
        # return that index so the program 
        # knows which node to visit
        return min_index 
    
    def dijkstra(self,src):
        # array of distances from the source 
        # to all other nodes, 
        # with values instantiated to a very high value
        dist = [sys.maxsize] * self.V 
        dist[src] = 0 # setting the source nodes distance to itself at 0
        sptSet = [False] * self.V # setting all values to False or unvisited in sptSet
        self.paths[src] = [src] # setting the source nodes path to itself as itself

        for _ in range(self.V): 
            x = self.minDistance(dist, sptSet) # find the nearest node
            sptSet[x] = True # mark that node as visited/processed
            for y in range(self.V):
                # check other nodes to see if:
                # 1. an edge exists between the two vertices
                # 2. the second vertex has not yet been visited
                # 3. the current distance to the y vertex is greater than the 
                # distance to x plus the connection in question (self.graph[x][y])
                # if so, update the distance to y and the paths to y as the shortest path
                if self.graph[x][y] > 0 and not sptSet[y] and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
                    self.paths[y] = self.paths[x] + [y]
        self.printSolution(dist)

if __name__ == "__main__":
    g = Graph(9)
    g.graph = [
        [0,4,0,0,0,0,0,8,0],
        [4,0,8,0,0,0,0,11,0],
        [0,8,0,7,0,4,0,0,2],
        [0,0,7,0,9,14,0,0,0],
        [0,0,0,9,0,10,0,0,0],
        [0,0,4,14,10,0,2,0,0],
        [0,0,0,0,0,2,0,1,6],
        [8,11,0,0,0,0,1,0,7],
        [0,0,2,0,0,0,6,7,0]
        ]
    g.dijkstra(0)

