"""
Header
"""

"""
    Interpreter

        sourcecode => python bytecode
"""
# the interpreter first compiles source files into python bytecode .pyc
bytecode = compile('x=2\nprint "X is", x',"fake_module", "exec")
# this is the bytecode representation
print [ord(byte) for byte in bytecode.co_code]

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
'''


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


