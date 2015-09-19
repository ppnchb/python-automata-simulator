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
        if string == '':
            return states
        prevStates = self.callRoutine(states, string[:-1])
        return self.symbolTransition(prevStates, string[-1])

    def symbolTransition(self, states, symbol):
        result = []
        for state in states:
            row = self.vocabulary.index(symbol) + 1
            column = self.states.index(state) + 1
            result.extend(self.table[row][column])
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