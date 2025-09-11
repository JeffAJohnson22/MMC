import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]
        self.paths = [[] for _ in range(self.V)]
        # Mapping of node indices to location names
        self.nodeNames = {
            0: "The Shire",
            1: "Bree",
            2: "Rivendell", 
            3: "Moira",
            4: "Dale",
            5: "Lorien",
            6: "Isengard",
            7: "Edoras",
            8: "Minas Tirith",
            9: "Emyn Muil",
            10: "Mt Doom"
        }

    def getPath(self, path):
        return " -> ".join([self.nodeNames[node] for node in path])

    def findSpecificPath(self, startingName, FinalName):
        # Find the node indices for the given location names
        startingNode = None
        dest_node = None
        
        for node, name in self.nodeNames.items():
            if name == startingName:
                startingNode = node
                startingNode = node
            if name == FinalName:
                dest_node = node
        
        if startingNode is None or dest_node is None:
            print(f"Error: Could not find locations {startingName} or {FinalName}")
            return
        
        # Run dijkstra from the source node
        dist = [sys.maxsize] * self.V 
        dist[startingNode] = 0
        sptSet = [False] * self.V
        paths = [[] for _ in range(self.V)]
        paths[startingNode] = [startingNode]

        for _ in range(self.V): 
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.V):
                # Check if there's a valid edge and if we found a shorter path
                weHaveAnEdge = self.graph[x][y] > 0
                notVisited = not sptSet[y]
                distanceToY = dist[y]
                distanceToX = dist[x] + self.graph[x][y]
                
                if weHaveAnEdge and notVisited and distanceToY > distanceToX:
                    # Update with the shorter distance and path
                    dist[y] = distanceToX
                    paths[y] = paths[x] + [y]
        
        # Display the specific path
        locationName = self.getPath(paths[dest_node])
        print(f"Shortest path from {startingName} to {FinalName}:")
        print(f"Distance: {dist[dest_node]}")
        print(f"Path: {locationName}")


    def printSolution(self,dist):
        print("Vertex \tDistance from Source \tPath")

        print("======================================")
        for node in range(self.V):
            # Get the location name and path names
            location = self.nodeNames[node]
            locationName = self.getPath(self.paths[node])
            print(f"{location:<15}\t{dist[node]}\t\t{locationName}")

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
                weHaveAnEdge = self.graph[x][y] > 0
                notVisited = not sptSet[y]
                distanceToY = dist[y]
                distanceToX = dist[x] + self.graph[x][y]
                
                if weHaveAnEdge and notVisited and distanceToY > distanceToX:
                    # Update with the shorter distance and path
                    dist[y] = distanceToX
                    self.paths[y] = self.paths[x] + [y]
        self.printSolution(dist)

if __name__ == "__main__":
    g = Graph(11) 
    g.graph = [
    [0,131,0,0,0,0,481,0,0,0,0],
    [131,0,306,0,0,0,0,0,0,0,0],
    [0,306,0,178,362,0,0,0,0,0,0],
    [0,0,178,0,0,172,173,0,0,0,0],
    [0,0,362,0,0,0,0,0,0,0,0],
    [0,0,0,172,0,0,0,201,0,217,0],
    [481,0,0,173,0,0,0,174,0,0,0],
    [0,0,0,0,0,201,174,0,315,262,0],
    [0,0,0,0,0,0,0,315,0,264,178],
    [0,0,0,0,0,217,0,262,264,0,183],
    [0,0,0,0,0,0,0,0,178,183,0], 
    ]
    
    print("=== SPECIFIC PATH ANALYSIS ===")
    print()
    
    # Find shortest path from Rivendell to Mt. Doom
    g.findSpecificPath("Rivendell", "Mt Doom")
    
    print("=== COMPLETE DIJKSTRA FROM THE SHIRE ===")
    print()
    g.dijkstra(0)


