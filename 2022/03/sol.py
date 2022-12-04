import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

def p1(f):
    ans = 0
    total_score = 0
    with open(f) as file:
        for line in file:
            line = line.strip()
            line_length = len(line)
            chars = line_length
            half = int(chars/2)
            first_line = line[0:int(half)]
            second_line = line[half:chars]
            common = ''.join(set(first_line).intersection(second_line))
            unicode_subtract = 64 - 26
            if common.islower():
                unicode_subtract = 96

            common_score = ord(common) - unicode_subtract

            total_score += common_score
    ans = total_score
    return ans


def p2(f):
    ans = 0
    total_score = 0
    int = 1
    line_list = []
    with open(f) as file:
        for line in file:
            line = line.strip()
            line_list.append(line.strip())
            if int < 3:
                int += 1
            else:
                int = 1
                common_obj = set.intersection(*map(set, line_list))
                line_list = []
                common = list(common_obj)[0]
                unicode_subtract = 64 - 26
                if common.islower():
                    unicode_subtract = 96

                common_score = ord(common) - unicode_subtract

                total_score += common_score
    ans = total_score
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
