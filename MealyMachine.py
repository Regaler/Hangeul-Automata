"""
2016-09-23
(c) 20120410 Minuk Ma, KAIST, akalsdnr@kaist.ac.kr
DFA.py
1. class MealyMachine: __init__, transit(), get_current(), print_state(), initialize()
2. def makeMealyMachine
3. def isSentence
"""

class MealyMachine:
    """MealyMachine Class. """
    
    def __init__(self, states=[], in_symbols=[], transition=[], out_symbols=[], out_func=[],initial=[]):
        """DFA is defined by 5 parameters."""
        # Type Check
        if not isinstance(states, (list)):
            raise TypeError('states must be a list')
        if not isinstance(in_symbols, (list)):
            raise TypeError('in_symbols must be a list')
        if not isinstance(transition, (list)):
            raise TypeError('transition must be a list')
        if not isinstance(out_symbols, (list)):
            raise TypeError('out_symbols must be a list')
        if not isinstance(out_func, (list)):
            raise TypeError('out_func must be a list')
        if not isinstance(initial, (list)):
            raise TypeError('initial must be a list')
        
        self._states = states
        self._in_symbols = in_symbols
        self._transition = transition
        self._out_symbols = out_symbols
        self._out_func = out_func
        self._initial = initial      
        self._current = states[0]
        self._alive = True

    def transit(self, symbol):
        """Read a symbol, scan transition function, and set the current state
            as the next state. If Mealy machine can't read the symbol, it's dead.
        """
        if self._alive:
            for elem in self._transition:
                if (elem[0]==self._current) and (elem[1]==symbol):
                    self._current = elem[2]
                    for comp in self._out_func:
                        if (comp[0]==elem[0]) and (comp[1]==elem[1]):
                            return comp[2]
            self._alive = False

    def get_current(self):
        """Return the current state"""
        return self._current

    def get_alive(self):
        """Return if it's dead or not"""
        return self._alive
    
    def print_state(self):
        """Print the current state"""
        print(self._current),
    
    def initialize(self):
        """Initialize DFA for further using"""
        self._current = self._initial[0]
        self._alive = True


def makeMealyMachine(Mealy_info):
    """Read a formatted text file, and make a MealyMachine object with that."""
    lines = Mealy_info.readlines()
    lines = map(lambda s: s.strip(), lines)
    #print lines
    
    for i in range(len(lines)):
        if lines[i] == 'State': state_index = i+1
        elif lines[i] == 'Input symbol': in_symbol_index = i+1
        elif lines[i] == 'State transition function': trans_index = i+1
        elif lines[i] == 'Output symbol': out_symbol_index = i+1
        elif lines[i] == 'Output function': out_func_index = i+1
        elif lines[i] == 'Initial state': initial_index = i+1
    
    states = lines[state_index].split(",")
    in_symbols = lines[in_symbol_index].split(",")
    transition = []
    for j in range(out_symbol_index - trans_index - 1):
        elem = lines[trans_index + j].split(",")
        elem[-1].strip()
        transition.append(elem)
    #print "transition: ", transition
    out_symbols = lines[out_symbol_index].split(",")
    out_func = []
    for j in range(initial_index - out_func_index - 1):
        elem = lines[out_func_index + j].split(",")
        elem[-1].strip()
        out_func.append(elem)
    initial = lines[initial_index].split(",")
    
    mealy = MealyMachine(states, in_symbols, transition, out_symbols, out_func, initial)
    
    return mealy


def isSentence(MM, string):
    """Let MM read a string. If MM can read that to the end, return True."""
    read = 0
    #MM.print_state()
    output = ''
    for i in range(len(string)):
        if MM.get_alive()==True:
            s = MM.transit(string[i])
            #MM.print_state()
            read = read + 1
            output = output + str(s)
    #print "\nstring len: ", len(string), "#of read: ", read
    #print "------------------------------------------------------"
    if (read == len(string)):
        return True, output
    else:
        return False, output
    
