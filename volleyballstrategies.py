from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator import VolleySimulation, volley_show_simu
from soccersimulator.settings import*
from pinkertons.tools import*
from pinkertons.Simu import*
from pinkertons.action import*
import math



class Echauffement(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Echauffement")

    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
        return m.to_ball()+sh.to_enemy()
        
    
class Attaque(Strategy):
    def __init__(self,forcet=1):
        Strategy.__init__(self, "Attaque")
        self.forcet=forcet

    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
        
        return m.to_ball()+sh.to_attaque()

