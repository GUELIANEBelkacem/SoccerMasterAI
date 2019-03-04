from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*
from .tools import*
from .Simu import*
import math

class Move(object):
    def __init__(self,superstate):
        self.superstate=superstate
        
        
    def to_ball(self):
        return SoccerAction(acceleration=(self.superstate.ball-self.superstate.player+self.superstate.anticiper)*999)
    
    def to_home(self):
        return SoccerAction(acceleration=(Vector2D(self.superstate.anticiperx-self.superstate.player.x,self.superstate.anticipery-self.superstate.player.y))*999)
    
    
class Shoot(object):
    def __init__(self,superstate):
        self.superstate=superstate
        
    def to_goal(self):
        strength=0.032
        if self.superstate.dball<PLAYER_RADIUS+BALL_RADIUS:
            return SoccerAction(shoot=(self.superstate.goal-self.superstate.player).normalize()*strength*self.superstate.alpha)
        else:
            return SoccerAction()
    
    def to_pass(self):
        return SoccerAction(shoot = self.superstate.player-self.superstate.poplayerfr)
    
        
'''
if s.dball<PLAYER_RADIUS+BALL_RADIUS:
                
                return SoccerAction(s.ball-s.player-s.vball*10,(s.goal-s.player).normalize()*self.strength*s.alpha)
        else:
                return SoccerAction(s.ball+s.vball*10-s.player,0)
                
'''