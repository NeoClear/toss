from rep import *

ins = rep()
ins.extend([], "rep/")
ins.count()

def cate(s: str):
    return s == 'Ladder'

def dura(i: int):
    return i < 360

def mp(s: str):
    return "Eph" in s

def ver(v: str):
    print(v)
    return True

def play(p):
    """
    p is player type
    """
    for player in p:
        print(player.name, player.pick_race, player.play_race,
              player.highest_league, player.is_human,
              player.is_observer, player.is_referee,
              player.result, player.team, player.url)
              
              
        #print(dir(player))
    return True

# print(ins.filter(category=cate, duration=dura, map=mp, version=ver, player=play).count())

def pvz(players) -> bool:
    if len(players) != 2:
        return False
    cnt = 0
    flag = False
    for player in players:
        if player.play_race == "Protoss":
            cnt |= 1
        elif player.play_race == "Zerg":
            cnt |= 2
        if player.name == "llllllllllll":
            flag = True
    return cnt == 3 and flag

def pvt(players) -> bool:
    if len(players) != 2:
        return False
    cnt = 0
    for player in players:
        if player.play_race == "Protoss":
            cnt |= 1
        elif player.play_race == "Terran":
            cnt |= 2
    return cnt == 3    

def tvz(players) -> bool:
    if len(players) != 2:
        return False
    cnt = 0
    for player in players:
        if player.play_race == "Zerg":
            cnt |= 1
        elif player.play_race == "Terran":
            cnt |= 2
    return cnt == 3    

def protoss_win(team) -> bool:
    if len(team.players) != 1:
        return False
    winner = team.players[0]
    return winner.play_race == "Protoss" and\
           winner.name == "llllllllllll"

print("winning rate of pvt is:",
      (ins.filter(player=pvt, winner=protoss_win)).count() /
       ins.filter(player=pvt).count())

def nuc(team) -> bool:
    if team is None:
        return False
    if len(team.players) != 1:
        return False
    winner = team.players[0]
    return winner.play_race == "Protoss" and\
           winner.name == "llllllllllll"

def nc(players) -> bool:
    for player in players:
        if player.name == "llllllllllll" and\
           player.play_race == "Protoss":
            return True
    return False

def is_ladder(s: str) -> bool:
    return s == "Ladder"

print("winning rate of NeoClear on Ladder using Protoss is:",
      (ins.filter(category=is_ladder, winner=nuc).count() /
       ins.filter(category=is_ladder, player=nc).count()))

print("There are games longer than 10 min:",
      ins.filter(duration=lambda x: x > 600).count() /
      ins.count())

print(ins.filter(duration=lambda x: x > 1200).select("player"))