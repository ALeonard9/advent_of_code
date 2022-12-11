import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery
sys.set_int_max_str_digits(0)

def p1(f):
    ans = 0
    rounds = 20
    relief = True
    monkeys = []
    with open(f) as file:
        instructions =dict((i,x) for i,x in enumerate(i.splitlines() for i in file.read().strip('\n').split('\n\n')))
        for ins in instructions:
            monkeys.append(Monkey(instructions[ins]))
    
    mod = 1
    for m in monkeys:
        mod *= m.test

    for r in range(rounds):  
        for m in monkeys:
            m.inspect(monkeys, relief, mod)

    inspect_nums = []
    for monkey in monkeys:
        inspect_nums.append(monkey.inspect_num)
    ans = sorted(inspect_nums,reverse=True)[0] * sorted(inspect_nums,reverse=True)[1]

    return ans


def p2(f):
    ans = 0
    rounds = 10000
    relief = False
    monkeys = []
    with open(f) as file:
        instructions =dict((i,x) for i,x in enumerate(i.splitlines() for i in file.read().strip('\n').split('\n\n')))
        for ins in instructions:
            monkeys.append(Monkey(instructions[ins]))

    mod = 1
    for m in monkeys:
        mod *= m.test
           
    for r in range(rounds):  
        for m in monkeys:
            m.inspect(monkeys, relief, mod)

    inspect_nums = []
    for monkey in monkeys:
        inspect_nums.append(monkey.inspect_num)
    ans = sorted(inspect_nums,reverse=True)[0] * sorted(inspect_nums,reverse=True)[1]
    return ans

class Monkey:
    def __init__(self,instructions):
        self.name = instructions[0][:-1]
        self.items = []
        item_list = instructions[1].split(':')[1]
        item_list = item_list.split(',')
        for i in item_list:
            self.items.append(int(i.strip()))
        self.operator = instructions[2].split('=')[1].strip().split(' ')[1]
        self.operation_num = instructions[2].split('=')[1].strip().split(' ')[2]
        self.test = int(instructions[3].split()[-1])
        self.throw_true = int(instructions[4].split()[-1])
        self.throw_false = int(instructions[5].split()[-1])
        self.inspect_num = 0
    
    def inspect(self, monkeys, relief, mod):
        for i in self.items:
            o = self.operation_num
            if not relief: i %= mod
            if self.operation_num == 'old': o = i
            statement = "{}{}{}".format(i,self.operator,o)
            new = eval(statement)
            if relief: new =  new // 3
            if new % self.test == 0:
                monkeys[self.throw_true].items.append(new)
            else:
                monkeys[self.throw_false].items.append(new)
            self.inspect_num +=1
        self.items = []


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