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
    return None

def get_neighbour(sol):
    neighbours = []
    # generate neighbours of sol
    return neighbours

# to return the best solution found within budget, and spent cost
def hillclimbing(budget):
    return None, None

# to return the best solution found within budget, and spent cost
def avm(budget):
    return None, None

guess, cost = hillclimbing(BUDGET)
print(guess, cost)