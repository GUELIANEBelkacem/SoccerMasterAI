from pinkertons import *
from pinkertons.Simu import GoalSearch
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*
import pylab


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Attaquant", AttaquantStrategy())  # Random strategy
#team1.add("Defenceur",DefonceurStrategy())
#team2.add("Fonceur", AttaquantStrategy())   # Static strategy
team2.add("Defenceur",DefonceurStrategy())# Static strategy

# Create a match
simu = Simulation(team1, team2)
show_simu(simu)

#g=GoalSearch(strategy=DefonceurStrategy(),params={"strength": pylab.frange(0.4,0.6,0.02)})
#g.start()
"""
print(g.get_res())
print("\n\n\n")
print(g.get_best())
"""
# Simulate and display the match


#0.52
#0.50