#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:21:37 2019

@author: 3804546
"""

from .random_strategy import AttaquantStrategy, DefonceurStrategy, FonceurStrategy,CoteStrategyd, CoteStrategyg, StaticStrategy, PassStrategy, AttaquantStrategy4, DefonceurStrategy4,CoteStrategyd4, CoteStrategyg4, AttaquantStrategy5,CoteStrategyd5, CoteStrategyg5, DefonceurStrategy5
from soccersimulator import SoccerTeam
from .QLearning import *
from .QStrategy import *

def get_team(nb_players):
    team = SoccerTeam(name ="pinkertons" )
    if nb_players == 1:
        team.add ( "Player 1", AttaquantStrategy())
    if nb_players == 2:
        team.add( "Player 1" , AttaquantStrategy())
        team.add("Player 2", DefonceurStrategy())
    if nb_players == 4:
        team.add("Player 2", DefonceurStrategy5())
        team.add("Player 4", CoteStrategy5())
        team.add("Player 3", CoteStrategy5())
        team.add( "Player 1" , AttaquantStrategy5())
    return team
