def BFS(V,E):
    for i in range(len(V)):
        V[i] = -1
    count = 0
    for i in range(len(V)):
        if V[i] == -1:
            Q = [i]
            V[i], count = count, count + 1
            print(f"Vertex {i} visited", V)
            while (len(Q) != 0):
                print(f"Vertex {Q[0]} dequeued", Q)
                for e in E:
                    if e[0] == Q[0] and V[e[1]] == -1:
                        Q.append(e[1])
                        V[e[1]], count = count, count + 1
                        print(f"Vertex {e[1]} enqueued", Q)
                    elif e[1] == Q[0] and V[e[0]] == -1:
                        Q.append(e[0])
                        V[e[0]], count = count, count + 1
                        print(f"Vertex {e[0]} enqueued", Q)
                Q.pop(0)

# def BFS(V, E):
#     for i in range(len(V)):
#         V[i] = -1  
#     count = 0
#     for i in range(len(V)):
#         if V[i] == -1:
#             Q = [i]
#             print(f"Vertex {chr(65+i)} visited", V)
#             V[i], count = count, count + 1
#             while len(Q) != 0:
#                 current = Q[0]
#                 print(f"Vertex {chr(65+current)} dequeued", Q)
#                 for e in E:
#                     if e[0] == current and V[e[1]] == -1: 
#                         Q.append(e[1])
#                         V[e[1]], count = count, count + 1
#                         print(f"Vertex {chr(65+e[1])} enqueued", Q)
#                         print(f"Vertex {chr(65+e[1])} visited", V)
#                 Q.pop(0)


# V = [0] * 9
# E = [[0,1,1], [0,2,1], [0,3,1], [1,4,1], [3,6,1], [4,5,1], [4,7,1], [5,8,1], [7,8,1] ]
# BFS(V,E)

V = [-1] * 8
E = [
    (0, 4),  # A → E
    (0, 7),  # A → H
    (1, 0),  # B → A
    (2, 6),  # C → G
    (2, 5),  # C → F
    (3, 4),  # D → E
    (3, 0),  # D → A
    (4, 2),  # E → C
    (5, 3),  # F → D
    (5, 4),  # F → E
    (6, 1),  # G → B
    (6, 4),  # G → E
    (7, 3)   # H → D
]


BFS(V, E)
# A 0
# B 1
# C 2
# D 3
# E 4
# F 5
# G 6
# H 7

