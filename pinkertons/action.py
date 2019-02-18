from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*
from tools import*
from Simu import*
import math

class Move(object):
    def __init__(self,superstate):
        self.superstate=superstate
        
        
    def to_ball(self):
        return SoccerAction(acceleration=self.superstate.ball-self.superstate.player)
    
    
class Shoot(object):
    def __init__(self,superstate):
        self.superstate=superstate
        
    def to_goal(self):
        if self.superstate.dball<PLAYER_RADIUS+BALL_RADIUS:
            return SoccerAction(shoot=self.superstate.goal-self.superstate.player)
        else:
            return SoccerAction()