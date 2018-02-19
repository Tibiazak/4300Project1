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


def isvalid(state, startstate):
    otherside = startstate.copy()
    for i in range(0, 3):
        otherside[i] = startstate[i] - state[i]
    if (state[1] > state[0]) and state[0] != 0:
        return False
    elif state[0] > 3 or state[1] > 3 or state[2] > 1:
        return False
    elif (otherside[1] > otherside[0]) and otherside[0] != 0:
        return False
    elif otherside[0] > 3 or otherside[1] > 3 or otherside[2] > 1:
        return False
    else:
        return True


def gensuccessors(ops, state, startstate):
    successors = []
    validops = []
    for op in ops:
        new = performop(state, op)
        if isvalid(new, startstate):
            successors.append(new)
            validops.append(op)
    return successors, validops


def search(node, depth, goal, ops, startstate):
    if node == goal:
        return []
    elif depth > 0:
        transitions, valops = gensuccessors(ops, node, startstate)
        # print("Transitions: ", str(transitions), "for node: ", str(node))
        for state in transitions:
            # print("State is: ", str(state), "in transitions: ", str(transitions))
            result = search(state, depth-1, goal, ops, startstate)
            if result is not None:
                # print("Result is :", str(result), "Operation is: ", str(valops[transitions.index(state)]))
                result.append(valops[transitions.index(state)])
                return result
        return None
    else:
        return None


# Initiate variables - startstate is 3 missionaries, 3 cannibals, and a boat
# goalstate is 0 missionaries, 0 cannibals, no boat

startstate = [3, 3, 1]
goalstate = [0, 0, 0]
operations = [[0, 1, 1], [1, 0, 1], [1, 1, 1], [2, 0, 1], [0, 2, 1]]
maxdepth = 11
found = False


for i in range(0, maxdepth):
    result = search(startstate, maxdepth, goalstate, operations, startstate)
    if result is not None:
        result.reverse()
        print(result)
        found = True
        break
if not found:
    print("Goal state not found at depth ", str(maxdepth))
