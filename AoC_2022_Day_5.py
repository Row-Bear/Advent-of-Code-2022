"""
Advent of Code - Day 5
"""
data = input_getter(day=5)

# Read the input. Split to separete the stack layout from the instructions
data = data.split('\n\n')
 
# Prepare a dictionary that will hold the stacked crates
cargo = {}
stacks = data[0].split('\n')

# Read the last line of the layout to get stack labels
for label in stacks[-1].replace(' ',''):
    cargo[label] = []

# Fill the stacks with the starting data
for line in stacks[:-1]:
    n = 1
    for i in range(1, len(line), 4):
        if line[i] != ' ': # Skip empty places
            cargo[str(n)].insert(0, line[int(i)])
        n += 1

# Execute the instructions based on the place in the line
for instr in data[1].strip('\n').split('\n'):
    amt = int(instr.split(' ')[1])
    src = str(instr.split(' ')[3])
    des = str(instr.split(' ')[5])
    for i in range(amt):
        cargo[des].append(cargo[src][-1])
        del cargo[src][-1]

result = ''    
for stack in cargo:
    result += (f'{cargo[stack][-1]}')

print(f'The answer for part 1 is: {result}')

for stack in stacks[-1].replace(' ',''):
    cargo[stack] = []


for line in stacks[:-1]:
    #print(line)
    n = 1
    for i in range(1, len(line), 4):
        #print(n, line[int(i)])
        if line[i] != ' ':
            cargo[str(n)].insert(0, line[int(i)])
        n += 1
        
for instr in data[1].strip('\n').split('\n'):
    # print(instr.split(' '))
    amt = int(instr.split(' ')[1])
    src = str(instr.split(' ')[3])
    des = str(instr.split(' ')[5])
    # print(hold[src], '->', hold[des])
    cargo[des] += (cargo[src][-amt:])
    del cargo[src][-amt:]
 
result = ''   

for stack in cargo:
    result += (f'{cargo[stack][-1]}')

print(f'The answer for part 2 is: {result}')
