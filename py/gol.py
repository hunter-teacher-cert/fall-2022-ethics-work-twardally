#gol.py
#Tanya Wardally
#CSCI 77800 Fall 2022
#collaborators:
#consulted:

import random, copy

rows = 25
cols = 25

Alive = 'X'
Dead = '-'

board = {}

for x in range (rows):
  for y in range (cols):
    if random.randint(0, 1) == 0:
      board[(x,y)] = Alive
    else:
      board[(x,y)] = Dead
    

while True:
  print('\n')
  cells = copy.deepcopy(board)


  for x in range (rows):
        for y in range (cols):    
            print(cells[(x,y)], end = " ")
  print()


for y in range (cols):
  for x in range (rows):
    left = (x-1) % rows
    right = (x+1) % rows
    above = (y-1) % cols
    below = (y+1) % cols


    numNeighbors = 0
    if cells[(left, above)] == Alive:
      numNeighbors += 1  # Top-left neighbor is alive.
    if cells[(x, above)] == Alive:
      numNeighbors += 1  # Top neighbor is alive.
    if cells[(right, above)] == Alive:
      numNeighbors += 1  # Top-right neighbor is alive.
    if cells[(left, y)] == Alive:
      numNeighbors += 1  # Left neighbor is alive.
    if cells[(right, y)] == Alive:
      numNeighbors += 1  # Right neighbor is alive.
    if cells[(left, below)] == Alive:
      numNeighbors += 1  # Bottom-left neighbor is alive.
    if cells[(x, below)] == Alive:
      numNeighbors += 1  # Bottom neighbor is alive.
    if cells[(right, below)] == Alive:
      numNeighbors += 1  # Bottom-right neighbor is alive.


    if cells[(x, y)] == Alive and (numNeighbors == 2 or numNeighbors == 3):
                   # Living cells with 2 or 3 neighbors stay alive:
      board[(x, y)] = Alive
    elif cells[(x, y)] == DEAD and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
      board[(x, y)] = Alive
    else:
                # Everything else dies or stays dead:
      board[(x, y)] = Dead
