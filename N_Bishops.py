from constraint import *


# Postavuvanje na N lovci na tabla NxN bez da se napagjaat

def findSolution(b1, b2):
    if abs(b1[0] - b2[0]) == abs(b1[1] - b2[1]):
        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    domain = []
    bishops = []
    N = int(input())
    for i in range(0, N):
        bishops.append(i)
        for j in range(0, N):
            domain.append((i, j))
    problem.addVariables(bishops, domain)
    for b1 in bishops:
        for b2 in bishops:
            if b2 < b1:
                problem.addConstraint(findSolution, (b1, b2))
    print(problem.getSolution())
