"""
Advent of Code - Day 9
"""



class RopePart(object):
  """
  RopeParts store the name, position and history for each part of a rope.
  The position history of each part is saved as a complete list, so that its
  path can be reconstructed if desired.

  Its move method take a move instruction (+1 or -1 in x and/or y direction),
  updates it's position and appends to the history.
  """

  def __init__(self, name="", starting_position=(), history=[]):
    self.name = name
    self.position = starting_position
    self.history = [starting_position]

  def __str__(self):
    return f'{self.name} is at position {self.position}'
  
  def move(self, instruction:tuple):
    self.position = (self.position[0] + instruction[0], self.position[1] + instruction[1])
    self.history.append(self.position)
  

def input_to_coordinate(instruction:str):

  """
  Takes the input instructions and parse them to a list of single 1-space moves.
  Used single step move to allow the tail of the rope to keep up with each move
  of the head.
  """
  # Expected input in from of 'U 1' 'R 2' 'D 1'. Stay in place if input differs
  if instruction[0].upper() not in 'UDRL':
    return []
  # Parse the instruction
  direction = instruction.split(' ')[0]
  amount = int(instruction.split(' ')[-1])
  
  moves = []
  for instr in range(amount):
    if direction == 'R':
      moves.append((1,0))
    elif direction == 'L':
      moves.append((-1,0))
    elif direction == 'U':
      moves.append((0,1))
    elif direction == 'D':
      moves.append((0,-1))
  return moves

def tail_move_calc(lead_pos, tail_pos):
  """
  From a given position of the head/leading node and the current node, determine
  the move needed for the tail node to move adjacent to the head node again.
  Assumes moves are made in 1 square increments
  Checks to see if a gap exists (difference of more than 1 in a coordinate), and
  check if an orthogonal move or diagonal move is needed.

  Returns a movement instruction as (x,y) tuple
  """
 
  dif_x = lead_pos[0] - tail_pos[0]
  dif_y = lead_pos[1] - tail_pos[1]

  if (abs(dif_x) > 1 and not dif_y) or (abs(dif_y) > 1 and not dif_x):
    # Orthonal moves
    if not dif_x and dif_y < 0: 
      move = (0,-1)
    elif not dif_x and dif_y > 0:
      move = (0,1)
    elif not dif_y and dif_x < 0:
      move = (-1,0)
    elif not dif_y and dif_x > 0:
      move = (1,0)
    
  elif (abs(dif_x) > 1 and dif_y) or (abs(dif_y) > 1 and dif_x):
    # Diagonal moves
    if dif_x > 0 and dif_y > 0:
      move = (1,1)
    elif dif_x > 0 and dif_y < 0:
      move = (1,-1) 
    elif dif_x < 0 and dif_y > 0:
      move = (-1,1)
    elif dif_x < 0 and dif_y < 0:
      move = (-1,-1) 
  else:
    move = (0,0)
  if move:
    return move  


# Retrieve input data for this day.
data = input_getter(day=9).strip().split('\n')

# Initialise the rope parts
head = RopePart(name='Head', starting_position=(0,0))
tail = RopePart(name='Tail', starting_position=(0,0)) 

# Read the instructions line by line.
# For each instruction, move the head one step, then move the tail to follow,
# untill the instuction is carried out.
for instruction in data:
  for i in input_to_coordinate(instruction):
    head.move(i)
    tail.move(tail_move_calc(head.position, tail.position))

# Get the unique squares visited by the tail from its history
unique_squares = set(tail.history)
print('Unique squares visited by tail: ', len(unique_squares))

## Part 2
# Delete the head and tail objects.
# It would be silly to start part 2 with the end position of the head..
del(head)
del(tail)


# In current setup, we need Head and Tail by name, so define them specifically
head = RopePart(name='head', starting_position=(0,0))
# Start a list of knots
knots = [head]
tail = RopePart(name='tail', starting_position=(0,0)) 

# Intermediate knots kan be auto-generated
for knot in range(8):
  new_knot = RopePart(name=str(knot), starting_position=(0,0))
  knots.append(new_knot)

# Add the tail to the end of the list of knots
knots.append(tail)

# As before, but use the list of knots to iterate through
for instruction in data:
  for i in input_to_coordinate(instruction):
    head.move(i)
    for idx, knot in enumerate(knots):
      if idx > 0:
        knot.move(tail_move_calc(knots[idx-1].position, knot.position))

# Get the unique squares visited by the tail from its history
unique_squares = set(tail.history)
print('Unique squares visited by tail: ', len(unique_squares))

