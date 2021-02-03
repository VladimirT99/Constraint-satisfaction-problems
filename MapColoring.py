from constraint import *

# MapColoring so 3 boi, so ogranicuvanje deka 2 sosedni drzavi ne mozat da imaat ista boja

if __name__ == '__main__':
    problem = Problem(MinConflictsSolver())
    problem.addVariables(['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T'], ['red', 'green', 'blue'])

    problem.addConstraint(lambda a, b: a != b, ('WA', 'NT'))
    problem.addConstraint(lambda a, b: a != b, ('WA', 'SA'))
    problem.addConstraint(lambda a, b: a != b, ('NT', 'Q'))
    problem.addConstraint(lambda a, b: a != b, ('SA', 'Q'))
    problem.addConstraint(lambda a, b: a != b, ('SA', 'NSW'))
    problem.addConstraint(lambda a, b: a != b, ('SA', 'V'))
    problem.addConstraint(lambda a, b: a != b, ('NSW', 'V'))
    solution = problem.getSolution()
    print(solution)
