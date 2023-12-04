import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

def p1(f):
    ans = 0
    ans_list = []
    with open(f) as file:
        for line in file:
            num_list = []
            line = line.strip()
            for d in line:
                if d.isnumeric():
                    num_list.append(d)
            ans_list.append(int(str(num_list[0]) + str(num_list[-1])))

    ans = sum(ans_list)
    return ans


def p2(f):
    ans = 0
    ans_list = []
    with open(f) as file:
        for line in file:
            first_number = 0
            last_number = 0
            num_list = []
            placeholder = ''
            line = line.strip()
            number_names = ['one','two','three','four','five','six','seven','eight','nine']
            for d in line:
                if first_number > 0:
                    break
                if d.isnumeric():
                    first_number = d
                    break
                elif d.isalpha():
                    placeholder += d
                    if any(num in placeholder for num in number_names):
                        i = 0
                        number = ''
                        for i,number in enumerate(number_names,start=1):
                            if number in placeholder:
                                first_number = i
                                break
            reversed_line = line[::-1]
            placeholder = ''
            for d in reversed_line:
                if last_number > 0:
                    break
                if d.isnumeric():
                    last_number = d
                    break
                elif d.isalpha():
                    placeholder = d + placeholder
                    if any(num in placeholder for num in number_names):
                        i = 0
                        number = ''
                        for i,number in enumerate(number_names,start=1):
                            if number in placeholder:
                                last_number = i
                                break
            ans_list.append(int(str(first_number) + str(last_number)))

    ans = sum(ans_list)
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