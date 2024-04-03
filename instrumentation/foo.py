import math
import random
# import pytest

appr = 0
bdist = 0

K = 1

def bdist_gte(level, x, y):
    global appr, bdist
    appr = 2 - level
    bdist = y - x + K
    return x >= y

def bdist_lte(level, x, y):
    global appr, bdist
    appr = 2 - level
    bdist = x - y + K
    return x <= y

def bdist_eq(level, x, y):
    global appr, bdist
    appr = 2 - level
    bdist = abs(x - y)
    return x == y

def norm(x):
    return 1.0 - math.pow(1.001, -x)

def fitness():
    global appr, bdist
    return appr + norm(bdist)

# rewrite function foo so that whenever we call it, we get
# the fitness for the target branch
#
# you can add supporting functions, but you should update
# approx and bdist directly

def foo(a, b, c):
    if bdist_gte(0, c, 4):
        if bdist_lte(1, c, 10):
            if bdist_eq(2, a, b):
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

def init_random(length, maxvalue):
    # randomly initialise a solution of length len, of randrange(max)
    sol = []
    for i in range(length):
        sol.append(random.randrange(maxvalue))
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
    
    sol = init_random(3, 1000)
    current_fitness = evaluate(sol)
    cost = 1

    while cost < budget:
        neighbours = get_neighbour(sol)
        is_top = True
        for n in neighbours:
            n_fitness = evaluate(n)
            cost += 1
            if n_fitness < current_fitness:
                is_top = False
                sol = n[:]
                current_fitness = n_fitness

        if is_top:
            break

    print("cost:", cost)
    return sol, current_fitness

def avm(budget):

    MODE = 0 # 0 is exploratory, 1 is accelleration
    INDEX = 0
    DIR = 1

    sol = init_random(LEN, MAX)
    current_fitness = evaluate(sol)
    cost = 1

    while cost < budget:
        if current_fitness == 0:
            break

        if MODE == 0: # exploratory mode
            inc_candidate = sol[:]
            inc_candidate[INDEX] += 1
            inc_fitness = evaluate(inc_candidate)
            cost += 1

            dec_candidate = sol[:]
            dec_candidate[INDEX] -= 1
            dec_fitness = evaluate(dec_candidate)
            cost += 1

            if inc_fitness < current_fitness:
                DIR = 1
                MODE = 1
                sol = inc_candidate[:]
                current_fitness = inc_fitness
            elif dec_fitness < current_fitness:
                DIR = -1
                MODE = 1
                sol = dec_candidate[:]
                current_fitness = dec_fitness
            else: # we need to look at the next variable
                MODE = 0
                INDEX = (INDEX + 1) % len(sol)
        else: # accelleration
            num_steps = 1
            while True:
                next_candidate = sol[:]
                next_candidate[INDEX] += DIR * 2 ** num_steps

                next_fitness = evaluate(next_candidate)
                cost += 1

                # check for overshooting
                if next_fitness >= current_fitness:
                    MODE = 0
                    INDEX = (INDEX + 1) % len(sol)
                    break
                else:
                    sol = next_candidate[:]
                    current_fitness = next_fitness
                    num_steps += 1

    print("cost:", cost)
    return sol, current_fitness


print(hillclimbing(10000))
print(avm(10000))

