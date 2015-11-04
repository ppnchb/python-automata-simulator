__author__ = 'Hyunsoo'

from automata.reader import *


class SVFunction:
    def __init__(self, data=None):
        self.states = []
        self.vocabulary = []
        self.table = []
        if data is not None:
            self.initialize(data)

    def __call__(self, state, symbol):
        assert symbol in self.vocabulary
        assert state in self.states
        row = self.states.index(state)+1
        column = self.vocabulary.index(symbol)+1
        return self.table[row][column]

    def initialize(self, data):
        states = getStates(data)
        vocabulary = getVocabulary(data)
        table = getTable(data)
        self.states = states
        self.vocabulary = vocabulary
        self.table = table


class Transition(SVFunction):
    def initialize(self, data):
        super().initialize(data)
        for row in range(1, len(self.table)):
            for column in range(1, len(self.table[0])):
                item = self.table[row][column]
                self.table[row][column] = [state for state in re.split('\s+', item) if state!='']
        assert self.isValidTransition(self.states, self.table)


    def isValidTransition(self, states, table):
        for line in table[1:]:
            for dest in line[1:]:
                for state in dest:
                    if state not in states:
                        return False
        return True

    def epsilonClosure(self, state):
        assert state in self.states
        if '' not in self.vocabulary:
            return [state]
        result = []
        iteration = [state]
        while result != iteration:
            result = iteration[:]
            for element in result:
                temp = [s for s in self.__call__(element, '') if s not in iteration]
                iteration.extend(temp)
        return result
