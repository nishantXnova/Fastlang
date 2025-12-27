class VirtualMachine:
    def __init__(self):
        self.stack = []
        self.vars = {}

    def run(self, bytecode):
        ops = {
            "PUSH": lambda i: self.stack.append(i[1]),
            "ADD": lambda i: self.stack.append(self.stack.pop() + self.stack.pop()),
            "PRINT": lambda i: print(self.stack.pop()),
            "STORE": lambda i: (self.vars.__setitem__(i[1], self.stack.pop())),
            "LOAD": lambda i: self.stack.append(self.vars[i[1]])
        }
        for instruction in bytecode:
            op = instruction[0]
            if op in ops:
                ops[op](instruction)
            else:
                raise ValueError(f"Unknown opcode: {op}")
