"""Assignment 6: Alpha-Beta Pruning"""

CODE = '''# Tree from the example: A (MAX) -> B, C (MIN) -> D, E, F, G (MAX) -> leaves
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [6, 9],
    'F': [1, 2],
    'G': [0, -1],
}
INF = float('inf')

def alphabeta(node, is_max, alpha, beta):
    best = -INF if is_max else INF
    for child in tree[node]:
        # a child is either another node (string) or a leaf value (number)
        value = alphabeta(child, not is_max, alpha, beta) if isinstance(child, str) else child
        if is_max:
            best = max(best, value)
            alpha = max(alpha, best)
        else:
            best = min(best, value)
            beta = min(beta, best)
        if beta <= alpha:  # pruning condition
            print(f"  Pruned remaining children of {node} (alpha={alpha}, beta={beta})")
            break
    print(f"Node {node} (\'MAX\' if is_max else \'MIN\') value = {best}")
    return best

print("Alpha-Beta Pruning")
result = alphabeta('A', True, -INF, INF)
print("Value of root A =", result)

# Output
# Alpha-Beta Pruning
# Node D (MAX) value = 5
#   Pruned remaining children of E (alpha=6, beta=5)
# Node E (MAX) value = 6
# Node B (MIN) value = 5
# Node F (MAX) value = 2
#   Pruned remaining children of C (alpha=5, beta=2)
# Node C (MIN) value = 2
# Node A (MAX) value = 5
# Value of root A = 5
'''

def alphabeta():
    """
    Assignment 6 - Alpha-Beta Pruning
    
    Prints the Alpha-Beta Pruning algorithm code for minimax game trees.
    Optimizes the minimax algorithm by pruning branches that cannot affect the result.
    Usage: heapplot.alphabeta()
    """
    print(CODE)
