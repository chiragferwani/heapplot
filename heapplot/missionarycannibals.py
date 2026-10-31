"""Assignment 7: A* Algorithm - Missionaries and Cannibals Problem"""

CODE = '''# State = (missionaries on left, cannibals on left, boat side: 1 = left, 0 = right)
import heapq

START, GOAL = (3, 3, 1), (0, 0, 0)
MOVES = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]  # people in the boat

def is_valid(m, c):
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False
    left_ok  = (m == 0 or m >= c)               # left bank safe
    right_ok = (3 - m == 0 or 3 - m >= 3 - c)  # right bank safe
    return left_ok and right_ok

def next_states(state):
    m, c, boat = state
    sign = -1 if boat == 1 else 1              # left->right removes people from left
    for dm, dc in MOVES:
        nm, nc = m + sign * dm, c + sign * dc
        if is_valid(nm, nc):
            yield (nm, nc, 1 - boat)

def h(state):                                   # heuristic: people left / boat capacity
    return (state[0] + state[1]) // 2

def a_star():
    open_list = [(h(START), 0, START, [START])]  # (f, g, state, path)
    visited = set()
    while open_list:
        f, g, state, path = heapq.heappop(open_list)
        if state == GOAL:
            return path
        if state in visited:
            continue
        visited.add(state)
        for nxt in next_states(state):
            heapq.heappush(open_list, (g + 1 + h(nxt), g + 1, nxt, path + [nxt]))

path = a_star()
print("Solution found in", len(path) - 1, "moves\\n")
print("Step | Left (M,C) | Right (M,C) | Boat")
for i, (m, c, b) in enumerate(path):
    print(f"{i:>4} |   ({m},{c})    |   ({3 - m},{3 - c})     | {\'Left\' if b else \'Right\'}")

# Output
# Solution found in 11 moves
# Step | Left (M,C) | Right (M,C) | Boat
#    0 |   (3,3)    |   (0,0)     | Left
#    1 |   (2,2)    |   (1,1)     | Right
#  ...
#   11 |   (0,0)    |   (3,3)     | Right
'''

def missionarycannibals():
    """
    Assignment 7 - Missionaries and Cannibals Problem (A* Search)
    
    Prints the A* solution for the classic Missionaries and Cannibals river-crossing puzzle.
    State: (missionaries_left, cannibals_left, boat_side)
    Usage: heapplot.missionarycannibals()
    """
    print(CODE)
