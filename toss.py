#!/usr/bin/env python

import os
import sys
from typing import List
from sc2reader.factories import SC2Factory
from sc2reader.events import *
from utils import file
import utils

class toss:
    _file = None
    _replay = None
    _info = None

    def __init__(self):
        self._file = file()
        self._info = dict()

    def analyze_file(self, filename: str) -> dict:
        """Return replay data of file filename
        """
        sc2 = SC2Factory()
        self._replay = sc2.load_replay(filename)
        self._info["filename"] = self._replay.filename
        self._info["category"] = self._replay.category
        self._info["duration"] = self._replay.length.seconds
        self._info["map"] = self._replay.map_name
        self._info["version"] = self._replay.release_string
        self._info["player"] = self._replay.players
        self._info["team"] = self._replay.team
        self._info["winner"] = self._replay.winner
        self._info["date"] = self._replay.date
        self._info["events"] = self._replay.events
        # for team in self._replay.teams:
        #     for player in team:
        #         print(dir(player))
        # for team in self._replay.teams:
        #     for player in team:
        #         print(player.color)
        # event = self._replay.events
        # for e in event:
        #     if isinstance(e, GameStartEvent):
        #     print(e)
        return self._info

def run():
    if len(sys.argv) < 2:
        print("Not enough arguments")
        return
    command = sys.argv[1]
    args = sys.argv[2:]

    if "rep" in command:
        if len(args) == 0:
            f = file()
            files = utils.get_files(f.current_pwd)
            utils.print_info(files)
        else:
            utils.print_info(args)
        
    elif "dir" in command:
        if len(args) == 0:
            f = file()
            files = utils.get_files(f.current_pwd)
            utils.print_info(files)
        else:
            for dir in args: 
                files = utils.get_files(dir)
                utils.print_info(files)


# def test():
#     path = sys.argv[1]
#     sc2 = SC2Factory()
#     replay = sc2.load_replay(path)
#     print(replay)

if __name__ == "__main__":
    run()
