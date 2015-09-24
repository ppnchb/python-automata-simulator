# -*- coding: utf-8 -*-

__author__ = 'Hyunsoo'

from automata.automata import MealyMachine

if __name__ == "__main__":
    machine = MealyMachine('mealy.csv')
    string = input(">> ")
    output = machine(string)
    print(output)