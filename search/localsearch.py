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

EXP = 0
PAT = 1

INC = 0
DEC = 1

# to return the best solution found within budget, and spent cost
def avm(budget):
    
    mode = EXP # current search mode: EXP or PAT
    dirr = None # current move direction: INC or DEC
    cv = 0 # index of current variable we are looking at
    
    step = 1 # we move 2**step in dirr direction in PAT mode
    spent = 0 # record the number of fitness evaluation

    explore_failed = [0] * LEN # record 1 if EXP move for variable failed

    sol = init_random(LEN, MAX)
    fit = evaluate(sol)
    spent += 1
    
    while spent < budget:
        # exploratory move
        if mode == EXP:
            # try increase and decrease
            _inc = sol[:]
            _inc[cv] += 1
            _dec = sol[:]
            _dec[cv] -= 1

            # evaluate both increase and decrease
            fit_inc = evaluate(_inc)
            spent += 1
            fit_dec = evaluate(_dec)
            spent += 1

            if fit_inc < fit: # increase is the right direction
                dirr = INC 
                sol = _inc[:]
                fit = fit_inc
                explore_failed[cv] = 0 # record that exploration succeeded
                mode = PAT # switch to PATTERN move
            elif fit_dec < fit: # decrease is the right direction
                dirr = DEC
                sol = _dec[:]
                fit = fit_dec
                explore_failed[cv] = 0
                mode = PAT
            else:
                # check if we have failed with exploration of all variables
                explore_failed[cv] = 1
                if sum(explore_failed) == LEN:
                    break
                cv = (cv + 1) % LEN
        elif mode == PAT:
            delta = 2 ** step # the distnace we move this time
            next_sol = sol[:] # where we end up when we move: first copy
            # add delta
            next_sol[cv] = next_sol[cv] + delta if dirr == INC else next_sol[cv] - delta
            fit_next = evaluate(next_sol)
            spent += 1
            
            # if fitness improves, move sol to next_sol, and increase step
            if fit_next <= fit:
                sol = next_sol[:]
                step += 1
            # overshooting: reset the step, set mode to EXP
            else:
                step = 1
                mode = EXP
                cv = (cv + 1) % LEN # try the next variable
    return sol, spent

guess, cost = hillclimbing(BUDGET)
print(guess, cost)

guess, cost = avm(BUDGET)
print(guess, cost)

print(hidden)

# print(guess, evaluate(guess))