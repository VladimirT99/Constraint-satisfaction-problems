from constraint import *


#     SEND
#   + MORE
#   ------
#    MONEY

def findSolution(S, E, N, D, M, O, R, Y):
    a = 1000 * S + 100 * E + 10 * N + D
    b = 1000 * M + 100 * O + 10 * R + E
    c = 10000 * M + 1000 * O + 100 * N + 10 * E + Y
    return a + b == c


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    domain = []
    for i in range(0, 9):
        domain.append(i)
    variables = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
    problem.addVariables(variables, domain)
    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(findSolution, variables)
    print(problem.getSolution())
