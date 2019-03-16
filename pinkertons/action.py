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
        
    def to_goal(self,forcet):
        forcet=1
        strength=0.032
        if self.superstate.dball<PLAYER_RADIUS+BALL_RADIUS:
            return SoccerAction(shoot=(self.superstate.goal-self.superstate.player).normalize()*strength*self.superstate.alpha*forcet)
        else:
            return SoccerAction()
    
    def to_pass(self):
        strength=0.032
        return SoccerAction(shoot = 1.25*Vector2D(((self.superstate.poplayerfr-self.superstate.player).normalize()*strength*self.superstate.pass_alpha).x,((self.superstate.poplayerfr-self.superstate.player).normalize()*strength*self.superstate.pass_alpha).y+((self.superstate.goal-self.superstate.player).normalize()*strength*self.superstate.alpha).y/4))
    
    def to_defend(self):
        strength=0.032
        return SoccerAction(shoot = 1.5*Vector2D(((self.superstate.goal-self.superstate.player+(self.superstate.poplayerfr-self.superstate.player)/3).normalize()*strength*self.superstate.alpha).x,((self.superstate.goal-self.superstate.player+(self.superstate.poplayerfr-self.superstate.player)/3).normalize()*strength*self.superstate.alpha).y))
        '''
        if(self.superstate.player.y>GAME_HEIGHT/2):
            return SoccerAction(shoot = 10*Vector2D(((self.superstate.goal-self.superstate.player).normalize()*strength*self.superstate.alpha).x,((self.superstate.goal-self.superstate.player).normalize()*strength*self.superstate.alpha).y+GAME_HEIGHT/100) )
        else:
            return SoccerAction(shoot = 10*Vector2D(((self.superstate.goal-self.superstate.player).normalize()*strength*self.superstate.alpha).x,((self.superstate.goal-self.superstate.player).normalize()*strength*self.superstate.alpha).y-GAME_HEIGHT/100) )
        -(self.superstate.poplayeren-self.superstate.poplayerfr).y*2
        '''    
        
'''
if s.dball<PLAYER_RADIUS+BALL_RADIUS:
                
                return SoccerAction(s.ball-s.player-s.vball*10,(s.goal-s.player).normalize()*self.strength*s.alpha)
        else:
                return SoccerAction(s.ball+s.vball*10-s.player,0)
                
'''