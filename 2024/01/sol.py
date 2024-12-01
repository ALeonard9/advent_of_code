import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery
from collections import Counter


def p1(f):
    ans = 0
    left = []
    right = []
    with open(f) as file:
        for line in file:
            line = line.strip()
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))

        left.sort()
        right.sort()
        # add the difference between the two lists
        for i in range(len(left)):
            ans += abs(left[i] - right[i])
    return ans


def p2(f):
    ans = 0
    left = []
    right = []
    similarity = []
    with open(f) as file:
        for line in file:
            line = line.strip()
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))

        left.sort()
        right.sort()

        freq = Counter(right)
        for i in range(len(left)):
            similarity.append(left[i] * freq[left[i]])
        ans = sum(similarity)
    return ans


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
