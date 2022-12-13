import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery

import ast

def p1(f):
    ans = 0
    index = 0
    with open(f) as file:

        for left, right in (i.splitlines() for i in file.read().strip('\n').split('\n\n')):
            left = ast.literal_eval(left)
            right = ast.literal_eval(right)
            index += 1
            e = evaluate(list(left),list(right))
            if e == 'Done: In Order':
                ans += index                
    return ans


def p2(f):
    ans = 0
    sorted_packets = []
    with open(f) as file:
        unsorted_packets = [x for x in file.read().strip('\n').split('\n') if x != '' ]
        sorted_packets.append(ast.literal_eval('[[2]]'))
        sorted_packets.append(ast.literal_eval('[[6]]'))

        while unsorted_packets:
            new_packet = ast.literal_eval(unsorted_packets.pop(0))
            for index, packet in enumerate(sorted_packets):
                e = evaluate(list(new_packet),list(packet))
                if e == 'Done: In Order':
                    sorted_packets.insert(sorted_packets.index(packet),new_packet)
                    break
                elif e == 'Done: Out of Order':
                    if index == len(sorted_packets) - 1:
                        sorted_packets.append(new_packet)
                    next
    ans = (sorted_packets.index(ast.literal_eval('[[2]]'))+1) * (sorted_packets.index(ast.literal_eval('[[6]]'))+1)
    return ans


def evaluate(left,right):
    if type(left) == type(right):
        if isinstance(left, int):
            if left < right:
                return 'Done: In Order'
            elif left > right:
                return 'Done: Out of Order'
            else:
                return 'Continue'
        elif isinstance(left, list):
            if not len(left) and len(right):
                return 'Done: In Order'
            elif len(left) and not len(right):
                return 'Done: Out of Order'
            for i in range(max(len(left),len(right))):
                
                if len(left)-1 < i:
                    return 'Done: In Order'
                elif len(right)-1 < i:
                    return 'Done: Out of Order'
                e = evaluate(left[i],right[i])
                if e:
                    if e.startswith('D'):
                        return e
                    if e.startswith('C'):
                        next
    elif isinstance(left, list) and isinstance(right, int):
        return evaluate(left,[right])
    elif isinstance(left, int) and isinstance(right, list):
        return evaluate([left],right)

    

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