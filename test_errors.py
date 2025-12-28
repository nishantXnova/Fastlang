from src.compiler import Compiler
from src.vm import VirtualMachine
from src.errors import CompileError, RuntimeError

def test_file(file_path):
    try:
        compiler = Compiler()
        bytecode = compiler.compile(file_path)
        print(f"Compiled {file_path} successfully: {bytecode}")
        vm = VirtualMachine()
        vm.run(bytecode)
    except (CompileError, RuntimeError) as e:
        print(f"Error in {file_path}: {e}")

if __name__ == "__main__":
    test_file("examples/test.fl")
    test_file("examples/broken1.fl")
    test_file("examples/broken2.fl")
    test_file("examples/broken3.fl")
