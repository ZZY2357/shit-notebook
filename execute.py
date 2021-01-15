# Functions

import os
import setting
from rich import print
from rich.markdown import Markdown

functions = []

def find_and_execute_function(args):
    for func in functions:
        if func.name == args[0]:
            func.execute(args)
            return
    print('Command not found. :confused:')

class Function:
    def __init__(self, name: str, executeFunction, describtion: str, helpInfo: str):
        self.name = name
        self.describtion = describtion
        self.help = helpInfo
        self.execute = executeFunction
        functions.append(self)

def _helpFunc(args):
    if args == ['help']:
        for func in functions:
            print(':sparkles: {0.name}\t\t\t\t\t{0.describtion}'.format(func))

def _exitFunc(args):
    # This is just used to hold the place in "helps".
    pass

def _createFunc(args):
    if len(args) == 1:
        title = input('Title: ')
    else:
        title = args[1]
    directory = os.path.abspath(os.path.expanduser(setting.getValue('notebooksPath')))
    path = os.path.join(directory, f'{ title }.md')
    if not os.path.exists(directory): os.mkdir(directory)

    with open(path, 'w') as f: f.write(f'# { title }')

    print(f'The note has been created at { path }.')

def _listFunc(args):
    directory = os.path.abspath(os.path.expanduser(setting.getValue('notebooksPath')))
    for f in os.listdir(directory):
        if f.endswith('.md'):
            print(f':notebook: { "".join(f.split(".")[:-1]) }')

def _viewFunc(args):
    title = args[1]
    directory = os.path.abspath(os.path.expanduser(setting.getValue('notebooksPath')))
    path = os.path.abspath(os.path.join(directory, f'{ title }.md'))
    if not os.path.exists(path): 
        print('File not found. :confused:')
        return
    else:
        with open(path, 'r') as f:
            print(Markdown(f.read()))

help = Function('help', _helpFunc, 'Get some help.', '')
exit = Function('exit', _exitFunc, 'Exit the app.', '')
create = Function('create', _createFunc, 'Create a note.', 'create [title]')
list = Function('list', _listFunc, 'List all notes.', '')
view = Function('view', _viewFunc, 'View a note.', 'view [title]')
