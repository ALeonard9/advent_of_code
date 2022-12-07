import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

def p1(f):
    ans = 0
    dir_list = []
    dir_dict = {}
    curr_dir = ''
    with open(f) as file:
        for line in file:
            line = line.strip()
            if line.startswith('$ cd'):
                curr_dir = line.split(' ')[-1]
                if curr_dir == '..':
                    curr_dir = dir_list.pop(-1)
                else:
                    dir_list.append(curr_dir)

            if line[0].isdigit():
                n = 0
                for d in dir_list:
                    i = 0
                    n += 1
                    dir_name = ''
                    while i < n:
                        if dir_list[i] == '/': 
                            base = dir_list[i]
                        else:
                            base = dir_list[i]+'/'
                        dir_name += base
                        i +=1
                    if dir_name in dir_dict.keys():
                        dir_dict[dir_name] += int(line.split(' ')[0])
                    else:
                        dir_dict[dir_name] = int(line.split(' ')[0])
        for k in dir_dict.keys():
            if dir_dict[k] < 100000:
                ans += dir_dict[k]

    return ans


def p2(f):
    ans = 0
    dir_list = []
    dir_dict = {}
    curr_dir = ''
    with open(f) as file:
        for line in file:
            line = line.strip()
            if line.startswith('$ cd'):
                curr_dir = line.split(' ')[-1]
                if curr_dir == '..':
                    curr_dir = dir_list.pop(-1)
                else:
                    dir_list.append(curr_dir)

            if line[0].isdigit():
                n = 0
                for d in dir_list:
                    i = 0
                    n += 1
                    dir_name = ''
                    while i < n:
                        if dir_list[i] == '/': 
                            base = dir_list[i]
                        else:
                            base = dir_list[i]+'/'
                        dir_name += base
                        i +=1
                    if dir_name in dir_dict.keys():
                        dir_dict[dir_name] += int(line.split(' ')[0])
                    else:
                        dir_dict[dir_name] = int(line.split(' ')[0])
        space_needed = dir_dict['/'] - 40000000
        sorted_dict = dict(sorted(dir_dict.items(), key=lambda item: item[1]))
        for k in sorted_dict.keys():
            if sorted_dict[k] >= space_needed:
                ans = sorted_dict[k]
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