"""Assignment 5: Hill Climbing Algorithm"""

CODE = '''graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
heuristic = {'A': 5, 'B': 3, 'C': 2, 'D': 6, 'E': 4, 'F': 0}

def hill_climbing(start):
    current = start
    path = [current]
    while True:
        neighbours = graph[current]
        if not neighbours:
            break
        best = min(neighbours, key=lambda n: heuristic[n])
        if heuristic[best] >= heuristic[current]:
            break
        current = best
        path.append(current)
    return path

path = hill_climbing('A')
print("Path:", " -> ".join(path))
print("Reached node:", path[-1], "|| Heuristic:", heuristic[path[-1]])

# Output
# Path: A -> C -> F
# Reached node: F || Heuristic: 0
'''

def hillclimbing():
    """
    Assignment 5 - Hill Climbing Algorithm
    
    Prints the Hill Climbing search algorithm code that greedily follows
    the steepest descent using heuristics.
    Usage: heapplot.hillclimbing()
    """
    print(CODE)
