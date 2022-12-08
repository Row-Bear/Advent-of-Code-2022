import requests
import os

def input_getter(day):
  if day in range(1, 26): 
    if not os.path.isfile(f'AOC/aoc{day}.txt'):

      cookie = {'session': 'xx'}
      url = f'https://adventofcode.com/2022/day/{day}/input'
      print('Retrieving input from website.')
      r = requests.get(url, cookies=cookie)
      
      with open(f'AOC/aoc{day}.txt', 'w') as f:
        f.write(r.text)
      return r.text
    else:
      print('Already have the file, using local copy.')
      with open(f'AOC/aoc{day}.txt', 'r') as f:
        return f.read()
