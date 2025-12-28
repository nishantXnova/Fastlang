from src.vm import VirtualMachine
from src.compiler import Compiler
compiler = Compiler()
bytecode = compiler.compile("examples/test.fl")
VirtualMachine().run(bytecode)
