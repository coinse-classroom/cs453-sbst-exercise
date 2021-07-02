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

def branch_lte(_id, x, y):
    global bdist, appr
    appr = 2 - _id
    bdist = x - y + K
    return x <= y

def branch_gte(_id, x, y):
    global bdist, appr
    appr = 2 - _id
    bdist = y - x + K
    return x >= y

def branch_eq(_id, x, y):
    global bdist, appr
    appr = 2 - _id
    bdist = abs(x - y)
    return x == y

# rewrite function foo so that whenever we call it, we get
# the fitness for the target branch
#
# you can add supporting functions, but you should update
# approx and bdist directly

def foo(x, y, z):
    if branch_gte(0, z, 4):
        if branch_lte(1, z, 10):
            if branch_eq(2, x, y):
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
    for i in range(len(sol)):
        n1 = sol[:]
        n1[i] += 1
        n2 = sol[:]
        n2[i] -= 1
        neighbours.append(n1)
        neighbours.append(n2)
    return neighbours

def evaluate(sol):
    foo(sol[0], sol[1], sol[2])
    return fitness()

# to return the best solution found within budget, and spent cost
def hillclimbing(budget):
    climb = True
    spent = 0
    sol = init_random(LEN, MAX)
    s_fit = evaluate(sol)
    spent += 1
    while climb and spent < budget:
        neighbours = get_neighbour(sol)
        climb = False
        for n in neighbours:
            n_fit = evaluate(n)
            spent += 1
            if n_fit < s_fit:
                sol = n[:]
                s_fit = n_fit
                climb = True
    return sol, spent

sol, cost = hillclimbing(2000)
print(sol, cost)