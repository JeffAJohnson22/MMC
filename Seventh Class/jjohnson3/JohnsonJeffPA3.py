"""
Project #3: The Smart Navigator (A* vs. BFS)
Name: Jeff Johnson
Date: 02/02/2026
"""

import heapq
from collections import deque

def get_neighbors(node, grid):
    """Returns valid North, South, East, West neighbors (0 = path, 1 = wall)."""
    neighbors = []
    rows, cols = len(grid), len(grid[0])
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = node[0] + dr, node[1] + dc
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
            neighbors.append((r, c))
    return neighbors

def manhattan_distance(a, b):
    """
    TASK: Implement Manhattan Distance h(n)
    Formula: |x1 - x2| + |y1 - y2|
    """
    if a == b:
        return 0
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def breadth_first_search(grid, start, goal):
    """
    TASK: Implement Breadth-First Search.
    - Use 'deque' for the frontier.
    - Return the total count of nodes visited.
    """
    nodes_visited = 0
    frontier = deque([start])
    visited = set()
    
    while frontier:
        node = frontier.popleft()
        
        if node in visited:
            continue
        
        visited.add(node)
        nodes_visited += 1
        
        if node == goal:
            return nodes_visited
        
        for neighbor in get_neighbors(node, grid):
            if neighbor not in visited:
                frontier.append(neighbor)
    
    return nodes_visited

def a_star_search(grid, start, goal):
    """
    TASK: Implement A* Search.
    - Use 'heapq' for the priority queue.
    - Use the tie-breaker: priority = (g + h) + (h * 0.001)
    - Return the total count of nodes visited.
    """
    nodes_visited = 0
    manhattan_result = manhattan_distance(start, goal)
    priority = 0 + manhattan_result + (manhattan_result * 0.001)
    frontier = [(priority, start)]
    visited = set()
    value = {start: 0}
    
    while frontier:
        _, node = heapq.heappop(frontier)
        
        if node in visited:
            continue
        
        visited.add(node)
        nodes_visited += 1
        
        if node == goal:
            return nodes_visited
        
        for neighbor in get_neighbors(node, grid):
            new_hotness = value[node] + 1
            
            if neighbor not in value or new_hotness < value[neighbor]:
                value[neighbor] = new_hotness
                mh_result = manhattan_distance(neighbor, goal)
                priority = new_hotness + mh_result + (mh_result * 0.001)
                heapq.heappush(frontier, (priority, neighbor))
    
    return nodes_visited

# ==========================================================
# TEST MAZES
# ==========================================================

# 1. WINDING MAZE (10x10)
m1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# 2. CHECKERBOARD (10x10)
m2 = [[(r+c)%2 if (0<r<9 and 0<c<9) else 0 for c in range(10)] for r in range(10)]

# 3. THE SPIRAL (12x12)
m3 = [[0]*12 for _ in range(12)]
for i in range(2, 10):
    m3[2][i] = m3[i][10] = m3[10][11-i] = m3[11-i][2] = 1
m3[3][2] = 0 

# 4. CORRIDORS (10x10)
m4 = [[0]*10 for _ in range(10)]
for r in [2, 4, 6, 8]:
    for c in range(0, 9): m4[r][c] = 1
for r in [1, 3, 5, 7]:
    m4[r][9] = 1

# ==========================================================
# TEST EXECUTION
# ==========================================================
start = (0, 0)
print(f"1. WINDING MAZE - BFS: {breadth_first_search(m1, start, (9,9))} | A*: {a_star_search(m1, start, (9,9))}")
print(f"2. CHECKERBOARD - BFS: {breadth_first_search(m2, start, (9,9))} | A*: {a_star_search(m2, start, (9,9))}")
print(f"3. THE SPIRAL   - BFS: {breadth_first_search(m3, start, (6,6))} | A*: {a_star_search(m3, start, (6,6))}")
print(f"4. CORRIDORS    - BFS: {breadth_first_search(m4, start, (9,0))} | A*: {a_star_search(m4, start, (9,0))}")