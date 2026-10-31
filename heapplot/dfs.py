"""Assignment 1: Depth First Search"""

CODE = '''graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

visited = set()

def dfs(node): 
    if node not in visited:
        print(node, end="")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(neighbour)

dfs('A')

# Output
# A B D E C F
'''

def dfs():
    """
    Assignment 1 - Depth First Search (DFS)
    
    Prints the DFS traversal code for a sample graph.
    Usage: heapplot.dfs()
    """
    print(CODE)
