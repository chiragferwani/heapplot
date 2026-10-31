"""Assignment 3: 8-Puzzle Problem"""

CODE = '''import heapq

def h(state, goal):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

def neighbours(state):
    i = state.index(0)
    row, col = divmod(i, 3)
    moves = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            j = r * 3 + c
            new_state = list(state)
            new_state[i], new_state[j] = new_state[j], new_state[i]
            moves.append(tuple(new_state))
    return moves

def solve(start, goal):
    pq = [(h(start, goal), 0, start)]
    visited = {start: 0}
    while pq:
        f, g, state = heapq.heappop(pq)
        if state == goal:
            print("Goal State Reached")
            print("Number of moves:", g)
            return
        for n in neighbours(state):
            new_g = g + 1
            if n not in visited or new_g < visited[n]:
                visited[n] = new_g
                heapq.heappush(pq, (new_g + h(n, goal), new_g, n))
    print("No solution found")

start = (1, 2, 3, 5, 6, 0, 7, 8, 4)
goal  = (1, 2, 3, 5, 8, 6, 0, 7, 4)
print("Initial State:", start)
print("Goal State:   ", goal)
solve(start, goal)

# Output
# Initial State: (1, 2, 3, 5, 6, 0, 7, 8, 4)
# Goal State:    (1, 2, 3, 5, 8, 6, 0, 7, 4)
# Goal State Reached
# Number of moves: 3
'''

def puzzle8():
    """
    Assignment 3 - 8-Puzzle Problem (A* Search)
    
    Prints the 8-puzzle solver code using A* with misplaced tiles heuristic.
    Usage: heapplot.puzzle8()
    """
    print(CODE)
