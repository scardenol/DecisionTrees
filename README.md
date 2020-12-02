**Names:** Danilo de Jesús Toro Echeverri, Salomón Cardeño Luján

**Context:**
The given context is to make predictions on the academic success (*éxito académico*) in
higher education (*educación superior*) using decision trees. The academic success in
this scope is defined as the probability that a student gets a total score superior to his
cohort's average, in the *Pruebas Saber Pro* test.

**Problem:**
Design an algorithm based on decision trees and the *Saber 11* data to predict whether a
student will have a total score, in the *Pruebas Saber Pro*, above average or not.

**About the data:**
The datasets in https://github.com/mauriciotoro/ST0245-Eafit/tree/master/proyecto/datasets
were the ones assigned to the project, where the training and test data are available as
different ```.csv``` files.

**General description:** 
The program takes a ```.csv``` file of training data, builds a decision tree based
on the CART algorithm and classifies a ```.csv``` file of testing data, making predictions
for the column with label *exito* (success).
language of a Pushdown Automaton. In order to do so, it utilizes various functions
in a certain processing order that can be easily understood via the following image.

<img src="https://imgur.com/a/5iLcF5m"/>
![Imgur](https://imgur.com/a/5iLcF5m)

The functions stated as "Functions" are simply the "main" functions whereas the functions
stated as "Auxiliary functions" serve a particular purpose required by a main function
that calls it. Generally speaking, each function's role is as follows:

```simPDA``` is the one function that tests the belonging of the word by returning
a boolean, True for belonging or False for not belonging. But in order to do so,
it proccesses the word ```processWord``` and also initializes the stack ```iniStack```
with the z0 symbol of the automaton being evaluated.

```processWord``` performs the transition from a current state to the next one, updates 
the stack and returns True or False if the word belongs to the automaton. If the current state
is Nothing it means the automaton has reached a dead state and the word does not belong.
It implements ```isAccepting```, ```getNextState``` and ```processInput``` for this task.

```processInput``` removes the last symbol of the stack and then pushes
each symbol that is in the list obtained from the automaton (in reverse order). It uses
```getStackReplace``` and ```pushList``` for this task.

```getNextState``` obtains the next state from the transition function of the automaton
given the current state, the input symbol and the stack. It implements ```nextStateAux```
in order to do so.

```nextStateAux``` obtains the next state from the transition function of the automaton.
given the current state, the input symbol and the last symbol of the stack.

```getStackReplace``` obtains the list of symbols that will replace the 
last symbol of the stack.

```getTransitionPair``` Obtains the ordered pair of state and list of stack symbols.

```pushList``` pushes each symbol of a given list into a given stack.

```lookupKey``` returns the first element of a given set or returns Nothing if no set is given.

```isAccepting``` returns boolean values, i.e, True or False whether or not the state evaluated is the
accepting state.

```iniStack``` returns a stack with the initial z0 symbol of the given automaton.

**How to use program:**
To use, input the following:

**1.** The ```simPDA``` function

**2.** followed by a function that has as input parameters the PDA set, i.e.,
the set that represents a Pushdown Automata:
```
data PushDownAutomata state symbol symbolp = PDA
  {states, alphabet, stackalphabet, delta, initialState, z0, acceptState}
```
which can be either one of the 3 given functions that represent automatas
```pda0```, ```pda1``` or ```pda2```, or by manual input of such set.

**3.** and lastly, followed by a string of symbols or a word either written
as a explicit set or by using Syntatic sugar.

**e.g.** to test if the word [0,1,1,0] belongs to the language of the automaton
described by ```pda0``` the input would be

```simPDA pda0 [0,1,1,0]```

**Operating system version:** Microsoft Windows 10 Home Single Language

**GHC version:** 8.8.3

HLint v2.2.11, (C) Neil Mitchell 2006-2020
