import sys
import os

# Add src folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from vm import VirtualMachine

bytecode = [
    ("PUSH", 10),
    ("PUSH", 5),
    ("ADD",),
    ("PRINT",)
]

vm = VirtualMachine()
vm.run(bytecode)
