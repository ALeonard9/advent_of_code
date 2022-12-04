import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

def p1(f):
    ans = 0
    total_points = 0
    with open(f) as file:
        for line in file:
            line = line.strip()
            match_list = line.split()
            for item in match_list:
                match item:
                    case 'X':
                        points = 1
                        match opp:
                            case 'A':
                                points += 3
                            case 'B':
                                points += 0
                            case 'C':
                                points += 6
                        total_points += points
                    case 'Y':
                        points = 2
                        match opp:
                            case 'A':
                                points += 6
                            case 'B':
                                points += 3
                            case 'C':
                                points += 0
                        total_points += points
                    case 'Z':
                        points = 3
                        match opp:
                            case 'A':
                                points += 0
                            case 'B':
                                points += 6
                            case 'C':
                                points += 3
                        total_points += points
                    case _:
                        opp = item
                        points = 0
    ans = total_points
    return ans


def p2(f):
    ans = 0
    total_points = 0
    with open(f) as file:
        for line in file:
            line = line.strip()
            match_list = line.split()
            for item in match_list:
                match item:
                    case 'X':
                        points = 0
                        match opp:
                            case 'A':
                                points += 3
                            case 'B':
                                points += 1
                            case 'C':
                                points += 2
                        total_points += points
                    case 'Y':
                        points = 3
                        match opp:
                            case 'A':
                                points += 1
                            case 'B':
                                points += 2
                            case 'C':
                                points += 3
                        total_points += points
                    case 'Z':
                        points = 6
                        match opp:
                            case 'A':
                                points += 2
                            case 'B':
                                points += 3
                            case 'C':
                                points += 1
                        total_points += points
                    case _:
                        opp = item
                        points = 0

    ans = total_points
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