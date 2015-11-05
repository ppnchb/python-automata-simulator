__author__ = 'Hyunsoo'

import re

def getStates(data):
    states = []
    for line in data[1:]:
        state = line[1]
        assert state not in states
        states.append(state)
    return states
def getVocabulary(data):
    vocabulary = []
    line = data[0][2:]
    for symbol in line:
        assert len(symbol) <= 1 and symbol not in vocabulary
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
def getTable(data):
    table = [line[1:] for line in data]
    return table
def getPartialData(data, index):
    height, width = len(data), len(data[0])
    result = [row[:] for row in data]
    for row in range(1, height):
        for column in range(2, width):
            tableData = re.split(';\s+', result[row][column])
            assert len(tableData)>index
            result[row][column]=tableData[index]
    return result