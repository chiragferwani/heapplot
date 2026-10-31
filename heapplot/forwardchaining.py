"""Assignment 9: Forward Chaining"""

CODE = '''# Each rule is (list of premises, conclusion)
rules = [
    (['A', 'B'], 'C'),   # IF A and B THEN C
    (['C'], 'D'),        # IF C THEN D
    (['D', 'E'], 'F'),   # IF D and E THEN F
    (['G'], 'H'),        # IF G THEN H (never fires, G is unknown)
]
facts = ['A', 'B', 'E']
query = 'F'

print("Known facts:", facts)
print("Query      :", query, "\\n")

inferred_path = []
new_fact_found = True
while query not in facts and new_fact_found:
    new_fact_found = False
    for premises, conclusion in rules:
        if conclusion not in facts and all(p in facts for p in premises):
            facts.append(conclusion)                       # infer a new fact
            inferred_path.append(f"{' and '.join(premises)} -> {conclusion}")
            print("Rule fired:", inferred_path[-1])
            new_fact_found = True

print()
if query in facts:
    print(f"SUCCESS: \'{query}\' is derived.")
    print("Inference path:", " ; ".join(inferred_path))
else:
    print(f"FAILURE: \'{query}\' cannot be derived.")
print("Final facts:", facts)

# Output
# Known facts: ['A', 'B', 'E']
# Query      : F
# Rule fired: A and B -> C
# Rule fired: C -> D
# Rule fired: D and E -> F
# SUCCESS: 'F' is derived.
# Inference path: A and B -> C ; C -> D ; D and E -> F
# Final facts: ['A', 'B', 'E', 'C', 'D', 'F']
'''

def forwardchaining():
    """
    Assignment 9 - Forward Chaining (Rule-Based Inference)
    
    Prints the Forward Chaining inference engine code.
    Applies rules data-driven to derive new facts until the query is satisfied.
    Usage: heapplot.forwardchaining()
    """
    print(CODE)
