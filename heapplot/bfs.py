"""Assignment 1: Breadth First Search"""

CODE = '''from collections import deque

graph ={
        'A':['B','C'],
        'B':['D','E'],
        'C':['F'],
        'D':[],
        'E':[],
        'F':[]
}

def bfs (graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end =" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
 
bfs(graph,'A')

# Output
# A B C D E F
'''

def bfs():
    """
    Assignment 1 - Breadth First Search (BFS)
    
    Prints the BFS traversal code for a sample graph.
    Usage: heapplot.bfs()
    """
    print(CODE)
