"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@student: ajs94 Aaron Santucci
@version 9feb2019
"""
import time
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class sine(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':
    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30

    bestHillClimbing = 0
    bestSimAnnealing = 0

    sumHillClimbing = 0
    sumSimAnnealing = 0

    # the number of times to repeat the algorithms
    numSimulations = 100

    # Solve the problem using hill-climbing.
    t = time.time()
    for i in range(numSimulations):
        initial = randrange(0, maximum)
        p = sine(initial, maximum, delta=1.0)
        hill_solution = hill_climbing(p)
        sumHillClimbing += p.value(hill_solution)

        if p.value(hill_solution) > p.value(bestHillClimbing):
            bestHillClimbing = hill_solution

    hc_time = time.time() - t
    print('Hill-climbing solution       x: ' + str(bestHillClimbing)
          + '\tvalue: ' + str(p.value(bestHillClimbing))
          + '\taverage: ' + str(sumHillClimbing / numSimulations)
          + '\ttime: ' + str(hc_time)
          )

    # Solve the problem using simulated annealing.
    t = time.time()
    for i in range(numSimulations):
        initial = randrange(0, maximum)
        p = sine(initial, maximum, delta=1.0)
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        sumSimAnnealing += p.value(annealing_solution)
        if p.value(annealing_solution) > p.value(bestSimAnnealing):
            bestSimAnnealing = annealing_solution

    hc_time = time.time() - t
    print('Simulated annealing solution x: ' + str(bestSimAnnealing)
          + '\tvalue: ' + str(p.value(bestSimAnnealing))
          + '\taverage: ' + str(sumSimAnnealing / numSimulations)
          + '\ttime: ' + str(hc_time)
          )
