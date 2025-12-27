class VirtualMachine:
    def __init__(self):
        self.stack = []

    def run(self, bytecode):
        for instruction in bytecode:
            op = instruction[0]
            if op == "PUSH":
                self.stack.append(instruction[1])
            elif op == "ADD":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
            elif op == "PRINT":
                print(self.stack.pop())
            else:
                raise ValueError(f"Unknown opcode: {op}")
