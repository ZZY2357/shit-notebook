# Read and execute the input.

import execute

def handleInput(inp: str):
    args = inp.split(' ')
    execute.find_and_execute_function(args)
