"""
Header
"""

# PyCharm keys
# F4 - jump to source
# Command + F12 => view file structure (functions)
# F1 - popup function definition
# Shift + Esc => Hide Active Tool Window ( Debugger )
# F12 ^^^^ to go back

# important modules
import dis      # disassembler of python bytecode
import sys      # functions and objects that interact closely with the interpreter
import os       # operating system interface

# extended modules
### TOD0 ####

# remove unused modules warning
sys
dis
os

"""
    Constants
"""
True
False
None
__debug__
Ellipsis

"""
    Data Structures
"""

# dictionary
d = {"first": "meh", "second": [1, 2, 3]}
d.keys()
d.values()

d["first"] = "abc"

# iterate over keys and values
for key, value in d.iteritems():
    print key, value

# strings printf syntax.
print("%s" % d["first"])

"""
    Interpreter

        sourcecode => python bytecode
"""
# the interpreter first compiles source files into python bytecode .pyc
bytecode = compile('x=2\nprint "X is", x',"fake_module", "exec")
# this is the bytecode representation
print [ord(byte) for byte in bytecode.co_code]

# show bytecode instructions
print dis.dis(bytecode)

"""
    Interpreter
        pyc ==> execute
"""

# run a piece of code
print eval(bytecode)

'''
    Virtual Machine Concepts

        + Python VM is a stack machine
        + Garbage collection is done by reference counting
        + Variables aren't really added to the stack, just a reference

        ceval.c is the main loop of the interpreter. Line ~980 contains the infinite loop for(;;) which gives us the
        REPL and Line 1112 is the giant switch statement for what to do on each opcode


        Everything in python is a PyObject. It is the main data structure for the language. All objects contain:
            -Type
            -Id
            -Value
            -Refcount
'''

'''
    Standard Library

        Quick tour =>
            https://docs.python.org/2/tutorial/stdlib.html
            https://docs.python.org/2/tutorial/stdlib2.html
'''

# without arguments, dir prints out all the variables in the current scope. This means that it will print all
# the variables and imported modules
names_in_current_scope = dir()

'''
    Functions

        + Internally the just extend PyObject
        + In essence contain a code object with the byte code and variables surrounding the "environment"
        + When you call a function, basically a new frame is created with code to execute, global + local variables
        + Function objects are created when <def> is encountered

'''

# builtins
dir(__builtins__)
len([1, 2, 3, 4])
chr(1)
eval("1+1")             # evaluates a string expression
id(5)                   # identity of an object guaranteed to be unique and constant

try:
    open("myfile")
except IOError:
    pass

range(10)
sum(range(3))
type(__builtins__)


def my_func(x):
    y = x + 1
    print y

print dir(my_func)


"""
    Functional Programming
"""


def my_upper(s):
    return s.upper()

mylist = ["maldojr88", "blahh"]

# functions are in the builtin modules
map(my_upper, mylist)
filter(lambda x: (x % 2) == 0, range(10))

# list comprehensions - a cleaner way to create lists
# [ <expression> for <var> in <list> <conditional> ]
squares = [x**2 for x in range(10) if x == 4]

"""
    Classes
"""
# when a class gets defined, a class object gets created which is basically a dictionary with method names
# as the keys and the function code to execute it as the values.


class Car:
    model = ""
    speed = 30
    price = 2000

    def __init__(self, model, speed, price=50000):
        self.model = model
        self.speed = speed
        self.price = price

    def describe_me(self):
        print "I'm a %s, I cost %i, and travel at %i MPH" % (self.model, self.price, self.speed)

toyota = Car("Toyota", 60)
toyota.describe_me()

bmw = Car("BMW", 85, 90000)
bmw.describe_me()

# self is a pointer to the instance of the class
print type(Car)
print type(toyota)

"""
    Generators

        They have the unix pipes methodology of executing as things become available or when needed
"""

