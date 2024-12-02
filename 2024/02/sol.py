import os
import sys
from pathlib import Path
import importlib.util
import importlib.machinery


def p1(f):
    ans = 0
    with open(f) as file:
        for line in file:
            report = []
            direction = "unknown"
            legit = True
            line = line.strip()
            report = list(map(int, line.split()))
            for i in range(1, len(report)):
                if (
                    abs(report[i - 1] - report[i]) >= 4
                    or abs(report[i - 1] - report[i]) == 0
                ):
                    legit = False
                    break
                if report[i - 1] < report[i] and direction == "unknown":
                    direction = "up"
                elif report[i - 1] > report[i] and direction == "unknown":
                    direction = "down"
                else:
                    if report[i - 1] < report[i] and direction == "down":
                        legit = False
                        break
                    elif report[i - 1] > report[i] and direction == "up":
                        legit = False
                        break
            if legit:
                ans += 1
    return ans


def p2(f):
    ans = 0
    with open(f) as file:
        for line in file:
            line = line.strip()
            report = []
            report = list(map(int, line.split()))
            ans += check_report(report)

    return ans


def check_report(report):
    good = 0
    report_meta = {"direction": "unknown", "failures": 0, "first_fail": False}
    for i in range(1, len(report)):
        report_meta = check_pairs(report[i - 1], report[i], report_meta)
        if report_meta["first_fail"]:
            if i + 1 < len(report):
                report_meta = check_pairs(report[i - 1], report[i + 1], report_meta)
    if report_meta["failures"] <= 1:
        good = 1
    return good


def check_pairs(first, second, report_meta):
    if abs(first - second) >= 4 or abs(first - second) == 0:
        report_meta["failures"] += 1
        report_meta["first_fail"] = True
    if first < second and report_meta["direction"] == "unknown":
        report_meta["direction"] = "up"
    elif first > second and report_meta == "unknown":
        report_meta["direction"] = "down"
    else:
        if first < second and report_meta["direction"] == "down":
            report_meta["failures"] += 1
            report_meta["first_fail"] = True
        elif first > second and report_meta["direction"] == "up":
            report_meta["failures"] += 1
            report_meta["first_fail"] = True
    return report_meta


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
