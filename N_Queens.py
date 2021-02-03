from constraint import *

# Postavuvanje N kralici na tabla NxN bez da se napagjaat

def findSolution(q1, q2):
    if abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return False
    if q1[0] == q2[0] or q1[1] == q2[1]:
        return False
    return True

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    N = int(input())
    kralici = []
    domain = []
    for i in range(0,N):
        kralici.append(i)
        for j in range(0, N):
            domain.append((i,j))

    problem.addVariables(kralici,domain)

    for q1 in kralici:
        for q2 in kralici:
            if q1 != q2:
                problem.addConstraint(findSolution, (q1, q2))

    solution = problem.getSolution()
    print(solution)

