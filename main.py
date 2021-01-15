#/usr/bin/env python3
import handleInput
from rich import print

def exit_app():
    print('Goodbye :smiley:')
    exit()

if __name__ == '__main__':
    print(' SHIT NOTEBOOK '.center(30, '*'))
    while True:
        inp = input('shit> ')
        if inp == 'exit': exit_app()
        handleInput.handleInput(inp)
        