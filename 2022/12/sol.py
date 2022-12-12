import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

from string import ascii_lowercase

def p1(f):
    ans = 0
    map, start, end = convert_map(f)
    possible_routes = [[start]]
    finished_routes = []
    done = False
    while not done:
    # ib = 0
    # ie = 1
    # while ib < ie:
        # route = possible_routes[ib]
        route = possible_routes[0]
        dirs = check_direction(map,route[-1],route)
        for coordinates in [c for c, v in dirs.items() if v]:
            if not coordinates in [x[-1] for x in possible_routes[1:]]:
                new_route = []
                new_route = list(route)
                new_route.append(coordinates)
                possible_routes.append(new_route)
                # ie += 1
                if new_route[-1] == end:
                    logger.log(len(new_route))
                    finished_routes.append(new_route)
                    possible_routes.remove(new_route)
                # ie -= 1
        possible_routes.remove(route)
        if len(possible_routes) == 0: done = True
        # ie -= 1
        # ib += 1
            # logger.log(possible_routes)
            # done = True # REMOVE LATER
        # if all(flag[-1] == end for (flag) in possible_routes): done = True
    ans = int(len(min(finished_routes, key = len))) -1
    return ans

def p2(f):
    ans = 0
    with open(f) as file:
        for line in file:
            line = line.strip()

    return ans

def convert_map(f):
    map = {}
    row = 0
    height_chart = {}
    for i , l in enumerate(ascii_lowercase):
        height_chart[l] = i
    height_chart['S'] = 0
    height_chart['E'] = 25
    with open(f) as file:
        for line in file:
            line = line.strip()
            pos = 0
            for l in line:
                if l == 'S': start = (pos,row)
                if l == 'E': end = (pos,row)
                map[(pos,row)] = height_chart[l]
                pos += 1
            row -= 1
    return map, start, end

def check_direction(map, coordinates, route):
    x = coordinates[0]
    y = coordinates[1]

    dirs = {}
    dirs[(x,y+1)] = False
    dirs[(x,y-1)] = False
    dirs[(x-1,y)] = False
    dirs[(x+1,y)] = False

    for dir in dirs:
        if dir in list(map.keys()):
            # logger.log("{} exists".format(dir))
            if dir not in route and map[coordinates]+1 >= map[dir]:
                # logger.log("{} is an acceptable height".format(dir))
                dirs[dir] = True

    return dirs


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