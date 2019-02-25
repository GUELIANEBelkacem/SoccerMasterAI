#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:21:37 2019

@author: 3804546
"""

from .random_strategy import AttaquantStrategy, DefonceurStrategy, FonceurStrategy
from soccersimulator import SoccerTeam

def get_team(nb_players):
    team = SoccerTeam(name ="pinkertons" )
    if nb_players == 1:
        team.add ( "Player 1", AttaquantStrategy())
    if nb_players == 2:
        team.add( "Player 1" , AttaquantStrategy())
        team.add("Player 2", DefonceurStrategy())
    return team
