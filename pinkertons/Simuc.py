from sklearn.model_selection import ParameterGrid
import random
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*
from .tools import*
from sklearn.model_selection import ParameterGrid

class GoalSearchc(object):
    def __init__(self,strategy,params,simu=None, trials=2,max_steps=1000000,max_round_step=40,nogen=2,cpt_gen=0,l=[]):
        self.strategy=strategy
        self.params=params.copy()
        self.simu=simu
        self.trials=trials
        self.max_steps=max_steps
        self.max_round_step=max_round_step
        self.nogen=nogen
        self.cpt_gen=cpt_gen
        self.l=l
    
    def start(self,show=True):
        if not self.simu:
            team1 = SoccerTeam("Team 1")
            team2 = SoccerTeam("Team 2")
            team1.add(self.strategy.name,self.strategy)
            team2.add(Strategy().name , Strategy())
            self.simu = Simulation(team1, team2 , max_steps = self.max_steps )
        self.simu.listeners += self
        if show :
            show_simu(self.simu)
        else :
            self.simu.start()
            
    def begin_match(self, team1, team2, state):

        self.last_step = 0 # Step of the last round
        self.criterion = 0 # Criterion to maximize ( here , number of goals )
        self.cpt_trials = 0 # Counter for trials

            
        for i in range(8):
            a=random.random()
            b=random.random()
            if(b<0.5):
                b=-1
            else:
                b=1
            if(a<0.5):
              a=-1
            else:
              a=1
            dic={
                    "forcet":1+random.random()*0.1*a,
                    "dpos":5/8*GAME_WIDTH+random.random()*0.1*b
            }
            self.l.append(dic)
                      
        self.param_grid = iter(self.l) 
    
        self.cur_param = next(self.param_grid, None ) # Current parameter
        if self.cur_param is None :
            raise ValueError("no parameter given")
        self.res = dict() # Dictionary of results
    def begin_round ( self , team1 , team2 , state ):
        ball = Vector2D.create_random(low=-30,high=30)
        ball.x+=GAME_WIDTH*8/10
        ball.y+=GAME_HEIGHT/2
        # Player and ball postion ( random )
        self.simu.state.states[(1 , 0)].position = ball.copy() # Player position
        self.simu.state.states[(1 , 0)].vitesse = Vector2D() # Player accelerati
        self.simu.state.ball.position = ball.copy() # Ball position
        self.last_step = self.simu.step
        # Last step of the game
        # Set the current value for the current parameters
        for key , value in self.cur_param.items():
            setattr( self.strategy , key , value )
            
    def end_round(self, team1, team2, state):
        # A round ends when there is a goal of if max step is achieved
        if state.goal > 0:
            self.criterion += 1 # Increment criterion
        self.cpt_trials += 1    # Increment number of trials
        print(self.cur_param,end = "  " )
        print ( " Crit :   {}      Cpt :   {} " . format(self.criterion,self.cpt_trials))
        if self.cpt_trials >= self.trials :  # Save the result
            self.res[tuple(self.cur_param.items())] = self.criterion*1./self.trials
            # Reset parameters
            self.criterion = 0
            self.cpt_trials = 0
            # Next parameter value
            self.cur_param = next(self.param_grid , None )
            if self.cur_param is None :
            
                if(self.cpt_gen==self.nogen-1):
                    self.simu.end_match ()
                else:
                    self.cpt_gen+=1
                    mr=0
                    nr=0
                    for t in self.res:
                        mr+=self.res[t]
                        nr+=1
                    mr=mr/nr
                    print(self.res)
                    for t in self.l:
                        key = tuple(t.items())
                        if key in self.res:
                             if (self.res[tuple(t.items())]<mr):
                                 self.l.remove(t)
                    for i in range(8-len(self.l)):
                        a=random.random()
                        b=random.random()
                        if(b<0.5):
                            b=-1
                        else:
                            b=1
                        if(a<0.5):
                            a=-1
                        else:
                            a=1
                        dic={
                                "forcet":2+random.random()*0.1*a,
                                "dpos":5/8+random.random()*0.1*b
                        }
                        self.l.append(dic)
                    self.param_grid = iter(self.l) 
                    self.cur_param = next ( self.param_grid , None )
        
    def update_round ( self , team1 , team2 , state ):
        # Stop the round if it is too long
        if state.step>self.last_step+self.max_round_step:
            self.simu.end_round()

    def get_res (self):
        return self.res

    def get_best(self):
        return max(self.res, key=self.res.get)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            