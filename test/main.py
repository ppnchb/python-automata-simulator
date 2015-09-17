# -*- coding: utf-8 -*-

__author__ = 'Hyunsoo'

from automata.dfa import DFA

if __name__ == "__main__":
    dfa = DFA('automata.csv')
    string = input(">> ")
    accepted = dfa.match(string)
    if accepted:
        print("네")
    else:
        print("아니요")