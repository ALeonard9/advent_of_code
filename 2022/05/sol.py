import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

def p1(f):
    ans = ''
    ship = {}
    line_cnt = 0
    with open(f) as file:
        for line in file:
            if line[0] != 'm':
                last_box = 0
                box = line.find('[', last_box)
                while box >= 0:
                    box = line.find('[', last_box)
                    if box >= 0:
                        lane = int((box/4) + 1)
                        last_box = box+1
                        letter = line[box+1]
                        if ship.get(lane) is None:
                            ship[lane] = [] 
                        ship[lane].append(letter)
            else:
                last = 0
                move_beg = line.find(' ', last)
                last = move_beg+1
                move_end = line.find(' ', last)
                last = move_end+1
                from_beg =line.find(' ', last)
                last = from_beg+1
                from_end = line.find(' ', last)
                last = from_end+1
                to_beg = line.find(' ', last)
                to_end = len(line)
                move = int(line[move_beg:move_end])
                from_lane = int(line[from_beg:from_end])
                to_lane = int(line[to_beg:to_end])
                i = 0
                while i < move:
                    tmp = ship[from_lane].pop(0)
                    ship[to_lane].insert(0,tmp)
                    i +=1  
    k = 0
    ship_len = len(ship)
    while k < ship_len:
        k += 1
        ans += ship[k].pop(0) 
    return ans


def p2(f):
    ans = ''
    ship = {}
    line_cnt = 0
    with open(f) as file:
        for line in file:
            if line[0] != 'm':
                last_box = 0
                box = line.find('[', last_box)
                while box >= 0:
                    box = line.find('[', last_box)
                    if box >= 0:
                        lane = int((box/4) + 1)
                        last_box = box+1
                        letter = line[box+1]
                        if ship.get(lane) is None:
                            ship[lane] = [] 
                        ship[lane].append(letter)
            else:
                last = 0
                move_beg = line.find(' ', last)
                last = move_beg+1
                move_end = line.find(' ', last)
                last = move_end+1
                from_beg =line.find(' ', last)
                last = from_beg+1
                from_end = line.find(' ', last)
                last = from_end+1
                to_beg = line.find(' ', last)
                to_end = len(line)
                move = int(line[move_beg:move_end])
                from_lane = int(line[from_beg:from_end])
                to_lane = int(line[to_beg:to_end])
                i = 0
                tmp = []
                while i < move:
                    tmp.append(ship[from_lane].pop(move-i-1))
                    i +=1  
                j = 0
                while j < move:
                    ship[to_lane].insert(0,tmp.pop(0))
                    j +=1
    k = 0
    ship_len = len(ship)
    while k < ship_len:
        k += 1
        ans += ship[k].pop(0) 
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