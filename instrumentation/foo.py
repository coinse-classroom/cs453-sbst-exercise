import math
import pytest

appr = 0
bdist = 0

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


foo(11, 2, 1)
assert 2.004 == pytest.approx(fitness(), 0.001)

foo(11, 2, 11)
assert 1.001 == pytest.approx(fitness(), 0.001)

foo(11, 2, 9)
assert 0.009 == pytest.approx(fitness(), 0.001)

foo(2, 2, 9)
assert fitness() == 0