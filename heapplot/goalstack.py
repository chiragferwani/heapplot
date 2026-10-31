"""Assignment 8: Goal Stack Planning"""

CODE = '''# Predicates are tuples, e.g. ('ON', 'B', 'A'), ('ONTABLE', 'A'), ('ARMEMPTY',)
state = {('ON', 'B', 'A'), ('ONTABLE', 'A'), ('ONTABLE', 'C'), ('ONTABLE', 'D'),
         ('CLEAR', 'B'), ('CLEAR', 'C'), ('CLEAR', 'D'), ('ARMEMPTY',)}
goal = [('ON', 'C', 'A'), ('ON', 'B', 'D'), ('ONTABLE', 'A'), ('ONTABLE', 'D'),
        ('CLEAR', 'B'), ('CLEAR', 'C'), ('ARMEMPTY',)]

def operator(name, x, y=None):
    """Return (preconditions, delete list, add list) of an operator."""
    if name == 'STACK':
        return ([('CLEAR', y), ('HOLDING', x)],
                [('CLEAR', y), ('HOLDING', x)],
                [('ARMEMPTY',), ('ON', x, y), ('CLEAR', x)])
    if name == 'UNSTACK':
        return ([('ARMEMPTY',), ('ON', x, y), ('CLEAR', x)],
                [('ARMEMPTY',), ('ON', x, y), ('CLEAR', x)],
                [('HOLDING', x), ('CLEAR', y)])
    if name == 'PICKUP':
        return ([('CLEAR', x), ('ONTABLE', x), ('ARMEMPTY',)],
                [('ONTABLE', x), ('CLEAR', x), ('ARMEMPTY',)],
                [('HOLDING', x)])
    if name == 'PUTDOWN':
        return ([('HOLDING', x)],
                [('HOLDING', x)],
                [('ONTABLE', x), ('CLEAR', x), ('ARMEMPTY',)])

def achiever(pred):
    """Pick the operator that makes a predicate true in the current state."""
    kind = pred[0]
    if kind == 'ON':
        return ('STACK', pred[1], pred[2])
    if kind == 'ONTABLE':
        return ('PUTDOWN', pred[1])
    if kind == 'CLEAR':      # remove whatever block is on top
        top = next(p[1] for p in state if p[0] == 'ON' and p[2] == pred[1])
        return ('UNSTACK', top, pred[1])
    if kind == 'HOLDING':
        x = pred[1]
        if ('ONTABLE', x) in state:
            return ('PICKUP', x)
        below = next(p[2] for p in state if p[0] == 'ON' and p[1] == x)
        return ('UNSTACK', x, below)
    if kind == 'ARMEMPTY':   # put down whatever the arm holds
        held = next(p[1] for p in state if p[0] == 'HOLDING')
        return ('PUTDOWN', held)

plan = []
stack = [('GOAL', goal)] + [('PRED', p) for p in reversed(goal)]
while stack:
    kind, item = stack.pop()
    if kind == 'PRED':
        if item not in state:
            op = achiever(item)
            stack.append(('ACTION', op))
            stack.append(('GOAL', operator(*op)[0]))
            stack.extend(('PRED', p) for p in reversed(operator(*op)[0]))
    elif kind == 'GOAL':
        if not all(p in state for p in item):   # re-check the sub-goal list
            stack.append(('GOAL', item))
            stack.extend(('PRED', p) for p in reversed(item))
    else:  # ACTION: apply it to the world state
        _, delete, add = operator(*item)
        state = (state - set(delete)) | set(add)
        plan.append(item)

print("Plan to reach the goal state:")
for i, op in enumerate(plan, 1):
    print(f"{i}. {op[0]}({', '.join(op[1:])})")
print("\\nGoal reached:", all(p in state for p in goal))

# Output
# Plan to reach the goal state:
# 1. UNSTACK(B, A)
# 2. PUTDOWN(B)
# 3. PICKUP(C)
# 4. STACK(C, A)
# 5. PICKUP(B)
# 6. STACK(B, D)
# Goal reached: True
'''

def goalstack():
    """
    Assignment 8 - Goal Stack Planning
    
    Prints the Goal Stack Planning algorithm code for the blocks world problem.
    Uses STRIPS-style operators: STACK, UNSTACK, PICKUP, PUTDOWN.
    Usage: heapplot.goalstack()
    """
    print(CODE)
