"""
Advent of Code - Day 10
"""
data = input_getter(day=10).strip().split('\n')

# Initial start for the cycle counter
cycle = 0
# Initial start of the register that's written to
cpu_reg = 1
# Counter for the signal sum
sum_signal = 0
# Cycle numbers at which signal strenght should be checked
target_cycles = [20, 60, 100, 140, 180, 220]

# Index to which the display is writing
crt_pos = 0
# List to hold the lines of display output
crt_out = [] #['','','','','',''] #??
# Setting for display width
display_width = 40

def run_cycle():
  global cycle
  draw_screen()
  # Update the cycle
  cycle += 1
  check_signal(cycle)

def check_signal(cycle):
  global sum_signal
  # Check if we need to record signal strenght
  if cycle in target_cycles:
    sum_signal += cycle * cpu_reg

def draw_screen():
  global crt_out, crt_pos
  # Every x rows, start a new line to display. Add tho the list if needed
  crt_row = cycle // display_width
  if len(crt_out) < crt_row + 1:
    crt_out.append('')

  # If the display row is full, reset the position counter
  if cycle % display_width == 0:
    crt_pos = 0
  else:
    crt_pos += 1
  
  # If the current position of the crt writer is within 1 of cpu register, 
  # enable the pixel at that position
  if cpu_reg -1 <= crt_pos <= cpu_reg + 1:
    crt_out[crt_row] += '@' # Use @ instead of # for readability
  else:
    crt_out[crt_row] += ' ' # Use ' ' instead of . for readability
  

# Run the instructions. 
# For a 'noop' instruction, just cycle up
# For an 'addx' instruction, cycle up twice, then add the value to the register
for line in data:
  instruction = line.split(' ')
  if instruction[0] == 'noop':
    run_cycle()
  elif instruction[0] == 'addx':
    run_cycle()
    run_cycle()
    cpu_reg += int(instruction[-1])

print(f'Signal strength is: {sum_signal}')
print(f'Display output is:')
for display_row in crt_out:
  print(display_row)
