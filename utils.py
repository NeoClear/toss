import os
import sys
from typing import List
import copy
import math
import toss

l1 = {"filename", "category", "duration", "map", "team"}
l2 = {"filename", "category", "duration", "map", "team", "winner", "date"}
l3 = {"filename", "category", "duration", "map", "version", "team", "winner", "date", "frame"}

def print_info(paths: List[str], level=1) -> None:
    """Print info of replay files in paths according to level of detail level
    """
    toss_cli = toss.toss()
    for path in paths:
        ret = toss_cli.analyze_file(path)
        print("################")
        ref = ""
        if level == 1:
            ref = l1
        elif level == 2:
            ref = l2
        elif level == 3:
            ref = l3
        else:
            ref = l1
        for name, content in ret.items():
            if name in ref:
                print(name + ":", content)

class file:
    _current_pwd = ""
    _execute_pwd = ""

    def __init__(self):
        self._current_pwd = os.getcwd()
        self._execute_pwd = os.path.abspath(sys.argv[0])

    @property
    def current_pwd(self):
        return self._current_pwd
    
    @current_pwd.setter
    def current_pwd(self, pwd):
        if isinstance(pwd, str):
            self._current_pwd = pwd

    @current_pwd.deleter
    def current_pwd(self):
        del self._current_pwd

    def refresh(self):
        self._current_pwd = os.getcwd()
        self._execute_pwd = os.path.abspath(sys.argv[0])

def get_files(dir: str) -> List[str]:
    """Return filenames of directory dir, including files in
    sub directories
    """
    ret = []
    for root, dirs, files in os.walk(dir):
        for name in dirs:
            ret.extend(get_files(os.path.join(root, name)))
        for name in files:
            ret.append(os.path.join(root, name))
    return ret


def sequence(f, lst: list) -> list:
    """Return the result of function f applied to every entry of lst
    """
    ret = []
    for ele in lst:
        ret.append(f(ele))
    return ret

def calc_median(data: list) -> float:
    """Return the median value of data,
    return 0.0 if data is empty

    Precondition: data is a list with numerical value
    """
    if len(data) == 0:
        return 0.0
    py = copy.copy(data)
    py.sort()
    if len(py) % 2 == 1:
        return float(py[len(py) / 2])
    return (py[len(py) // 2] + py[len(py) // 2 - 1]) / 2

def calc_mean(data: list) -> float:
    """Return the mean value of data,
    return 0.0 of data is empty
    """
    if len(data) == 0:
        return 0.0
    acc = 0.0
    for n in data:
        acc += n
    return acc / len(data)


def calc_q1(data: list) -> float:
    """Return the value of q1 of data

    Precondition: data is not empty
    values of data are numerical
    """
    py = copy.copy(data)
    py.sort()
    return py[round(len(py) / 4)]


def calc_q3(data: list) -> float:
    """Return the value of q3 of data

    Precondition: data is not empty
    values of data are numerical
    """
    py = copy.copy(data)
    py.sort()
    return py[len(py) - 1 - round(len(py) / 4)]


def calc_iqr(data: list) -> float:
    """Return the value of iqr of data

    Precondition: data is not empty
    values of data are numerical
    """
    return calc_q3(data) - calc_q1(data)

def calc_max(data: list) -> float:
    """Return the value of max of data

    Precondition: data is not empty
    values of data are numerical
    """
    acc = data[0]
    for n in data:
        if n > acc:
            acc = n
    return float(acc)

def calc_min(data: list) -> float:
    """Return the value of min of data

    Precondition: data is not empty
    values of data are numerical
    """
    acc = data[0]
    for n in data:
        if n < acc:
            acc = n
    return float(acc)

def calc_standard_deviation(data: list) -> float:
    """Return the standard deviation of data

    Precondition: items in data is greater than 1
    values of data are numerical
    """
    mean = calc_mean(data)
    acc = 0.0
    for n in data:
        acc += (n - mean) ** 2
    acc /= len(data) - 1
    return math.sqrt(acc)