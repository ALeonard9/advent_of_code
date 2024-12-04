import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery
import re


def p1(f):
    ans = 0
    with open(f) as file:
        for line in file:
            line = line.strip()
            ans = find_mul(line)
    return ans


def p2(f):
    ans = 0
    string = ""
    with open(f) as file:
        for line in file:
            line = line.strip()
            string += line
    split_result = split_on_do_and_dont(string)
    add = True
    for part in split_result:
        if part == "do()":
            add = True
        elif part == "don't()":
            add = False
        else:
            if add:
                ans += find_mul(part)
    return ans


def find_mul(line):
    ans = 0
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, line)
    for match in matches:
        x, y = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", match).groups()
        ans += int(x) * int(y)
    return ans


def split_on_do_and_dont(s):
    pattern = r"do\(\)|don't\(\)"
    split_result = re.split(pattern, s)
    matches = re.findall(pattern, s)
    result = []
    for part, match in zip(split_result, matches + [""]):
        result.append(part)
        if match:
            result.append(match)

    return result


def import_path(path):
    module_name = os.path.basename(path).replace("-", "_")

    spec = importlib.util.spec_from_loader(
        module_name, importlib.machinery.SourceFileLoader(module_name, path)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[module_name] = module
    return module


logger_module_path = os.path.join(Path().absolute(), "utils/logger.py")
logger = import_path(logger_module_path)
