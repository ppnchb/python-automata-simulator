__author__ = 'Hyunsoo'

from automata.reader import *
from automata.transition import *

class NFA:
    def __init__(self, file=""):
        self.states = []
        self.finalState = []
        self.initialState = None
        self.currentState = []
        self.vocabulary = []
        self.transition = Transition()
        if len(file)>0:
            self.setParameterFromFile(file)
            self.initialize()

    def setParameterFromFile(self, path):
        file = open(path, 'r')
        data = [line.split(',') for line in file.read().split('\n')[:-1]]
        self.setParameter(data)

    def setParameter(self, data):
        self.states = getStates(data)
        self.vocabulary = getVocabulary(data)
        self.transition = Transition(data)
        self.initialState = getInitialState(data)
        self.finalState = getFinalState(data)

    def initialize(self):
        self.currentState = self.transition.epsilonClosure(self.initialState)

    def __call__(self, symbol):
        assert type(symbol) is str and len(symbol)==1
        nextState = []
        for state in self.currentState:
            temp = [s for s in self.transition(state, symbol) if s not in nextState]
            nextState.extend(temp)
        for state in nextState:
            temp = [s for s in self.transition.epsilonClosure(state) if s not in nextState]
            nextState.extend(temp)
        self.currentState = nextState

    def isAccepted(self):
        for state in self.currentState:
            if state in self.finalState:
                return True
        return False

    def saveConfiguration(self, path):
        filepath = path + ('.csv' if path[-4:] != '.csv' else '')
        file = open(filepath, 'w')
        file.write(',,'+','.join(self.vocabulary)+'\n')
        for row in self.transition.table[1:]:
            modifiedRow = [item if type(item) is str else ' '.join(item) for item in row]
            finalStateNotation = '*,' if modifiedRow[0] in self.finalState else ','
            file.write(finalStateNotation+','.join(modifiedRow)+'\n')
        file.close()

class MealyMachine:
    def __init__(self, file=""):
        self.states = []
        self.initialState = None
        self.currentState = None
        self.inputVocabulary = []
        self.transition = Transition()
        self.outputFunction = Transition()
        if len(file)>0:
            self.setParameter(file)
            self.initialize()

    def initialize(self):
        self.currentState = self.initialState

    def __call__(self, symbol):
        assert symbol in self.inputVocabulary
        output = self.outputFunction(self.currentState, symbol)
        self.currentState = self.transition(self.currentState, symbol)[0]
        return output

    def setParameter(self, path):
        file = open(path, 'r')
        data = [line.split(',') for line in file.read().split('\n')[:-1]]

        self.states = getStates(data)
        self.initialState = getInitialState(data)
        self.inputVocabulary = getVocabulary(data)
        self.transition = Transition(getPartialData(data, 1))
        self.outputFunction = SVFunction(getPartialData(data, 0))