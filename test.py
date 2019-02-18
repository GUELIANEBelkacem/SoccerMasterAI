#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:29:36 2019

@author: 3804546
"""
from pinkertons import *
from pinkertons.Simu import GoalSearch
import pylab


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Attaquant", AttaquantStrategy())  # Random strategy
team1.add("Defenceur",DefonceurStrategy())
team2.add("Fonceur", AttaquantStrategy())   # Static strategy
team2.add("Defenceur",DefonceurStrategy())

# Create a match
#simu = Simulation(team1, team2)
g=GoalSearch(strategy=AttaquantStrategy(),params={"strength": pylab.frange(0.4,0.6,0.02)})
g.start()
print(g.get_res())
print("\n\n\n")
print(g.get_best())
# Simulate and display the match
#show_simu(simu)

#0.52
#0.50