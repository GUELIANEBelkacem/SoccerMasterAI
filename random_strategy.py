# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*
from tools import*
from Simu import*
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
    def __init__(self,strength=None):
        Strategy.__init__(self, "Attaquant")
        self.strength=strength

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state,id_team,id_player)
        if(s.dgoal<GAME_WIDTH/2):   
            if s.dball<PLAYER_RADIUS+BALL_RADIUS:
                return SoccerAction(s.ball-s.player-s.vball*10,(s.goal-s.player).normalize()*2)
            else:
                return SoccerAction(s.ball+s.vball*10-s.player,0)
        else:
            if s.dball<PLAYER_RADIUS+BALL_RADIUS:
                return SoccerAction(s.ball-s.player-s.vball*10,(s.goal-s.player).normalize()*self.strength)
            else:
                return SoccerAction(s.ball+s.vball*10-s.player,0)

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
        
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Attaquant", AttaquantStrategy())  # Random strategy
team1.add("Defenceur",DefonceurStrategy())
team2.add("Fonceur", FonceurStrategy())   # Static strategy
team2.add("Defenceur",DefonceurStrategy())

# Create a match
#simu = Simulation(team1, team2)
g=GoalSearch(strategy=AttaquantStrategy(),params={"strength": [1,2]})
g.start()
print(g.get_res())
print(g.get_best())
# Simulate and display the match
#show_simu(simu)

