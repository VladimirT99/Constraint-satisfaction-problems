from constraint import *

# Postavuvanje na konji na shahovska tabla bez da se napagjaat

def findSolution(knight1, knight2):
    if abs(knight1[0] - knight2[0]) == 2 and abs(knight1[1] - knight2[1]) == 1:
        return False
    elif abs(knight1[0] - knight2[0]) == 1 and abs(knight1[1] - knight2[1]) == 2:
        return False
    elif knight1 == knight2:
        return False
    else:
        return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    domain = []
    variables = []
    n = int(input())
    for i in range(0, n):
        variables.append(i + 1)
        for j in range(0, n):
            domain.append((i, j))
    problem.addVariables(variables, domain)

    for k1 in variables:
        for k2 in variables:
            if k2 > k1:
                problem.addConstraint(findSolution, (k1, k2))

    print(problem.getSolution())
    # brojot na site mozni resenija
    # solutions = problem.getSolutions()
    # print(len(solutions))
