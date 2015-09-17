__author__ = 'Hyunsoo'

from automata.reader import *
from automata.transition import Transition

class DFA():
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
        currentState = self.initialState
        for symbol in string:
            if symbol not in self.vocabulary:
                return False
            currentState = self.transition(currentState, symbol)
        return currentState in self.finalState