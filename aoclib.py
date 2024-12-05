'''
Advent of Code automation template Original Author - @MathisHammel
https://gist.github.com/MathisHammel/43aa722469a626504de40744dfe0a3da
This template provides functions to download inputs and submit answers on AoC.

Edited slightly by me to make this into a library vs a template
Also added some helper functions for common aoc problems

'''

import requests, os, shutil, re
from dotenv import load_dotenv

dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(dir, 'cookie.env'))
AOC_COOKIE = os.getenv("AOC_COOKIE")
YEAR = '2024'

def get_input(day):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}/input', 
                       headers={'cookie':'session='+AOC_COOKIE})
    return req.text.split('\n')[:-1]

def get_example(day,offset=0):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}',
                       headers={'cookie':'session='+AOC_COOKIE})
    return req.text.split('<pre><code>')[offset+1].split('</code></pre>')[0].split('\n')[:-1]

def submit(day, level, answer):
    print(f'You are about to submit the follwing answer:')
    print(f'>>>>>>>>>>>>>>>>> {answer}')
    input('Press enter to continue or Ctrl+C to abort.')
    data = {
      'level': str(level),
      'answer': str(answer)
    }

    response = requests.post(f'https://adventofcode.com/{YEAR}/day/{day}/answer',
                             headers={'cookie':'session='+AOC_COOKIE}, data=data)
    if 'You gave an answer too recently' in response.text:
        # You will get this if you submitted a wrong answer less than 60s ago.
        print('VERDICT : TOO MANY REQUESTS')
    elif 'not the right answer' in response.text:
        if 'too low' in response.text:
            print('VERDICT : WRONG (TOO LOW)')
        elif 'too high' in response.text:
            print('VERDICT : WRONG (TOO HIGH)')
        else:
            print('VERDICT : WRONG (UNKNOWN)')
    elif 'seem to be solving the right level.' in response.text:
        # You will get this if you submit on a level you already solved.
        # Usually happens when you forget to switch from `PART = 1` to `PART = 2`
        print('VERDICT : ALREADY SOLVED')

    else:
        print('VERDICT : OK !')
        if level == 1:
            shutil.copy(f"day{day}.py", f"day{day}p1.py")
        else:
            os.rename(f"day{day}.py", f"day{day}p2.py")

# Returns a list of all ints found in a string Ex. "23 105 1 34s90" = [23, 105, 1, 34, 90]
def getints(s):
    return list(map(int, re.findall(r'\d+', s)))

# Transposes an input by switching rows and columns:  [[1,2,3], [4,5,6], [7,8,9]] = [[1,4,7], [2,5,8],[3,6,9]]
def flipinp(i):
    return ["".join([i[a][b] for a in range(len(i))]) for b in range(len(i[0]))]

# Gets a list of neighbors in a grid. Diag is if you include diagonals. If order is true, the list will contain None for every spot where there is no neighbor, ex. if a spot is in the top left corner, the first 4 items in list will be None.
def getNeighbors(grid, x, y, diag=True, order=False):
    n = [None for i in range(9)]

    if x > 0:
        n[1] = grid[x-1][y]
        if diag and y > 0:
            n[0] = grid[x-1][y-1]
        if diag and y < len(grid[0]) - 1:
            n[2] = grid[x-1][y+1]
    if x < len(grid) - 1:
        n[7] = grid[x+1][y]
        if diag and y > 0:
            n[6] = grid[x+1][y-1]
        if diag and y < len(grid[0]) - 1:
            n[8] = grid[x+1][y+1]
    if y > 0:
        n[3] = grid[x][y-1]
    if y < len(grid[0]) - 1:
        n[5] = grid[x][y+1]

    if order:
        return n
    else:
        return [i for i in n if i != None]
    
class Node:
    nodes = []
    def __init__(self, value, data=None):
        self.nexts = []
        self.value = value
        self.data = None
        Node.nodes.append(self)

    @staticmethod
    def findNode(v):
        for i in Node.nodes:
            if i.value == v:
                return i
        return None

    def addNextNode(self, n):
        if isinstance(n, Node):
            self.nexts.append(n)
        else:
            self.addNextNode(Node.findNode(n))

    def addNewNode(self, v):
        n = Node(v)
        self.nexts.append(n)
        return n

    def getNextValues(self):
        return [i.value for i in self.nexts]
    
    def dive(self, v):
        if isinstance(v, Node) and v in self.nexts:
            return True
        elif v in self.getNextValues():
            return True

        for i in self.nexts:
            if i.dive(v):
                return True
        return False