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
                expr = line[6:]  # remove 'print '
                if ' + ' in expr:
                    # print x + y or 5 + 3
                    parts = expr.split(' + ')
                    if len(parts) != 2:
                        raise CompileError("Invalid expression syntax", line_num)
                    a, b = parts
                    if a.isdigit():
                        bytecode.append(("PUSH", int(a), line_num))
                    else:
                        bytecode.append(("LOAD", a, line_num))
                    if b.isdigit():
                        bytecode.append(("PUSH", int(b), line_num))
                    else:
                        bytecode.append(("LOAD", b, line_num))
                    bytecode.append(("ADD", line_num))
                else:
                    # print x or print 5
                    if expr.isdigit():
                        bytecode.append(("PUSH", int(expr), line_num))
                    else:
                        bytecode.append(("LOAD", expr, line_num))
                bytecode.append(("PRINT", line_num))
            else:
                raise CompileError("Unknown statement", line_num)
        return bytecode
