import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

from string import ascii_lowercase
from heapq import heappop, heappush

def p1(f):
    ans = 0
    map, start, end = convert_map(f)
    ans = ascend(map, start, end)
    
    return ans

def p2(f):
    ans = 0
    map, _, end = convert_map(f)
    ans = descend(map, end)
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

def check_direction_up(map, coordinates):
    x = coordinates[0]
    y = coordinates[1]

    dirs = {}
    dirs[(x,y+1)] = False
    dirs[(x,y-1)] = False
    dirs[(x-1,y)] = False
    dirs[(x+1,y)] = False

    for dir in dirs:
        if dir in list(map.keys()):
            if map[coordinates]+1 >= map[dir]:
                dirs[dir] = True

    return dirs

def check_direction_down(map, coordinates):
    x = coordinates[0]
    y = coordinates[1]

    dirs = {}
    dirs[(x,y+1)] = False
    dirs[(x,y-1)] = False
    dirs[(x-1,y)] = False
    dirs[(x+1,y)] = False

    for dir in dirs:
        if dir in list(map.keys()):
            if (map[coordinates] - map[dir]) <= 1:
                dirs[dir] = True

    return dirs


def ascend(map, start, end):
    visited = []
    heap = [(0, start[0], start[1])]

    while True:
        if not heap:
            return 1000
        steps, i, j = heappop(heap)
        if (i,j) in visited:
            continue
        visited.append((i,j))

        if (i, j) == end:
            return steps
        
        dirs = check_direction_up(map,(i,j))

        for coordinates in [c for c, v in dirs.items() if v]:
            heappush(heap, (steps + 1, coordinates[0], coordinates[1]))

def descend(map, start):
    visited = []
    heap = [(0, start[0], start[1])]

    while True:
        if not heap:
            return 1000
        steps, i, j = heappop(heap)
        if (i,j) in visited:
            continue
        visited.append((i,j))

        if (i, j) == end:
            return steps
        
        dirs = check_direction_up(map,(i,j))

        for coordinates in [c for c, v in dirs.items() if v]:
            heappush(heap, (steps + 1, coordinates[0], coordinates[1]))


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