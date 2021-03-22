#!/usr/bin/env python3

from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.validation import Validator,ValidationError
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
import json
import random

GREEN = '\033[92m'             
RED = '\033[91m'            
BLUE = '\033[94m'           
ENDC = '\033[0m'            
BOLD = '\033[1m'            

style = Style.from_dict({
    '':          'bold',  # User input (default text).
    'attck': '#ff0066',
    'gt':       '#44ff00 bold',
    'section':  '#00ffff',
})

message = [
    ('class:attck', 'ATT&CK'),
    ('class:gt',       ' > '),
]

techinques_data = json.load(open('data/attck_techniques.json'))
techinques = list(techinques_data.keys()) + ['quit'] #exit quick from section mode
techinques_suggester = FuzzyWordCompleter(techinques)

options = ['random_mode', 'search_mode']
options_suggester = FuzzyWordCompleter(options)

def print_title(title, info, end=None):
    print(f'{BOLD}{GREEN}{title}{ENDC}{info}', end=end)

class Selection_Validator(Validator):
    def __init__(self, options):
        self.options = options

    def validate(self, document):
        text = document.text
        if text not in set(self.options):
            raise ValidationError(message='Not a valid selection!')

def attck_prompt():
    #session = PromptSession() ==> from prompt_toolkit import PromptSession
    while True:
        try:
            selected_mode = prompt(message,completer=options_suggester, style=style, validator=Selection_Validator(options))
            message_section = [
                ('class:attck', 'ATT&CK'),
                ('class:section',   f' [{selected_mode}]'),
                ('class:gt',    ' > '),
            ]
        except KeyboardInterrupt:
            break

        while True:
            try:
                if selected_mode == 'search_mode':
                    selection = prompt(message_section, completer=techinques_suggester, style=style, validator=Selection_Validator(techinques))
                    if selection == 'quit':
                        exit()
                    else:
                        selected_technique_data = techinques_data[selection]
                        print_title('\nTechnique: ', selection, end='\n')
                        print_title('\nID: ', selected_technique_data[0], end='\n')
                        print_title('\nDescription:\n', selected_technique_data[1], end='\n\n')
                else:
                    selection = prompt(message_section, style=style)
                    if selection == 'quit':
                        print('Bye')
                        exit()
                    else:
                        random_selection = random.choice(techinques)
                        selected_technique_data = techinques_data[random_selection]
                        print_title('\nTechnique: ', random_selection, end='\n')
                        print_title('\nID: ', selected_technique_data[0], end='\n')
                        print_title('\nDescription:\n', selected_technique_data[1], end='\n\n')
            except KeyboardInterrupt:
                print(f'{BLUE}{BOLD}[!]{ENDC} {BOLD}Exiting {selected_mode}', end='\n\n')
                break

    print('Bye')

if __name__ == '__main__':
    attck_prompt()