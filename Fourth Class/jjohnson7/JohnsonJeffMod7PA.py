import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]
        self.paths = [[] for _ in range(self.V)]
        # dictionary for location look up
        self.nodeNames = {
            0: "Earth",
            1: "Pleiades",
            2: "Alpha Centauri",
            3: "Vela Molecular Ridge",
            4: "Rosette Nebula",
            5: "Orion Nebula",
            6: "Canis Major",
            7: "Orion",
        }

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
    
    # A: Dijkstra's algorithm implementation included and working
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
        self.printSolution(src, dist)

    # A: Dijkstra's algorithm implementation included and working
    def printSolution(self, src, dist):
        # Your program should print the shortest path from the Shire to various points in Middle Earth including the paths and the distances along the way.
        
        # Skip the source node
        for node in range(self.V):
            if node == src:  
                continue

            # Created an empty array for each point to store the actual path taken.
            paths = []
            for i in self.paths[node]:
                paths.append(self.nodeNames[i])
            # Gets the total shortest distance from the source to this specific node
            distance = dist[node] 
            # Looks up the name of the destination node
            destination = self.nodeNames[node]
            
            # The print statement includes all of the necessary information in a readable format.
            if len(paths) > 1:
                # takes the list of nodes and joins them with arrows into a string
                pathString = " -> ".join(paths)
                print("To reach {} from {}, Invader Zim's path must be:".format(destination, self.nodeNames[src]))
                print("{}".format(pathString))
                print("Total distance traveled would be {} lightyears.".format(distance))
                
                # checks if the path to the current node has more than one sub path
                if len(self.paths[node]) > 1:
                    print("Splits:")
                    # Loops through each consecutive pair of nodes in the path.
                    for i in range(len(self.paths[node]) - 1):
                        # Gets the current node and the next node in the path.
                        fromHere = self.paths[node][i]
                        toHere = self.paths[node][i + 1]
                        # Looks up the distance between these two.
                        splitDistance = self.graph[fromHere][toHere]
                        print("   {} -> {} is {} lightyears".format(self.nodeNames[fromHere], self.nodeNames[toHere], splitDistance))
                print("About {} pints of Romulan Ale is required. \n".format(distance // 32))
            else:
                print("To reach {}: No path available\n".format(destination))
                
    def printSpecificPath(self, start, end):
        # took most of this from what was given for the dijkstra algorithm
        dist = [sys.maxsize] * self.V
        dist[start] = 0
        sptSet = [False] * self.V

        # Created an empty array for each point to store the actual path taken.
        paths = []
        for i in range(self.V):
            paths.append([])
        # Sets the path to the start node as just itself
        self.paths[start] = [start]
        
        for _ in range(self.V): 
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.V):
                if self.graph[x][y] > 0 and not sptSet[y] and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
                    self.paths[y] = self.paths[x] + [y]
        
        # Get path to end node
        pathNodes = []
        for i in self.paths[end]:
            pathNodes.append(self.nodeNames[i])
        # takes the list of nodes and joins them with arrows into a string
        pathString = " -> ".join(pathNodes)
        # Gives me the total lightyears for the complete journey
        distance = dist[end]
        # The print statement includes all of the necessary information in a readable format.
        print(f"Path: {pathString}")
        print(f"Distance: {distance} lightyears")
        print("Splits:")
        
        # Print splits
        # Loops through each consecutive pair of nodes in the path
        for i in range(len(self.paths[end]) - 1):
            # Gets the current node index
            fromHere = self.paths[end][i]
            # Gets the next node index
            toHere = self.paths[end][i + 1]
            # Looks up the distance between these two.
            splitDistance = self.graph[fromHere][toHere]
            print(f"  {self.nodeNames[fromHere]} -> {self.nodeNames[toHere]}: {splitDistance} lightyears")

        print(f"Romulan Ale pints: {distance // 32} pints")

def main():

    g = Graph(8)
    # B. The adjacency matrix representing Middle Earth is correct.
    g.graph = [
    [0, 442, 4, 0, 0, 1344, 0, 0],
    [442, 0, 0, 0, 842,932, 0, 0],
    [4, 0, 0, 437, 0,0, 0, 0],
    [0, 0, 437, 0, 0,399, 337, 0],
    [0, 842, 0, 0, 0,376, 0, 345],
    [1344,932,0, 399, 376, 0, 0, 154],
    [0, 0, 0, 337, 0, 0, 0, 221],
    [0, 0, 0, 0, 345, 154, 221, 0] 
    ]
    while True:
        print(" \n Welcome to Middle Earth!")
        print("===================================")
        print("1. Print the shortest path from the Shire to various points in Middle Earth including the paths and the distances along the way.")
        print("2. Print what is the shortest path from the Shire to Rivendell, and then from Rivendell to Mt. Doom.")
        print("3. Exit")
        print("===================================")
        choice = int(input("Please select an option: "))
        if choice == 1:
            print("=== Starting out from the {} these are the shortest paths ===\n".format(g.nodeNames[0]))
            g.dijkstra(0)
        if choice == 2:
            print("=== Starting out from the {} but going to {} first, before heading to {} ===\n".format(g.nodeNames[0], g.nodeNames[2], g.nodeNames[10]))

            print("1st Leg: The Shire to Rivendell \n")
            # Shire index 0 to Rivendell index 2
            g.printSpecificPath(0, 2)  

            print("\n2nd Leg: Rivendell to Mt Doom \n")
            # Rivendell index 2 to Mt Doom index 10
            g.printSpecificPath(2, 10)  
        if choice == 3:
            print("Exiting the program.")
            break

main()