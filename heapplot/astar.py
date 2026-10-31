"""Assignment 2: A* Algorithm"""

CODE = '''import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [], 'E': [], 'F': []
}
heuristic = {'A': 6, 'B': 4, 'C': 5, 'D': 2, 'E': 0, 'F': 3}

def a_star(start, goal):
    pq = [(heuristic[start], 0, start)]
    visited = set()
    while pq:
        f, g, node = heapq.heappop(pq)
        if node in visited:
            continue
        print(node, "|| g =", g, "|| f =", f)
        visited.add(node)
        if node == goal:
            print("Goal reached with total cost", g)
            return
        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                new_g = g + cost
                heapq.heappush(pq, (new_g + heuristic[neighbour], new_g, neighbour))

a_star('A', 'E')

# Output
# A || g = 0 || f = 6
# B || g = 1 || f = 5
# D || g = 3 || f = 5
# E || g = 6 || f = 6
# Goal reached with total cost 6
'''

def astar():
    """
    Assignment 2 - A* Algorithm
    
    Prints the A* search algorithm code that finds the optimal path using f = g + h.
    Usage: heapplot.astar()
    """
    print(CODE)
