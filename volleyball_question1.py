from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator import VolleySimulation, volley_show_simu
from soccersimulator.settings import*
from pinkertons.tools import*
from pinkertons.Simu import*
from pinkertons.action import*
from volleyballstrategies import Echauffement,Attaque
import math


team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")


team1.add("Player 1", Echauffement())  
team2.add("Player 2", Attaque())  


simu = VolleySimulation(team1, team2)


volley_show_simu(simu)
