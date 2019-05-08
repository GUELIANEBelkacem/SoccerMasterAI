from pinkertons import *
from pinkertons.Simu import GoalSearch
from pinkertons.Simuc import GoalSearchc
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*
import pylab
'''
g=GoalSearchc(strategy=AttaquantStrategy(),params={"strength": pylab.frange(0.4,0.6,0.02)})
g.start()
'''

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")


# Add players
team1.add("Defenceur",DefonceurStrategy4())
team1.add("Attaquant", AttaquantStrategy())  # Random strategy
team1.add("wingd", CoteStrategyd4())   # Static strategy
team1.add("wingg",CoteStrategyg4())# Static strategy 

team2.add("Defenceur----",DefonceurStrategy5())# Static strategy
team2.add("wing g----",CoteStrategyg5())
team2.add("wing d----", CoteStrategyd5())   # Static strategy
team2.add("Fonceur4----", AttaquantStrategy5())   # Static strategy# Static strategy


# Create a match
simu = Simulation(team1, team2)
show_simu(simu)

'''
g=GoalSearch(strategy=AttaquantStrategy(),params={'avade': pylab.frange(0.1,1,0.01)})
g.start()

print(g.get_res())
print("\n\n\n")
print(g.get_best())
'''
# Simulate and display the match


#0.52
#0.50
