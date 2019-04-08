from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator import VolleySimulation, volley_show_simu
from soccersimulator.settings import*
from pinkertons.tools import*
from pinkertons.Simu import*
from pinkertons.action import*
from volleyballstrategies import Echauffement,Attaque,Defense,UnVsUn,Defense2,Attaque2,Attaque3
import math
from pinkertons.Simu import GoalSearch
from pinkertons.Simuc import GoalSearchc
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*
import pylab


g=GoalSearch(strategy=Attaque(),params={"force": pylab.frange(0.4,0.6,0.02)})
g.start()

print(g.get_res())
print("\n\n\n")
print(g.get_best())