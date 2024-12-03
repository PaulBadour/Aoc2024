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


def getints(s):
    return list(map(int, re.findall(r'\d+', s)))