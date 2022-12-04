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
            comma = int(line.find(','))
            line_end = len(line)
            elf1 = line[0:comma]
            elf1_start = int(elf1[0:elf1.find('-')])
            elf1_end = int(elf1[elf1.find('-')+1:comma])

            elf2 = line[comma+1:line_end]
            elf2_start = int(elf2[0:elf2.find('-')])
            elf2_end = int(elf2[elf2.find('-')+1:line_end])

            if (elf1_start <= elf2_start and elf1_end >= elf2_end) or (elf1_start >= elf2_start and elf1_end <= elf2_end):
                total_score += 1
    ans = total_score
    return ans


def p2(f):
    ans = 0
    total_score = 0
    with open(f) as file:
        for line in file:
            line = line.strip()
            comma = int(line.find(','))
            line_end = len(line)
            elf1 = line[0:comma]
            elf1_start = int(elf1[0:elf1.find('-')])
            elf1_end = int(elf1[elf1.find('-')+1:comma])

            elf2 = line[comma+1:line_end]
            elf2_start = int(elf2[0:elf2.find('-')])
            elf2_end = int(elf2[elf2.find('-')+1:line_end])

            if (elf1_start <= elf2_start <= elf1_end) or (elf1_start <= elf2_end <= elf1_end) or (elf2_start <= elf1_start <= elf2_end) or (elf2_start <= elf1_end <= elf2_end):
                total_score += 1
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