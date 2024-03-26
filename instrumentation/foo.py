import math
import random
# import pytest

appr = 0
bdist = 0

K = 1

def norm(x):
    return 1.0 - math.pow(1.001, -x)

def fitness():
    return appr + norm(bdist)

# rewrite function foo so that whenever we call it, we get
# the fitness for the target branch
#
# you can add supporting functions, but you should update
# approx and bdist directly

def foo(x, y, z):
    if z >= 4:
        if z <= 10:
            if x == y:
                # target
                return True
            else:
                return False
        else:
            return False
    else:
        return False

LEN = 3
MAX = 256

def init_random(len, max):
    # randomly initialise a solution of length len, of randrange(max)
    sol = []
    for i in range(len):
        sol.append(random.randrange(max))
    return sol

def get_neighbour(sol):
    neighbours = []
    # generate neighbours of sol

    return neighbours

def evaluate(sol):
    foo(sol[0], sol[1], sol[2])
    return fitness()

# to return the best solution found within budget, and spent cost
def hillclimbing(budget):
    return sol, spent

sol, cost = hillclimbing(2000)
print(sol, cost)