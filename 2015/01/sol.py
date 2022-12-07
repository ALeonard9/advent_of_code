import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

def p1(f):
    ans = 0
    with open(f) as file:
        for line in file:
            line = line.strip()
            up = line.count('(')
            down = line.count(')')
            ans = up - down

    return ans


def p2(f):
    ans = 0
    floor = 0
    i = 0
    with open(f) as file:
        for line in file:
            line = line.strip()
            for c in line:
                i += 1
                if c == '(':
                    floor += 1
                elif c == ')':
                    floor -= 1
                if floor < 0:
                    ans = i
                    break

    return ans

def import_path(path):
    module_name = os.path.basename(path).replace('-', '_')

    spec = importlib.util.spec_from_loader(
        module_name,
        importlib.machinery.SourceFileLoader(module_name, path)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[module_name] = module
    return module
logger_module_path = os.path.join(Path().absolute(),'utils/logger.py')
logger = import_path(logger_module_path)