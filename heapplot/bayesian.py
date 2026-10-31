"""Assignment 10: Bayesian Network"""

CODE = '''# Practical 10: Bayesian Network - student exam performance
# Variables: e = exam level, i = IQ level, s = aptitude score, m = marks, a = admission
# Each value is 0 or 1. CPTs list [P(x=0), P(x=1)].

P_e = [0.7, 0.3]
P_i = [0.8, 0.2]
P_s_given_i = {0: [0.75, 0.25], 1: [0.4, 0.6]}
P_m_given_ie = {(0, 0): [0.6, 0.4], (0, 1): [0.9, 0.1],
                (1, 0): [0.5, 0.5], (1, 1): [0.8, 0.2]}
P_a_given_m = {0: [0.6, 0.4], 1: [0.9, 0.1]}

def joint(a, m, i, e, s):
    """P(a,m,i,e,s) = P(a|m) * P(m|i,e) * P(i) * P(e) * P(s|i)"""
    return (P_a_given_m[m][a] * P_m_given_ie[(i, e)][m] *
            P_i[i] * P_e[e] * P_s_given_i[i][s])

print("Case 1: difficult exam, low IQ, low aptitude, passes and gets admission")
print("P(a=1, m=1, i=0, e=1, s=0) =", round(joint(1, 1, 0, 1, 0), 4))
print("\\nCase 2: easy exam, high IQ, high aptitude, fails and no admission")
print("P(a=0, m=0, i=1, e=0, s=1) =", round(joint(0, 0, 1, 0, 1), 4))

# Extra: add up the joint over all 32 combinations
combos = [(a, m, i, e, s) for a in (0, 1) for m in (0, 1)
          for i in (0, 1) for e in (0, 1) for s in (0, 1)]
print("\\nSum of the joint over all 32 combinations =", round(sum(joint(*c) for c in combos), 4))
print("P(Admission = 1) =", round(sum(joint(*c) for c in combos if c[0] == 1), 4))

# Output
# Case 1: difficult exam, low IQ, low aptitude, passes and gets admission
# P(a=1, m=1, i=0, e=1, s=0) = 0.0018
#
# Case 2: easy exam, high IQ, high aptitude, fails and no admission
# P(a=0, m=0, i=1, e=0, s=1) = 0.0252
#
# Sum of the joint over all 32 combinations = 1.0
# P(Admission = 1) = 0.301
'''

def bayesian():
    """
    Assignment 10 - Bayesian Network
    
    Prints the Bayesian Network code modelling student exam performance
    using Conditional Probability Tables (CPTs).
    Usage: heapplot.bayesian()
    """
    print(CODE)
