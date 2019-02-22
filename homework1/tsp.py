"""
Travelling Sales Person problem using hill climbing and simulated annealing
https://en.wikipedia.org/wiki/Travelling_salesman_problem

@author: ajs94
@version 20feb2019
"""

import time
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule
from random import randrange


class TSP(Problem):

    def __init__(self, mapSize, pathsList):
        self.mapSize = mapSize
        self.pathsList = pathsList

        # Starting point is random
        self.initial = []
        self.initial.append(randrange(0, mapSize - 1))
        print("Starting point:\t" + str(self.initial[0]) + "\n")

    def actions(self, state):
        actions = []
        for point in range(0, mapSize):
            if point not in state:
                actions.append(point)
        return actions

    def result(self, state, move):
        new_state = state[:]
        new_state.append(move)
        return new_state

    def value(self, state):
        value = 0
        for i in range(0, len(state) - 1):
            spot = (i + 1) % mapSize
            value += self.pathsList[tuple(sorted((state[i], state[spot])))]
        return value


if __name__ == '__main__':

    # for size anything below about 20-30 the time will be ~0
    mapSize = 100
    pathsList = {}

    # assign each path links and randomized distances with other points
    # ae '(0, 1): 10' is point 0's link to point 1 with a distance of 10
    for i in range(0, mapSize):
        for k in range(i + 1, mapSize):
            path = (i, k)
            path_dist = randrange(1, 11)
            pathsList[path] = path_dist

    # don't over-clutter the screen with paths and distances
    if mapSize <= 10:
        print('Paths:\t' + str(pathsList ))

    problem = TSP(mapSize, pathsList)

    t = time.time()
    hill_climbing = hill_climbing(problem)
    hc_time = time.time() - t

    print('Hill climbing:\t' + str(hill_climbing)
          + '\n\tvalue: ' + str(problem.value(hill_climbing))
          + '\n\ttime: ' + str(hc_time)
          )

    t = time.time()
    sim_annealing = simulated_annealing(problem, exp_schedule(k=20, lam=0.005, limit=1000))
    sa_time = time.time() - t

    print('Simulated annealing\t: ' + str(sim_annealing )
          + '\n\tvalue: ' + str(problem.value(sim_annealing ))
          + '\n\ttime: ' + str(sa_time)
          )
