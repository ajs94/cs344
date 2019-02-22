"""
a course-scheduling domain and implement it using the AIMA constraint satisfaction framework
https://cs.calvin.edu/courses/cs/344/kvlinden/03constraint/homework.html

@author: ajs94
@version 21feb2019
"""

import time
from csp import min_conflicts, \
    CSP, parse_neighbors


class Scheduler:

    def __init__(self, courses, schedule, staff, rooms):
        self.schedule = schedule
        self.staff = staff
        self.rooms = rooms

        self.possible_setups = []
        self.variables = courses
        self.domains = {}
        self.neighbors = {}

    # variables: a list of variables; each is atomic (e.g. int or string).
    def get_variables(self):
        return self.variables

    # domains: a dict of {var:[possible_value, ...]} entries.
    def get_domains(self):
        for prof in self.staff:
            for timeslot in self.schedule:
                for room in self.rooms:
                    self.possible_setups.append(prof + " " + timeslot + " " + room)
        for var in self.variables:
            self.domains[var] = self.possible_setups

        return self.domains

    # neighbors: a dict of {var:[var,...]} that for each variable lists
    #   the other variables that participate in constraints.
    def get_neighbors(self):
        self.neighbors = parse_neighbors("junk: filler")
        for type in [self.variables, self.possible_setups]:
            for A in type:
                for B in type:
                    if A != B:
                        if B not in self.neighbors[A]:
                            self.neighbors[A].append(B)
                        if A not in self.neighbors[B]:
                            self.neighbors[B].append(A)

        return self.neighbors

    # constraints: a function f(A, a, B, b) that returns true if neighbors
    #   A, B satisfy the constraint when they have values A=a, B=b
    def constraint_check(self, A, a, B, b):
        # split[0] = professor, split[1] = time, split[2] = room
        splitA = a.split()
        splitB = b.split()
        # Check if same professor and time
        if ((splitA[0] == splitB[0]) and (splitA[1] == splitB[1])):
            return False
        # Check if same time and room
        if ((splitA[1] == splitB[1]) and (splitA[2] == splitB[2])):
            return False

        return True

    def get_csp(self):
        return CSP(self.get_variables(), self.get_domains(), self.get_neighbors(), self.constraint_check)


if __name__ == '__main__':

    # the stuff to be scheduled ...
    courses = ["CS-108", "CS-112", "CS-212", "CS-214", "CS-232", "CS-336", "CS-344"]
    timeslots = ["MWF9AM", "MWF1030AM", "MWF130PM", "TTH1030AM", "TTH130PM"]
    professors = ["Plantinga", "Adams", "Norman", "VanderLinden", "Schuurman"]
    classrooms = ["SB-410", "SB-411"]

    t = time.time()
    Scheduler = Scheduler(courses, timeslots, professors, classrooms)
    solution = min_conflicts(Scheduler.get_csp())
    total_time = time.time() - t

    if solution is not None:
            print('Schedule found:\t' + str(solution)
          + '\n\ttime: ' + str(total_time)
          )
