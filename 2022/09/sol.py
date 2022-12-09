import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

def p1(f):
    ans = 0
    head = Knot('Head')
    tail = Knot('Tail')
    spots = []
    with open(f) as file:
        for line in file:
            direction, move = line.strip().split()
            for m in range(0,int(move)):
                head.lead(direction)
                tail.follow(head)
                spots.append("{},{}".format(tail.x,tail.y))
        ans = len(set(spots))
    return ans


def p2(f):
    ans = 0
    knots = [Knot("Knot{}".format(x)) for x in range(10)]
    spots = []
    with open(f) as file:
        for line in file:
            direction, move = line.strip().split()
            for m in range(0,int(move)):
                knots[0].lead(direction)
                for i in range(1,len(knots)):
                    knots[i].follow(knots[i-1])
                spots.append("{},{}".format(knots[-1].x,knots[-1].y))
        ans = len(set(spots))

    return ans

class Knot:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
    def lead(self,direction):
        match direction:
            case 'U':  
                self.y += 1
            case 'D':
                self.y -= 1
            case 'R':
                self.x +=1
            case 'L':
                self.x -=1
        return

    def follow(tail,head):
        if abs(tail.x-head.x) <= 1 and abs(tail.y-head.y) <= 1:
            return
        elif tail.x == head.x:
            tail.y = int((head.y+tail.y)/2)
        elif tail.y == head.y:
            tail.x = int((head.x+tail.x)/2)
        else:
            if abs(head.x - tail.x) == abs(head.y-tail.y) == 2:
                tail.x = int((head.x+tail.x)/2)
                tail.y = int((head.y+tail.y)/2)
            if abs(head.x - tail.x) == 2:
                tail.x = int((head.x+tail.x)/2)
                tail.y = head.y
            if abs(head.y-tail.y) == 2:
                tail.x = head.x
                tail.y = int((head.y+tail.y)/2)
    def pos(self):
        return "{},{}".format(self.x,self.y)

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