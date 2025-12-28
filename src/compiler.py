from .errors import CompileError

class Compiler:
    def compile(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        bytecode = []
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue
            if line.startswith('let '):
                # let x = 10
                if ' = ' not in line:
                    raise CompileError("Invalid assignment syntax", line_num)
                parts = line.split(' = ')
                if len(parts) != 2:
                    raise CompileError("Invalid assignment syntax", line_num)
                var_part = parts[0]
                val_part = parts[1]
                if not var_part.startswith('let ') or len(var_part.split()) != 2:
                    raise CompileError("Invalid assignment syntax", line_num)
                var = var_part.split()[1]
                try:
                    val = int(val_part)
                except ValueError:
                    raise CompileError("Invalid value in assignment", line_num)
                bytecode.append(("PUSH", val, line_num))
                bytecode.append(("STORE", var, line_num))
            elif line.startswith('print '):
                expr = line[6:].strip()  # remove 'print ' and strip
                bytecode.extend(self.compile_expression(expr, line_num))
                bytecode.append(("PRINT", line_num))
            else:
                raise CompileError("Unknown statement", line_num)
        return bytecode

    def compile_expression(self, expr, line_num):
        # Tokenize: split by spaces
        tokens = expr.split()
        if not tokens:
            raise CompileError("Empty expression", line_num)
        # Shunting-yard algorithm for infix to postfix
        output = []
        operators = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        for token in tokens:
            if token.isdigit():
                output.append(("PUSH", int(token), line_num))
            elif token in precedence:
                while operators and operators[-1] in precedence and precedence[operators[-1]] >= precedence[token]:
                    op = operators.pop()
                    output.append((self.op_to_bytecode(op), line_num))
                operators.append(token)
            else:
                # Assume variable
                output.append(("LOAD", token, line_num))
        while operators:
            op = operators.pop()
            output.append((self.op_to_bytecode(op), line_num))
        return output

    def op_to_bytecode(self, op):
        return {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}[op]
