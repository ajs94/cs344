'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@student: ajs94
@version Feb 22, 2019
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())

"""
By Hand:
    P(Cavity | catch) = P(Cavity and Catch)/P(Catch) = .108 / .34 = .529
In Program:
    PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
    False: 0.471, True: 0.529    
"""

P = JointProbDist(['Coin1', 'Coin2'])
Heads, tails = True, False
P[T, T] = 0.25
P[F, T] = 0.25
P[T, F] = 0.25
P[F, F] = 0.25

PC = enumerate_joint_ask('Coin2', {'Coin1': Heads}, P)
print(PC.show_approx())

"""
This is correct given that we know that flipping one coin is independent of
    flipping another, each flip is .5/.5 split.
"""