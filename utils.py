import os
import sys
from typing import List
import toss

l1 = {"filename", "category", "duration", "map", "team"}
l2 = {"filename", "category", "duration", "map", "team", "winner", "date"}
l3 = {"filename", "category", "duration", "map", "version", "team", "winner", "date", "frame"}

def print_info(paths: List[str], level=1) -> None:
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
    ret = []
    for root, dirs, files in os.walk(dir):
        for name in dirs:
            ret.extend(get_files(os.path.join(root, name)))
        for name in files:
            ret.append(os.path.join(root, name))
    return ret


def sequence(f, lst: list) -> list:
    ret = []
    for ele in lst:
        ret.append(f(ele))
    return ret