__author__ = 'Hyunsoo'

from automata.reader import *
from automata.transition import Transition

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