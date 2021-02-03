from constraint import *

# Posatavuvanje na N topovi na tabla NxN bez da se napagjaat

if __name__ == '__main__':
    problem = Problem(MinConflictsSolver())
    pozicija = []
    topovi = []
    N = int(input())
    for i in range(0, N):
        pozicija.append(i)
        topovi.append(i)
    problem.addVariables(topovi, pozicija)

    for t1 in topovi:
        for t2 in topovi:
            if t1 != t2:
                problem.addConstraint(lambda a, b: a != b, (t1, t2))

    print(problem.getSolution())
