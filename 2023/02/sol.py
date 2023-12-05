import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

def p1(f):
    ans = 0
    game = 1
    max_colors = {
        'red': 12, 
        'green': 13,
        'blue': 14
    }
    with open(f) as file:
        for line in file:
            possible = True
            line = line.strip()
            line = line[line.find(':')+2:]
            sets = line.split(';')
            for set in sets:
                cubes = set.split(',')
                for cube in cubes:
                    c = cube.split()
                    if int(c[0]) > max_colors[c[1]]:
                        possible = False
            if possible:
                ans += game
            game += 1
    return ans


def p2(f):
    ans = 0
    with open(f) as file:
        for line in file:
            lowest_color = {
                'red': 0,
                'blue': 0,
                'green': 0
            }
            line = line.strip()
            game = line[line.find(':')+2:]
            sets = game.split(';')
            for set in sets:
                cubes = set.split(',')
                for cube in cubes:
                    c = cube.split()
                    if int(c[0]) > lowest_color[c[1]]:
                        lowest_color[c[1]] = int(c[0])
            ans += (lowest_color['red']* lowest_color['green']*lowest_color['blue'])
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