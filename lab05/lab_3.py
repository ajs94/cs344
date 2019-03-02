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
sunny = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1}),
    ])

# P(Raise | sunny)
#   These are independent, so it's just P(Raise)
#   = <0.01, 0.99>
print(enumeration_ask('Raise', dict(Sunny=T), sunny).show_approx())

# P(Raise | happy ∧ sunny)
#   = a * P(H | S, R) * P(R)
#   = a * 1.0 * 0.01
#   <0.0142, 0.986>
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), sunny).show_approx())

# P(Raise | happy)
# <0.0185, 0.982>
print(enumeration_ask('Raise', dict(Happy=T), sunny).show_approx())

# P(Raise | happy ∧ ¬sunny)
# <0.0833, 0.917>
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), sunny).show_approx())

# These results make sense given that P(Raise) is so small so it's unlikely that
#   it occurs regardless, but Happy and Sunny have high probabilities so they raises these probabilities.
