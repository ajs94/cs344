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
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# P(Alarm | burglary ∧ ¬earthquake)
# From the table: < .04, .96 >
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# P(John | burglary ∧ ¬earthquake)
#   a * [ P( J | A ) * P( A | B, -E ) + P( J | -A ) * P( -A | B, -E) ]
#   = a * (0.9 * 0.94 + 0.05 * 0.06)
#   = < .151, .849 >
print(elimination_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# P(Burglary | alarm) =
#   a * [ P(B) * P(E) * P( A | B, E ) + P(B) * P(-E) * P( A | B, -E) ]
#   = a * (0.001 * 0.002 * 0.95 + 0.001 * 0.998 * 0.94)
#   = <0.374, 0.626>
print(elimination_ask('Burglary', dict(Alarm=T), burglary).show_approx())

# P(Burglary | john ∧ mary)
#   = <.284, .716>
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
