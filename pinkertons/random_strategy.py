# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*
from .tools import*
from .Simu import*
import math

class FonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state,id_team,id_player)
        if s.dball<PLAYER_RADIUS+BALL_RADIUS:
            return SoccerAction(s.ball-s.player,s.goal-s.player)
        else:
            return SoccerAction(s.ball-s.player,s.goal-s.player)
        
class AttaquantStrategy(Strategy):
    def __init__(self,strength=5.1):
        Strategy.__init__(self, "Attaquant")
        self.strength=strength

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state,id_team,id_player)
       


        if s.dball<PLAYER_RADIUS+BALL_RADIUS:
                
                return SoccerAction(s.ball-s.player-s.vball*10,(s.goal-s.player).normalize()*self.strength*s.alpha)
        else:
                return SoccerAction(s.ball+s.vball*10-s.player,0)
'''
       if(s.dgoal<GAME_WIDTH/1.2):   
    if s.dball<PLAYER_RADIUS+BALL_RADIUS:
        return SoccerAction(s.ball-s.player-s.vball*10,(s.goal-s.player).normalize())
    else:
        return SoccerAction(s.ball+s.vball*10-s.player,0)
else:
'''

class DefonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defonceur")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state,id_team,id_player)
        if(s.dball<GAME_WIDTH/2)and(s.dplayer<GAME_WIDTH/2+30)and((s.goal-s.ball).norm>GAME_WIDTH/2):
            if s.dball<PLAYER_RADIUS+BALL_RADIUS:
                return SoccerAction(s.ball-s.player-s.vball*10,(s.goal-s.player).normalize()*2)
            else:
                return SoccerAction(s.ball+s.vball*10-s.player,0)
        else:
            return SoccerAction(Vector2D(abs(s.goal.x-GAME_WIDTH+10)-s.player.x,s.goal.y-s.player.y),0)
        