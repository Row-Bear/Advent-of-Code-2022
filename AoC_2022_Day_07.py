"""
Advent of Code - Day 7
"""
data = input_getter(day=7)

# Initialise the dir list with info for root, to set up data structure.
dirs =  [['$/', [], 0, 0]]
dir_idx = ['$/']

current_dir = ['$/']
current_dir_str = '$/'

# Group the input by commands + result
for chunk in data.strip().split('\n$ ')[1:]:

  if chunk[:2] == 'cd': # Navigating
    if chunk.split(' ')[-1] == '/': # Back to root
      current_dir_str = '$/'
    elif chunk.split(' ')[-1] == '..':
      # Going up a dir. Retrieve parent dir from current dir
      parent_dir = current_dir_str[:-len(current_dir_str.split('/')[-2])-1]

      # Get the weight of the current dir, and use it to set the parent dir weight
      current_dir_file_weight = dirs[dir_idx.index(current_dir_str)][2]
      current_dir_weight = dirs[dir_idx.index(current_dir_str)][3]

      dirs[dir_idx.index(parent_dir)][3] += current_dir_file_weight
      dirs[dir_idx.index(parent_dir)][3] += current_dir_weight

      # Update current dir to the parent dir
      current_dir_str = parent_dir
    else:
      current_dir_str += chunk.split(' ')[-1] + '/'

  elif chunk[:2] == 'ls': # Listing file output
    for n in chunk.split('\n')[1:]:
    # result is dir 
      if n.split(' ')[0] == 'dir':
        dir_name = current_dir_str + n.split(' ')[1] + '/'
        # Add new found dirs to list
        if not dir_name in dir_idx:
          dir_idx.append(dir_name)
          dirs.append([dir_name, [], 0, 0])

    # result is file 
      else:
        file_name = n.split(' ')[1]
        file_size = int(n.split(' ')[0])
        # Add file
        dirs[dir_idx.index(current_dir_str)][1].append((file_name, file_size))
        # Add filesize
        dirs[dir_idx.index(current_dir_str)][2] += file_size 

sum_dir_size = 0
used_size = dirs[0][2] + dirs[0][3]

for dir in dirs:
  if dir[2] + dir[3] <= 100000:
    sum_dir_size += dir[3] + dir[2]

print(f'Total size of all directories smaller than 100000: {sum_dir_size}')

total_size = 70000000
required_size = 30000000
free_size = total_size - used_size
dir_to_delete = (dirs[0][0], dirs[0][2] + dirs[0][3])

for dir in dirs:
  if dir[2] + dir[3] >= (required_size-free_size):
    if dir[2] + dir[3] < dir_to_delete[1]:
      dir_to_delete = (dir[0], dir[2] + dir[3])

print(f'Directory {dir_to_delete[0]} is the smallest that can be deleted to clear enough space.')
print(f'It will free up {dir_to_delete[1]} arbitrary size units')
