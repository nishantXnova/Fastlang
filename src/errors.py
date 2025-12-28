class CompileError(Exception):
    def __init__(self, message, line=None):
        self.message = message
        self.line = line
        super().__init__(f"CompileError{' (line ' + str(line) + ')' if line else ''}: {message}")

class RuntimeError(Exception):
    def __init__(self, message, line=None):
        self.message = message
        self.line = line
        super().__init__(f"RuntimeError{' (line ' + str(line) + ')' if line else ''}: {message}")
