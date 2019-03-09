'''
This module implements the Bayesian network shown in the text, Figure 14.12.
It's taken from the AIMA Python code.

@student: ajs94
@version March 8, 2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
weather = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: 0.1, F: 0.5}),
    ('Rain', 'Cloudy', {T: 0.8, F: 0.2}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.9, (F, T): 0.9, (F, F): 0.0})
    ])


# i.        P(Cloudy) = 0.5
#           Given from info
#           = <0.5, 0.5>
print(enumeration_ask('Cloudy', dict(), weather).show_approx())

# ii.       P(Sprinkler | cloudy) = 0.1
#           Given from info
#           = <0.1, 0.9>
print(enumeration_ask('Sprinkler', dict(Cloudy=T), weather).show_approx())

# iii.      P(Cloudy | the sprinkler is running and it’s not raining)
#           = a * P(Sprinkler, -Rain|Cloudy) * P(Cloudy)
#           = a * 0.1 * 0.2 * 0.5
#           = a * <0.01, .2>
#           = <0.0476, 0.952>
print(enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=F), weather).show_approx())

# iv.       P(WetGrass | it’s cloudy, the sprinkler is running and it’s raining) = 0.99
#           Given from info
#           = <0.01, 0.99>
print(enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), weather).show_approx())

# v.        P(Cloudy | -WestGrass)
#           = a * ...?
#           I have no idea how to start/work through this...
#           = <0.361, 0.639>
print(enumeration_ask('Cloudy', dict(WetGrass=F), weather).show_approx())
