__author__ = 'Hyunsoo'

from automata.reader import *
from automata.transition import *

class NFA():
    def __init__(self, file=""):
        self.states = []
        self.vocabulary = []
        self.transition = Transition()
        self.initialState = None
        self.finalState = []
        if len(file)>0:
            self.setParameter(file)

    def setParameter(self, path):
        file = open(path, 'r')
        data = [line.split(',') for line in file.read().split('\n')[:-1]]

        self.states = getStates(data)
        self.vocabulary = getVocabulary(data)
        self.transition = Transition(data)
        self.initialState = getInitialState(data)
        self.finalState = getFinalState(data)

    def match(self, string):
        initialStates = [self.initialState]
        finalStates = self.transition.determine(initialStates, string)
        for state in finalStates:
            if state in self.finalState:
                return True
        return False


class MealyMachine:
    def __init__(self, file=""):
        self.states = []
        self.initialState = None
        self.inputVocabulary = []
        self.transition = Transition()
        self.outputFunction = Transition()
        if len(file)>0:
            self.setParameter(file)

    def __call__(self, string):
        currentState = self.initialState
        output = []
        inputString = string[:]
        while len(inputString)>0:
            symbol, inputString = inputString[0], inputString[1:]
            nextState = self.transition(currentState, symbol)[0]
            outputSymbol = self.outputFunction(currentState, symbol)
            currentState = nextState
            output.append(outputSymbol)
        return output

    def setParameter(self, path):
        file = open(path, 'r')
        data = [line.split(',') for line in file.read().split('\n')[:-1]]

        self.states = getStates(data)
        self.initialState = getInitialState(data)
        self.inputVocabulary = getVocabulary(data)
        self.transition = Transition(getPartialData(data, 1))
        self.outputFunction = SVFunction(getPartialData(data, 0))


class InstantMealyMachine(MealyMachine):
    def __init__(self, file=""):
        super().__init__(file)
        self.currentState = self.initialState

    def __call__(self, symbol):
        assert symbol in self.inputVocabulary
        output = self.outputFunction(self.currentState, symbol)
        self.currentState = self.transition(self.currentState, symbol)
        return output