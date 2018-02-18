# status = [3, 3, 1]
# operation = [0, 1, 1]
# newstat = status
# for i in range(0, 3):
#     newstat[i] = newstat[i] - operation[i]
# print(newstat)
# operations = [[0, 1, 1], [1, 0, 1], [1, 1, 1], [2, 0, 1], [0, 2, 1]]


def performop(state, op):
    newstate = list.copy(state)
    for i in range(0, 3):
        if state[2] == 1:
            newstate[i] = newstate[i] - op[i]
        else:
            newstate[i] = newstate[i] + op[i]
    return newstate


def isvalid(state):
    if state[1] > state[0]:
        return False
    else:
        return True


def gensuccessors(ops, state):
    successors = []
    validops = []
    for op in ops:
        new = performop(state, op)
        if isvalid(new):
            successors.append(new)
            validops.append(op)
    return successors, validops


startstate = [3, 3, 1]
goalstate = [0, 0, 0]
operations = [[0, 1, 1], [1, 0, 1], [1, 1, 1], [2, 0, 1], [0, 2, 1]]

frontier, validops = gensuccessors(operations, startstate)
print(frontier)
print(validops)
for state in frontier:
    if state == goalstate:
        print("Found solution with operation: ")
        print(validops[frontier.index(state)])
        break
    else:
        print("No solution found.")

