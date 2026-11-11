"""root finding algorithms, as developed in Notebook 8"""


class RootFinder:
    """a blueprint class for root finding algorithms"""

    def __init__(self, f, f1=None, eps=1e-6, M=99):
        self.f = f
        self.f1 = f1
        self.eps = eps
        self.M = M

    def solve(self, a, b=None):
        raise NotImplementedError("Subclass must implement solve().")


class BisectionSolver(RootFinder):
    """root finding by repeated bisection of an interval [a, b]"""

    def solve(self, a, b):  # overwrite parent's method
        f = self.f
        if f(a) * f(b) >= 0:
            raise ValueError("end points must have opposite signs")
        for i in range(self.M):
            c = (a+b)/2
            if abs(f(c)) < self.eps:
                return c
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        print("Warning: maximum iterations reached.")
        return c


class NewtonSolver(RootFinder):
    """root finding by Newton's method, starting from a guess a"""

    def solve(self, a, b=None):
        f, f1 = self.f, self.f1
        if f1 is None:
            raise ValueError("Newton's method needs the derivative f1")
        for i in range(self.M):
            y = f(a)
            if abs(y) < self.eps:
                return a
            a -= y/f1(a)
        print("Warning: maximum iterations reached.")
        return a
