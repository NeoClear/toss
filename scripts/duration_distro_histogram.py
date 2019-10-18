#!/usr/bin/env python

from __future__ import absolute_import

import sys
sys.path.append("..")

import toss
import rep
import seaborn
import utils

replays = rep.rep()

replays.extend([], "../rep/")

distro = utils.sequence(lambda x: x["duration"], replays.select("duration"))

# print(distro)
seaborn.distplot(distro)
