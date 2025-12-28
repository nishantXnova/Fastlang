import sys
from src.vm import VirtualMachine
from src.compiler import Compiler

if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    file_path = "examples/test.fl"

compiler = Compiler()
bytecode = compiler.compile(file_path)
print("Bytecode:", bytecode)
vm = VirtualMachine()
vm.run(bytecode)
