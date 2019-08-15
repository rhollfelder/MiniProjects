#!/usr/bin/env python3
import random


user = input('Choose rock, paper, or scissors:')
choices = ['rock','paper','scissor']
number = random.randint(0,2)
computer = choices[number]


if computer == 'rock' and user == 'paper': 
  print('You win!, computer chose',computer) 
elif computer == 'paper' and user == 'scissor': 
  print('You win!, computer chose',computer) 
elif computer == 'scissor' and user == 'rock': 
  print('You win!, computer chose',computer) 
elif user == 'rock' and computer == 'paper': 
  print('computer wins!, computer chose',computer) 
elif user == 'paper' and computer == 'scissor': 
  print('computer wins!, computer chose',computer) 
elif user == 'scissor' and computer == 'rock': 
  print('computer wins!, computer chose',computer) 
else:
  print('tie game!')
