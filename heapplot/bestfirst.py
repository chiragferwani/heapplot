"""Assignment 2: Best First Search"""

CODE = '''import heapq

graph = {
    'A': [('B', 1), ('C', 1)],
    'B': [('D', 1), ('E', 1)],
    'C': [('F', 1)],
    'D': [], 'E': [], 'F': []
}
heuristic = {'A': 6, 'B': 4, 'C': 5, 'D': 7, 'E': 3, 'F': 0}

def best_first_search(start, goal):
    visited = set()
    pq = [(heuristic[start], start)]
    while pq:
        h, node = heapq.heappop(pq)
        if node in visited:
            continue
        print(node, end=" ")
        visited.add(node)
        if node == goal:
            print("\\nGoal reached!")
            return
        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(pq, (heuristic[neighbour], neighbour))

best_first_search('A', 'F')

# Output
# A B E C F
# Goal reached!
'''

def bestfirst():
    """
    Assignment 2 - Best First Search
    
    Prints the Best First Search algorithm code using a priority queue with heuristics.
    Usage: heapplot.bestfirst()
    """
    print(CODE)
