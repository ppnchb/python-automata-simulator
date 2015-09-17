__author__ = 'Hyunsoo'

from automata.reader import *

class Transition():
    def __init__(self, data=None):
        self.states = []
        self.vocabulary = []
        self.table = None
        if data is not None:
            self.initialize(data)

    def __call__(self, state, symbol):
        assert state in self.states and symbol in self.vocabulary
        row = self.states.index(state) + 1
        column = self.vocabulary.index(symbol) + 1
        output = self.table[row][column]
        if output == '':
            return None
        return self.table[row][column]

    def initialize(self, data):
        states = getStates(data)
        vocabulary = getVocabulary(data)
        table = [line[1:] for line in data]
        assert self.isValidTransition(states, table)
        self.states = states
        self.vocabulary = vocabulary
        self.table = table

    def isValidTransition(self, states, table):
        for line in table[1:]:
            for state in line[1:]:
                if not(state == '' or state in states):
                    return False
        return True