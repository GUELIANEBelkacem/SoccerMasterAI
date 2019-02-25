"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*
from tools import*
from Simu import*
import math
from action import*

class DefonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defonceur")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        a=Vector2D(1,1)
        b=0
        c=Vector2D(1,1)
        d=Vector2D(0,45)
        e=0
        f=Vector2D(0,45)
        f=d-state.ball.position
        
        e=0.07*((f.x*f.x+f.y*f.y)**0.05)
        a=state.ball.position-state.player_state(2,0).position
        b=a.x*a.x+a.y*a.y
        c=e*(d-state.ball.position)
        
        
        
        if (b<2.7225):
            return   SoccerAction(2*a,c)
        else:
            return SoccerAction(2*a,Vector2D(0,0))
    

        c=Vector2D(1,1)
        d=Vector2D(0,45)
        e=Vector2D(150,45)
        f=Vector2D(150,45)
        g=0
     
        e=state.ball.position-state.player_state(1,1).position
        f=a=state.player_state(1,1).position-state.player_state(1,0).position
        g=e.x*e.x+e.y*e.y
        a=state.player_state(1,1).position-state.player_state(2,0).position
        b=a.x*a.x+a.y*a.y
        c=d-state.ball.position
        
        
        
        if (b<3000 and g<3000):
            return   SoccerAction(e,f)
        else:
            return SoccerAction(d-state.player_state(1,1).position,Vector2D(0,0))
        
class DefonceurStrategyother(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defonceur")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        a=Vector2D(1,1)
        b=0
        c=Vector2D(1,1)
        d=Vector2D(150,45)
        e=Vector2D(150,45)
        f=Vector2D(150,45)
        g=0
     
        e=state.ball.position-state.player_state(2,1).position
        f=a=state.player_state(2,1).position-state.player_state(2,0).position
        g=e.x*e.x+e.y*e.y
        a=state.player_state(2,1).position-state.player_state(1,0).position
        b=a.x*a.x+a.y*a.y
        c=d-state.ball.position
        
        
        
        if (b<3000 and g<3000):
            return   SoccerAction(e,f)
        else:
            return SoccerAction(d-state.player_state(2,1).position,Vector2D(0,0))
        
class FonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
        
        return(m.to_ball()+sh.to_goal())

class FonceurStrategyother(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state,id_team,id_player)
        m=Move(s)
        sh=Shoot(s)
        
        return m.to_ball()+sh.to_goal()

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("fonceur", FonceurStrategy())
team1.add("Defonceur", DefonceurStrategy())  # Random strategy
team2.add("fonceur", FonceurStrategyother()) 
team2.add("Defonceur", DefonceurStrategyother())  # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
"""
