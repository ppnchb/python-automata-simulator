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
            self.setParameter(file)
            self.initialize()

    def setParameter(self, path):
        file = open(path, 'r')
        data = [line.split(',') for line in file.read().split('\n')[:-1]]

        self.states = getStates(data)
        self.vocabulary = getVocabulary(data)
        self.transition = Transition(data)
        self.initialState = getInitialState(data)
        self.finalState = getFinalState(data)

    def initialize(self):
        self.currentState = [self.initialState]

    def __call__(self, symbol):
        assert symbol is str and len(symbol)==1
        nextState = []
        for state in self.currentState:
            temp = [state for state in self.transition(state, symbol) if state not in nextState]
            nextState.extend(temp)
        self.currentState = nextState

    def isAccepted(self):
        for state in self.currentState:
            if state in self.finalState:
                return True
        return False


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