"""Assignment 1: Depth Limited Search"""

CODE = '''graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : ['G'],
    'E' : [],
    'F' : [], 
    'G' : []
}

visited = set()

def dls(node, depth, limit):
    if depth > limit: 
        return
    if node not in visited: 
        print(node, end="")
        visited.add(node)
        for neighbour in graph[node]:
            dls(neighbour, depth+1, limit)

dls('A', 0, 2)

# Output
# A B D E C F
'''

def dls():
    """
    Assignment 1 - Depth Limited Search (DLS)
    
    Prints the Depth Limited Search code for a sample graph with depth limit = 2.
    Usage: heapplot.dls()
    """
    print(CODE)
