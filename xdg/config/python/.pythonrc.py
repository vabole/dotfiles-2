# Add auto-completion and a stored history file of commands to your Python
# interactive interpreter. Requires Python 2.0+, readline. Autocomplete is
# bound to the Esc key by default (you can change it - see readline docs).
#

import atexit
import os
import readline
import rlcompleter

dir = os.path.dirname(__file__)
historyPath = os.path.join(dir, '.python_history')

def save_history(historyPath=historyPath):
    import readline
    readline.write_history_file(historyPath)

if os.path.exists(historyPath):
    readline.read_history_file(historyPath)
atexit.register(save_history)
del os, atexit, readline, rlcompleter, save_history, historyPath

#import sympy
#x, y, z, t = symbols('x y z t')
#k, m, n = symbols('k m n', integer=True)
#f, g, h = symbols('f g h', cls=Function)
#init_printing() # doctest: +SKIP