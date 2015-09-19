__author__ = 'Hyunsoo'

import re
ValidPattern = re.compile("^[a-zA-Z_][a-zA-Z0-9_]*$")

def isValidStateName(name):
    return ValidPattern.match(name) is not None
def getStates(data):
    states = []
    for line in data[1:]:
        state = line[1]
        assert isValidStateName(state) and state not in states
        states.append(state)
    return states
def getVocabulary(data):
    vocabulary = []
    line = data[0][2:]
    for symbol in line:
        assert len(symbol) == 1 and symbol not in vocabulary
        vocabulary.append(symbol)
    return vocabulary
def getInitialState(data):
    return data[1][1]
def getFinalState(data):
    finalStates = []
    for line in data[1:]:
        if len(line[0])>0:
            finalStates.append(line[1])
    return finalStates
def getTransitionTable(data):
    table = [line[1:] for line in data]
    for row in range(1, len(table)):
        for column in range(1, len(table[0])):
            string = table[row][column]
            dest = re.split('\s+', string)
            table[row][column] = dest
    return table