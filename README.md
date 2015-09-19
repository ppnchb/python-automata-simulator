# python-automata-simulator
Automata simulator written in Python

## Features
* Read a `.csv` file to import an automaton.
* Determine whether given input is accepted.

## Supported automata types
* Nondeterministic finite automata

## How to use

### 1. Requirements
* Python 3 or later

### 2. Importing in project
To use this package, copy and paste `automata` folder in the same directory with the module that uses the package.

## Valid format of `.csv`
You must follow these rules to import an automaton by `.csv` without errors.

1. Define a set of states and an initial state.
  * Names of states are restricted exactly same as C variable names. The name must matches the regex `^[a-zA-Z_][a-zA-Z0-9_]*$`.
  * Every state must be placed at `2B, 3B, 4B, ..`.
  * Initial state must be placed at `2B`. Other than the initial state can be placed in any order.

2. Define a vocabulary.
  * Symbols must be a single letter.
  * Every symbol in the vocabulary must be placed at `1C, 1D, 1E, ..`.
  * Symbols can be placed in any order.

3. Define a set of accepting states
  * If a state is one of the accepting states, write `*` in the left cell of where the state is placed.
  * For non-accepting states, leave the left cell empty.

4. Define a transition table
  * Write next states in right column and row.
  * The cell can be empty. In these case, the transition will be a partial function.
  * Seperate states in a single cell with one single space(`' '`) if there are more than one states in a cell.

## How to test

### 1. Requirements
* Python 3 or later
* PyCharm

### 2. Steps
1. Open project from `python-automata-simulator` folder by PyCharm.
2. Run `python-automata-simulator/test/main.py`.
