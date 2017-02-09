"""
    Interpreter

        sourcecode => python bytecode
"""

#the interpreter first compilessoure files into python bytecode .pyc
bytecode = compile('x=2\nprint "X is", x',"fake_module", "exec")
#this is the bytecode representation
print [ord(byte) for byte in bytecode.co_code]
#run a piece of code
print eval(bytecode)



