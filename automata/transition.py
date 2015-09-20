__author__ = 'Hyunsoo'

from automata.reader import *

class Transition():
    def __init__(self, data=None):
        self.states = []
        self.vocabulary = []
        self.table = None
        if data is not None:
            self.initialize(data)

    def __call__(self, states, string):
        for symbol in string:
            assert symbol in self.vocabulary
        for state in states:
            assert state in self.states
        return self.callRoutine(states, string)

    def callRoutine(self, states, string):
        currentState = states[:]
        inputString = string
        while len(inputString)>0:
            symbol, inputString = inputString[0], inputString[1:]
            currentState = self.symbolTransition(currentState, symbol)
        return currentState

    def symbolTransition(self, states, symbol):
        result = []
        for state in states:
            row = self.states.index(state) + 1
            column = self.vocabulary.index(symbol) + 1
            nextStates = [item for item in self.table[row][column] if item not in result]
            result.extend(nextStates)
        return result

    def initialize(self, data):
        states = getStates(data)
        vocabulary = getVocabulary(data)
        table = getTransitionTable(data)
        assert self.isValidTransition(states, table)
        self.states = states
        self.vocabulary = vocabulary
        self.table = table

    def isValidTransition(self, states, table):
        for line in table[1:]:
            for dest in line[1:]:
                for state in dest:
                    if state not in states:
                        return False
        return True