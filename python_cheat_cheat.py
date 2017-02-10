"""
Header
"""

# important modules
import dis      # disassembler of python bytecode
import sys      # functions and objects that interact closely with the interpreter

# remove unused modules warning
sys
dis

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
# the varaibles and imported modules
names_in_current_scope = dir()

'''
    Functions

        + Internally the just extend PyObject
        + In essence contain a code object with the byte code and variables surrounding the "environment"
        + When you call a function, basically a new frame is created with code to execute, global + local variables
        + Function objects are created when <def> is encountered

'''


def my_func(x):
    y = x + 1
    print y

print dir(my_func)


"""
    Functional Programming
"""