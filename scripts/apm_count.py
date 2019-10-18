import sys
sys.path.append("..")

import toss
import rep
import seaborn
import utils
from sc2reader.events import *

replays = rep.rep()
replays.append(file="../rep/Triton LE (3).SC2Replay")

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
    for rp in reps:
        for player in rp["player"]:
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
            print(player.name + ":", cnt * 60 // rp["duration"])

# replays.apply(fff)
replays.apply(each)
events = replays.select("events")[0]["events"]
# print(events)
e = events[1000]
# print(e)
print(dir(e))
# print(e.frame)
print(e.second)