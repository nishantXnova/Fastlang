class Compiler:
    def compile(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        bytecode = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith('let '):
                # let x = 10
                parts = line.split(' = ')
                var = parts[0].split(' ')[1]
                val = int(parts[1])
                bytecode.append(("PUSH", val))
                bytecode.append(("STORE", var))
            elif line.startswith('print '):
                expr = line[6:]  # remove 'print '
                if ' + ' in expr:
                    # print x + y or 5 + 3
                    a, b = expr.split(' + ')
                    if a.isdigit():
                        bytecode.append(("PUSH", int(a)))
                    else:
                        bytecode.append(("LOAD", a))
                    if b.isdigit():
                        bytecode.append(("PUSH", int(b)))
                    else:
                        bytecode.append(("LOAD", b))
                    bytecode.append(("ADD",))
                else:
                    # print x or print 5
                    if expr.isdigit():
                        bytecode.append(("PUSH", int(expr)))
                    else:
                        bytecode.append(("LOAD", expr))
                bytecode.append(("PRINT",))
        return bytecode
