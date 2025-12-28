from .errors import RuntimeError

class VirtualMachine:
    def __init__(self):
        self.stack = []
        self.vars = {}

    def run(self, bytecode):
        def check_stack(n, line):
            if len(self.stack) < n:
                raise RuntimeError("Stack underflow", line)

        for instruction in bytecode:
            op = instruction[0]
            line = instruction[2] if len(instruction) > 2 else None
            if op == "PUSH":
                self.stack.append(instruction[1])
            elif op == "ADD":
                check_stack(2, line)
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
            elif op == "PRINT":
                check_stack(1, line)
                print(self.stack.pop())
            elif op == "STORE":
                check_stack(1, line)
                self.vars[instruction[1]] = self.stack.pop()
            elif op == "LOAD":
                if instruction[1] not in self.vars:
                    raise RuntimeError(f"Undefined variable '{instruction[1]}'", line)
                self.stack.append(self.vars[instruction[1]])
            else:
                raise RuntimeError(f"Unknown opcode: {op}", line)
