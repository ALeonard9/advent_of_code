import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

def p1(f):
    ans = 0
    with open(f) as file:
        map_dict = load_map(file)
        for row in list(map_dict.keys())[1:-1]:
            i = 0
            for tree in map_dict[row][1:-1]:
                i += 1
                tree_height = tree
                tree_x = row
                tree_y = i
                v = check_visibility(map_dict,tree_height, tree_x, tree_y)
                if v:
                    ans += 1
        ans += (len(map_dict)*2 + len(map_dict[0])*2)-4
    return ans


def p2(f):
    ans = 0
    with open(f) as file:
        map_dict = load_map(file)
        for row in list(map_dict.keys())[1:-1]:
            i = 0
            for tree in map_dict[row][1:-1]:
                i += 1
                tree_height = tree
                tree_x = row
                tree_y = i
                vis = calculate_visibility(map_dict,tree_height, tree_x, tree_y)
                if vis > ans:
                    ans = vis
    return ans

def load_map(file):
    i = 0
    map_dict = {}
    for line in file:
        map_dict[i] = []
        line = line.strip()
        for l in line:
            map_dict[i].append(int(l))
        i += 1
    return map_dict

def check_visibility(m,h,x,y):
    visibility = False
    for i1 in range (list(m.keys())[0],x):
        if m[i1][y] >= h:
            break
        if i1 == x-1:
            visibility = True
            return visibility
    for i2 in range (x+1,list(m.keys())[-1]+1):
        if m[i2][y] >= h:
            break
        if i2 == list(m.keys())[-1]:
            visibility = True
            return visibility
    for i3 in range (0,y):
        if m[x][i3] >= h:
            break
        if i3 == y-1:
            visibility = True
            return visibility
    for i4 in range (y+1,len(m[x])):
        if m[x][i4] >= h:
            break
        if i4 == len(m[x])-1:
            visibility = True
            return visibility
    return visibility
        
def calculate_visibility(m,h,x,y):
    v1 = v2 = v3 = v4 = 0
    for i1 in reversed(range (list(m.keys())[0],x)):
        v1 += 1
        if m[i1][y] >= h:
            break
    for i2 in range (x+1,list(m.keys())[-1]+1):
        v2 += 1
        if m[i2][y] >= h:
            break
    for i3 in reversed(range (0,y)):
        v3 += 1
        if m[x][i3] >= h:
            break
    for i4 in range (y+1,len(m[x])):
        v4 += 1
        if m[x][i4] >= h:
            break
    v = v1*v2*v3*v4
    return v


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