from typing import List
import toss
import utils

class rep:
    _meta = None
    def __init__(self):
        self._meta = []
    
    def append(self, ele: dict, file=None) -> None:
        self._meta.append(ele)
        if file is not None:
            toss_ins = toss.toss()
            self._meta.append(toss_ins.analyze_file(file))
    
    def extend(self, lst: List[dict], dir=None) -> None:
        # self._meta.extend(lst)
        if dir is not None:
            files = utils.get_files(dir)
            for file in files:
                toss_ins = toss.toss()
                self._meta.append(toss_ins.analyze_file(file))
    
    def count(self) -> int:
        return len(self._meta)

    def filter(self, category=None, duration=None,
                    map=None, version=None, player=None,
                    team=None, winner=None, date=None):
        ret = rep()
        for ele in self._meta:
            if category is not None:
                if not category(ele["category"]):
                    continue
            if duration is not None:
                if not duration(ele["duration"]):
                    continue
            if map is not None:
                if not map(ele["map"]):
                    continue
            if version is not None:
                if not version(ele["version"]):
                    continue
            if player is not None:
                if not player(ele["player"]):
                    continue
            if team is not None:
                if not team(ele["team"]):
                    continue
            if winner is not None:
                if not winner(ele["winner"]):
                    continue
            if date is not None:
                if not date(ele["date"]):
                    continue
            ret.append(ele)
        return ret
    
    def select(self, *args: str) -> List[dict]:
        ret = []
        for ele in self._meta:
            line = dict()
            for arg in args:
                line[arg] = ele[arg]
            ret.append(line)
        return ret
