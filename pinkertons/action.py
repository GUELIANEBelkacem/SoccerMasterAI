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
    def to_betweend(self):
        return SoccerAction(acceleration=(self.superstate.betweend-self.superstate.player)*999)
    def to_betweeng(self):
        return SoccerAction(acceleration=(self.superstate.betweeng-self.superstate.player)*999)
    
    
class Shoot(object):
    hoha=1
    def __init__(self,superstate):
        self.superstate=superstate
    def to_goal(self,forcet):

        forcet=1
        strength=0.032
        if (self.superstate.dball<PLAYER_RADIUS+BALL_RADIUS+1)and(Shoot.hoha==1):
            Shoot.hoha=0
            return SoccerAction(shoot=(self.superstate.goal-self.superstate.player).normalize()*strength*self.superstate.alpha*forcet)
        else:
            if (self.superstate.dball<PLAYER_RADIUS+BALL_RADIUS)and(Shoot.hoha==0):
                if(self.superstate.ball.x==GAME_WIDTH/2)and(self.superstate.ball.y==GAME_HEIGHT/2):
                    Shoot.hoha=1
                return SoccerAction(shoot=(self.superstate.goal-self.superstate.player).normalize()*strength*self.superstate.alpha*forcet)
            else:
                if(self.superstate.ball.x==GAME_WIDTH/2)and(self.superstate.ball.y==GAME_HEIGHT/2):
                    Shoot.hoha=1
                return SoccerAction()
        
    def to_pass(self):
        strength=0.032
        if (self.superstate.dball<PLAYER_RADIUS+BALL_RADIUS):
            print("1111111111111111111111111111")
            return SoccerAction(shoot = 3*Vector2D(((self.superstate.closefriend-self.superstate.player).normalize()*strength*self.superstate.pass_alpha).x,((self.superstate.closefriend-self.superstate.player).normalize()*strength*self.superstate.pass_alpha).y+((self.superstate.goal-self.superstate.player).normalize()*strength*self.superstate.alpha).y/4))
        else:
            return SoccerAction()
        
    def to_defend(self):
        strength=0.032
        if (self.superstate.dball<PLAYER_RADIUS+BALL_RADIUS):
            return SoccerAction(shoot = 1.5*Vector2D(((self.superstate.goal-self.superstate.player+(self.superstate.poplayerfr-self.superstate.player)/3).normalize()*strength*self.superstate.alpha).x,((self.superstate.goal-self.superstate.player+(self.superstate.poplayerfr-self.superstate.player)/3).normalize()*strength*self.superstate.alpha).y))
        else:
            return SoccerAction()
        
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