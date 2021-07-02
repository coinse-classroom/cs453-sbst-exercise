import random
import math

MAX = 100
LEN = 10
BUDGET = 10000

# Create a hiddn vector of length LEN

hidden = []
for i in range(LEN):
    hidden.append(random.randrange(MAX))

def evaluate(solution):
    assert len(solution) == LEN
    return math.sqrt(sum([(p - q)**2 for (p, q) in zip(hidden, solution)]))

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

# to return the best solution found within budget, and spent cost
def avm(budget):
    return None, 0

guess, cost = hillclimbing(BUDGET)
print(guess, cost)
print(hidden)
# print(guess, evaluate(guess))