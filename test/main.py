# -*- coding: utf-8 -*-

__author__ = 'Hyunsoo'

from automata.automata import MealyMachine

if __name__ == "__main__":
    machine = MealyMachine('mealy.csv')
    output = []
    symbol = input(">> ")
    while symbol is not "":
        outputSymbol = machine(symbol)
        output.append(outputSymbol)
        print(outputSymbol)
        symbol = input(">> ")
    print(output)
