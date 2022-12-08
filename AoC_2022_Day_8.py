"""
Advent of Code - Day 8
"""
data = input_getter(day=8).strip().split('\n')

class ElfTree():
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.visible = False
    self.vis_from_left = False
    self.vis_from_right = False
    self.vis_from_top = False
    self.vis_from_bottom = False
    self.view_to_left = 0
    self.view_to_right = 0
    self.view_to_top = 0
    self.view_to_bottom = 0
    self.scenic_score = 0

  def __str__(self):
    return f'Tree at x={self.x}, y={self.y}, z={self.z}, visible={self.visible}'
  
  def calc_scenic_score(self):
    self.scenic_score = self.view_to_left * self.view_to_right * self.view_to_top * self.view_to_bottom

"""
list_getter takes and input array and two integer values (coordinate).
It returns two lists, one for all values on the x-axis for the given coordinate.
The other for all values on the y-axis for the given coordinate.
"""
def list_getter(input_array, x,y):
  x_list = list(map(int,input_array[y]))
  y_list = []
  for line in input_array:
    y_list.append(int(line[x]))
  return x_list, y_list

"""
view_finder takes a list of integers, and a height as integer
It will return how many positions in the list can be 'seen' from outside of 
the list. 
Will process the list left to right, as if the viewer is to the left of the list
Returned value includes the final element and is 1-based
"""
def view_finder(trees:list, height:int):
  if not trees:
    # Empty list means the tree is at an edge, 0 points
    return 0
  elif max(trees) < height:
    # Can see al the way to the end!
    return len(trees)
  else:
    # Count how far we can see
    for idx, tree in enumerate(trees, start=1):
      if tree >= height:
        return idx
  pass

 
tree_list =[]
grid_size = len(data[0])
debug_print = False
if debug_print: grid_size = 10
 

for x in range(grid_size):
  for y in range(grid_size):
    x_list, y_list = list_getter(data, x, y)
    
    z = y_list[y]
    new_tree = ElfTree(x=x, y=y, z=z)
    
    
    x_left = x_list[:x]
    x_right = x_list[x+1:]
    y_left = y_list[:y]
    y_right = y_list[y+1:]

    if debug_print:
    # Debugging
      print('x')
      print(x_list)
      print(x,y,z)
      print(x_left, x_right)
      print('y')
      print(y_list)
      print(x,y,z)
      print(y_left, y_right)

    # Check if tree is visible from the left
    if x_left and z > max(x_left) or x == 0:
      new_tree.visible = True
      new_tree.vis_from_left = True
      if debug_print: print(f'{new_tree} is visible from left')

    # Log the view from the tree to the left
    new_tree.view_to_left = view_finder(x_left[::-1], z)
    if debug_print: print(f'View from tree to the left: {new_tree.view_to_left}')

    # Check if tree is visible from the right
    if x_right and z > max(x_right) or x == grid_size-1:
      new_tree.visible = True
      new_tree.vis_from_right = True
      if debug_print: print(f'{new_tree} is visible from right')

    # Log the view from the tree to the right
    new_tree.view_to_right = view_finder(x_right, z)
    if debug_print: print(f'View from tree to the right: {new_tree.view_to_right}')

    # Check if tree is visible from the top
    if y_left and z > max(y_left) or y == 0:
      new_tree.visible = True
      new_tree.vis_from_top = True
      if debug_print: print(f'{new_tree} is visible from top')
    
    # Log the view from the tree to the top  
    new_tree.view_to_top = view_finder(y_left[::-1], z)
    if debug_print: print(f'View from tree to the top: {new_tree.view_to_top}')

    # Check if tree is visible from the bottom
    if y_right and z > max(y_right) or y == grid_size-1:
      new_tree.visible = True
      new_tree.vis_from_bottom = True
      if debug_print: print(f'{new_tree} is visible from bottom')

    # Log the view from the tree to the right
    new_tree.view_to_bottom = view_finder(y_right, z)
    if debug_print: print(f'View from tree to the bottom: {new_tree.view_to_bottom}')
    
    # Debugging - newlines for output separation
    if debug_print:
      print()
      print()
    # Calculate the scenic score of the tree
    new_tree.calc_scenic_score()

    # Store the tree in a list
    tree_list.append(new_tree)

print('Total number of trees visible from outside', sum(1 for i in tree_list if i.visible))

if debug_print:
  print('Visible from top ',sum(1 for i in tree_list if i.vis_from_top))
  print('Visible from left',sum(1 for i in tree_list if i.vis_from_left))
  print('Visible from right ',sum(1 for i in tree_list if i.vis_from_right))
  print('Visible from bottom ',sum(1 for i in tree_list if i.vis_from_bottom))

print('The highest scenic score is:', max(tree.scenic_score for tree in tree_list))
# Part 1 answer: 1776
# Part 2 answer: 234416
