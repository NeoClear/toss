import sys
sys.path.append("..")

import toss
import utils
import rep
import seaborn
import pandas

replays = rep.rep()

replays.extend([], "../rep/")

players = utils.sequence(lambda x: x["player"], replays.select("player"))

def play(players):
    ret = []
    for match in players:
        if len(match) != 2:
            continue
        cnt = 0
        for p in match:
            if p.play_race == "Terran":
                cnt |= 1
            if p.play_race == "Protoss":
                cnt |= 2
            if p.play_race == "Zerg":
                cnt |= 4
        if cnt == 1:
            ret.append("TvT")
        elif cnt == 2:
            ret.append("PvP")
        elif cnt == 3:
            ret.append("PvT")
        elif cnt == 4:
            ret.append("ZvZ")
        elif cnt == 5:
            ret.append("TvZ")
        elif cnt == 6:
            ret.append("PvZ")
    return ret

ans = play(players)
df = pandas.DataFrame(data={"Match Type": ans, "Base": [1] * len(ans)})
# print(df)

seaborn.barplot(x="Match Type", y="Base", data=df, estimator=lambda lst: len(lst))