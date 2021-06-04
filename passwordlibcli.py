"""providing a command line interface for the module in order for to be
used more easily
"""

from getpass import getpass
import sys
from passwordlib import functions


long_options = {
    '--help' : functions.helper_text,
    '--version' : functions.version,
    '--generate' : functions.generate_password,
    '--check' : functions.is_password_safe,
}

short_options = {
    '-h' : long_options['--help'],
    '-v' : long_options['--version'],
    '-g' : long_options['--generate'],
    '-c' : long_options['--check'],
                 }

messages = ('''to find out how to use this module, pass the option "-h" or 
        "--help"''',
        '''no arguments passed;''',
        '''invalid argument;''',
        )

if __name__ == '__main__':
    inputs = sys.argv
    if len(inputs) ==  1:
        print(messages[0] + '\n',  messages[0])
    elif inputs[1] in long_options.keys():
        di = long_options
    elif inputs[1] in short_options.keys():
        di = short_options  
    else:
        print(messages[2] + '\n' + messages[0])
    option = inputs[1]
    if len(inputs) == 2:
        if option == '-c' or option == '--check':
            di[option](getpass())
        else:
            di[option]()
    else:
        argument = inputs[2]
        di[option](argument)