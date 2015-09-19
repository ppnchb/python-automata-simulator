# -*- coding: utf-8 -*-

__author__ = 'Hyunsoo'

from automata.automata import NFA

if __name__ == "__main__":
    nfa = NFA('automata.csv')
    string = input(">> ")
    accepted = nfa.match(string)
    if accepted:
        print("네")
    else:
        print("아니요")