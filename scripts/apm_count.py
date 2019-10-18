import sys
sys.path.append("..")

import toss
import rep
import seaborn
import utils
from sc2reader.events import *

replays = rep.rep()
replays.extend(dir="../rep")

NeoClear = "http://us.battle.net/sc2/en/profile/10455330/1/llllllllllll/"

def fff(reps):
    cnt = 0
    for rp in reps:
        for e in rp["events"]:
            if (isinstance(e, CommandEvent) or
                isinstance(e, SelectionEvent) or
                isinstance(e, ControlGroupEvent)):
                cnt += 1
        print(cnt * 60 // rp["duration"])

def each(reps):
    ret = []
    for rp in reps:
        for player in rp["player"]:
            if (player.url != NeoClear):
                continue
            cnt = 0
            for e in player.events:
                # if (isinstance(e, CommandEvent) or
                #     isinstance(e, SelectionEvent) or
                #     isinstance(e, ControlGroupEvent)):
                #     cnt += 1
                if (isinstance(e, GameEvent) and
                    not isinstance(e, GameStartEvent) and
                    not isinstance(e, PlayerLeaveEvent) and
                    not isinstance(e, UserOptionsEvent) and
                    not isinstance(e, CameraEvent)):
                    cnt += 1
            ret.append(cnt * 60 // rp["duration"])
            # print(player.name + ":", cnt * 60 // rp["duration"])
    return ret

# replays.apply(fff)
apms = replays.apply(each)
# print(events)
# print(e)
# print(e.frame)

seaborn.distplot(apms)