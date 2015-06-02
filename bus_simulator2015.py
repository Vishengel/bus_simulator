#!/usr/bin/python

from manual import Manual
from simulation import Simulation

continueWhenDeckIsEmpty = True

print "****************************************************"
print "*",
print "                                                ",
print "*"
print "*",
print "Welcome to Bus Simulator 2015: Electric Boogaloo",
print "*"
print "*",
print "                                                ",
print "*"
print "****************************************************"

mode = raw_input("Would you like to play a round yourself (m) or let the computer run a set number of rounds (a)? ")
print ""

if mode == 'm':
  numberOfCards = 0
  while numberOfCards != 7 and numberOfCards != 9:
    numberOfCards = input("7 or 9? ")
    if numberOfCards != 7 and numberOfCards != 9:
      print("Holy fucking smoke, read the question dipshit...")

  man = Manual(numberOfCards, continueWhenDeckIsEmpty)
  man.run()

if mode == 'a':
  totalIterations = input("Enter total number of rounds: ")
  print ""
  print "Running simulation for 7 cards and %d iterations..." % totalIterations
  sim = Simulation(7, continueWhenDeckIsEmpty, totalIterations)
  sim.run()

  print ""
  print "Running simulation for 9 cards and %d iterations..." % totalIterations
  sim = Simulation(9, continueWhenDeckIsEmpty, totalIterations)
  sim.run()
