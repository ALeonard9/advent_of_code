import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

def p1(f):
    ans = 1
    coordinates = ["0,0"]
    x = 0
    y = 0
    with open(f) as file:
        for line in file:
            line = line.strip()
            for sym in line:
                x,y = mover(sym,x,y)
                curr = "{},{}".format(x,y)
                if not curr in coordinates:
                    coordinates.append(curr)
                    ans += 1

    return ans


def p2(f):
    ans = 1
    coordinates = ["0,0"]
    santa = GiftGiver()
    robo_santa = GiftGiver()
    i=0
    with open(f) as file:
        for line in file:
            line = line.strip()

            for sym in line:
                i += 1
                if (i % 2) == 0:
                    s = santa
                else:
                    s = robo_santa
                s.move(sym)
                curr = "{},{}".format(s.x,s.y)
                if not curr in coordinates:
                    coordinates.append(curr)
                    ans += 1
    return ans

class GiftGiver:
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self,sym):
        self.x,self.y = mover(sym,self.x,self.y)


def mover(sym,x,y):
    match sym:
        case '^':
            x += 1
        case '>':
            y += 1
        case 'v':
            x -= 1
        case '<':
            y -= 1
    return x,y

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