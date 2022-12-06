import sys
import os
import argparse
from datetime import datetime
from pathlib import Path
import importlib.util
import importlib.machinery


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


def test_solution(s):
    if s == 1:
        infile = open(path_to_day+'ex_sol1.txt', 'r')
        ex_ans = str(infile.readline())
        result = str(sol.p1(path_to_day+'ex.txt'))
        if result == ex_ans:
            logger.log('Problem 1 example passed.', 'good')
        else:
            logger.log('Problem 1 example failed.', 'fail')
            msg = "Expected " + str(ex_ans) + ",calculated " + str(result)
            logger.log(msg, 'info')
    elif s == 2:
        infile = open(path_to_day+'ex_sol2.txt', 'r')
        ex_ans = str(infile.readline())
        result = str(sol.p2(path_to_day+'ex.txt'))
        if result == ex_ans:
            logger.log('Problem 2 example passed.', 'good')
        else:
            logger.log('Problem 2 example failed.', 'fail')
            msg = "Expected " + str(ex_ans) + ",calculated " + str(result)
            logger.log(msg, 'info')
    else:
        raise AssertionError(
            'Incorrect argument passed. Please send 1 or 2 for the problem you are trying to solve.')


if __name__ == '__main__':
    now = datetime.now()
    year = now.strftime("%Y")
    day = now.strftime("%d")
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--problem",
                        help="Which problem?", required=False, default="1")
    parser.add_argument("-d", "--day", help="Which day?",
                        required=False, default=day)
    parser.add_argument("-y", "--year", help="Which year?",
                        required=False, default=year)
    parser.add_argument("-s", "--suppress", help="Suppress solution?",
                        required=False, default=False, action=argparse.BooleanOptionalAction)

    arg = parser.parse_args()

    if len(arg.day) == 1:
        arg.day = "0"+arg.day

    path_to_day = arg.year+'/'+arg.day+'/'
    sol_module_path = os.path.join(Path().absolute(), path_to_day, 'sol.py')
    sol = import_path(sol_module_path)
    logger_module_path = os.path.join(Path().absolute(), 'utils/logger.py')
    logger = import_path(logger_module_path)

    msg = "Running script for Advent of Code {} on day {} for problem {}".format(
        arg.year, arg.day, arg.problem)
    logger.log(msg, 'info')

    if int(arg.problem) == 1:
        test_solution(1)
        if not arg.suppress: print('Problem 1 solution:', sol.p1(path_to_day+'in.txt'))
    elif int(arg.problem) == 2:
        test_solution(2)
        if not arg.suppress: print('Problem 2 solution:', sol.p2(path_to_day+'in.txt'))
    else:
        raise AssertionError(
            'Incorrect argument passed. Please send 1 or 2 for the problem you are trying to solve.')
