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
    ans = 0
    with open(f) as file:
        for line in file:
            line = line.strip()

    return ans

def cycle_through(cycle, x, ans, amount=0):
    # logger.log("BEGIN: Cycle {}".format(cycle))
    if cycle == 20 or (cycle-20) % 40 == 0:
        ans +=  cycle * x
        logger.log("{},{},{}".format(cycle,x,ans))
    x += amount
    # logger.log("{},{},{}".format(cycle,x,ans))
    # logger.log("END Cycle {}".format(cycle))
    cycle += 1
    return cycle, x, ans

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