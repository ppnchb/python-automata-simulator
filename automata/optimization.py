__author__ = 'Hyunsoo'

from automata.automata import NFA
from automata.reader import *

def epsilonElimination(nfa):
    data = [line.split(',') for line in nfa.getConfigurationString().split('\n')[:-1]]
    for state in nfa.states:
        row = nfa.states.index(state) + 1
        eClosure = nfa.transition.epsilonClosure(state)
        for s in eClosure:
            if s in nfa.finalState:
                data[row][0] = '*'
                break

        for symbol in nfa.vocabulary:
            if symbol is '':
                continue
            nextState = []
            for state in eClosure:
                temp = [s for s in nfa.transition(state, symbol) if s not in nextState]
                nextState.extend(temp)
            column = nfa.vocabulary.index(symbol) + 2
            data[row][column] = ' '.join(nextState)

    epsilonColumn = 0
    for i in range(2, len(data[0])):
        if data[0][i] is '':
            epsilonColumn = i
            break
    if epsilonColumn == 0:
        return nfa
    for row in data:
        row.pop(epsilonColumn)

    result = NFA()
    result.setParameter(data)
    return result


def equivalentDFA(nfa):
    vocabulary = nfa.vocabulary
    states = []
    rawData = []
    queue = [[nfa.initialState]]
    while len(queue) > 0:
        state = queue.pop(0)
        states.append(state)
        transition = []
        for symbol in vocabulary:
            nextState = []
            for element in state:
                temp = [s for s in nfa.transition(element, symbol) if s not in nextState]
                nextState.extend(temp)
            if nextState not in states and nextState not in queue:
                queue.append(nextState)
            transition.append(nextState)
        isFinal = False
        for element in state:
            if element in nfa.finalState:
                isFinal = True
        rawData.append((isFinal, state, transition))
    data = [['', '']+vocabulary]
    for isFinal, state, transition in rawData:
        newStateName = 'q'+str(states.index(state))
        newTransition = ['q'+str(states.index(s)) for s in transition]
        data.append(['*' if isFinal else ''] + [newStateName] + newTransition)

    result = NFA()
    result.setParameter(data)
    return result


def minimizedDFA(dfa):
    numState = len(dfa.states)
    equivalenceTable = [[0]*numState for i in range(numState)]
    for i in range(numState):
        for j in range(i+1, numState):
            state1 = dfa.states[i]
            state2 = dfa.states[j]
            if ((state1 in dfa.finalState) != (state2 in dfa.finalState)):
                equivalenceTable[i][j] = 1
    changed = True
    while changed:
        changed = False
        for i in range(numState):
            for j in range(i+1, numState):
                state1 = dfa.states[i]
                state2 = dfa.states[j]
                for symbol in dfa.vocabulary:
                    nextState1 = dfa.transition(state1, symbol)[0]
                    nextState2 = dfa.transition(state2, symbol)[0]
                    p = dfa.states.index(nextState1)
                    q = dfa.states.index(nextState2)
                    if p>q:
                        p, q = q, p
                    if equivalenceTable[p][q] == 1 and equivalenceTable[i][j] == 0:
                        changed = True
                        equivalenceTable[i][j] = 1
    totalStates = list(range(numState))
    equivalencePartition = list(range(numState))
    while len(totalStates) > 0:
        stateIndex = totalStates.pop(0)
        equivalentStates = [stateIndex] + [i for i in range(stateIndex+1, numState) if equivalenceTable[stateIndex][i] == 0]
        for index in equivalentStates[1:]:
            totalStates.remove(index)
            equivalencePartition[index] = stateIndex

    configurationString = dfa.getConfigurationString()
    for index in range(numState):
        currentStateName = dfa.states[index]
        equivalentStateName = dfa.states[equivalencePartition[index]]
        configurationString = configurationString.replace(currentStateName, equivalentStateName)
    data = [line.split(',') for line in configurationString.split('\n')[:-1]]
    removedRow = []
    for index in range(numState):
        row = index + 1
        if index != equivalencePartition[index]:
            removedRow.append(row)
    removedRow.reverse()
    for row in removedRow:
        data.pop(row)

    result = NFA()
    result.setParameter(data)
    return result
