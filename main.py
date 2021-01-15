#/usr/bin/env python3
import handleInput
from rich import print

def exit_app():
    print('Goodbye :smiley:')
    exit()

if __name__ == '__main__':
    while True:
        inp = input('sn> ')
        if inp == 'exit': exit_app()
        handleInput.handleInput(inp)
