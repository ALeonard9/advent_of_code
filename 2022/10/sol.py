import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

def p1(f):
    ans = 0
    cycle = 0
    x = 1
    with open(f) as file:
        for line in file:
            line = line.strip()
            if line.startswith('a'):
                _, amount = line.split()
                amount = int(amount)
                cycle, x, ans = cycle_through(cycle, x, ans)
                cycle, x, ans = cycle_through(cycle, x, ans, amount)
            else:
                cycle, x, ans = cycle_through(cycle, x, ans)
    return ans


def p2(f):
    ans = {}
    cycle = 1
    x = 1
    row = 1
    ans[row] = ""
    with open(f) as file:
        for line in file:
            line = line.strip()
            if line.startswith('a'):
                _, amount = line.split()
                amount = int(amount)
                cycle, x, ans, row = draw(cycle, x, ans, row)
                cycle, x, ans, row = draw(cycle, x, ans, row, amount)
            else:
                cycle, x, ans, row = draw(cycle, x, ans, row)
    draw_ans(ans)
    return ans[1]

def cycle_through(cycle, x, ans, amount=0):
    if cycle == 20 or (cycle-20) % 40 == 0:
        ans +=  cycle * x
    x += amount
    cycle += 1
    return cycle, x, ans

def draw(cycle, x, ans, row, amount=0):
    position = cycle-(40*(row-1)) -1
    if position in range(x-1,x+2):
        ans[row] += "#"
    else:    
        ans[row] += "."
    x += amount
    cycle += 1
    if cycle % 40 == 1: 
        row += 1
        if row < 7: ans[row] = ""
    return cycle, x, ans, row

def draw_ans(ans):
    for key in ans:
        print(ans[key])

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