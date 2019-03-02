'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@student: ajs94
@version March 2, 2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
    ])

# P(C | T1, T2)
#   = a * P(T1, T2 | C) * P(C)
#   = a * P(T1 | C) * P(T2 | C) * P(C)
#   = a * 0.9 * 0.9 * 0.01
#   = <0.17, 0.83>
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

# P(C | T1, -T2)
#   = a * P(T1, -T2 | C) * P(C)
#   = a * P(T1 | C) * P(-T2 | C) * P(C)
#   = a * 0.9 * 0.2 * 0.01
#   = <0.00565, 0.994>
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

# These results make sense because the chance of having cancer is low (0.01) and the
#   probability of the each test correctly determining if there is cancer is very high (0.9)
