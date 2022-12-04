import sys


class log_style:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


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


def test_solution(s):
    if s == 1:
        infile = open('ex_sol1.txt', 'r')
        ex_ans = int(infile.readline())
        result = p1('ex.txt')
        if result == ex_ans:
            print(log_style.OKGREEN + "Problem 1 example passed."+log_style.ENDC)
        else:
            print(log_style.FAIL + "Problem 1 example failed."+log_style.ENDC)
            print("Expected", ex_ans, ",calculated", result)
    elif s == 2:
        infile = open('ex_sol2.txt', 'r')
        ex_ans = int(infile.readline())
        result = p2('ex.txt')
        if result == ex_ans:
            print(log_style.OKGREEN + "Problem 2 example passed."+log_style.ENDC)
        else:
            print(log_style.FAIL + "Problem 2 example failed."+log_style.ENDC)
            print("Expected", ex_ans, ",calculated", result)
    else:
        raise AssertionError(
            'Incorrect argument passed. Please send 1 or 2 for the problem you are trying to solve.')


if sys.argv[1:]:
    if int(sys.argv[1]) == 1:
        test_solution(1)
        print('Problem 1 solution:', p1('in.txt'))
    elif int(sys.argv[1]) == 2:
        test_solution(2)
        print('Problem 2 solution:', p2('in.txt'))
    else:
        raise AssertionError(
            'Incorrect argument passed. Please send 1 or 2 for the problem you are trying to solve.')
else:
    raise AssertionError(
        'No argument passed. Please send 1 or 2 for the problem you are trying to solve.')
