from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*
import numpy as np
import numpy.linalg as la
import math
from pinkertons import *
import pickle as pkl

# Strategy
QTestStrategy = QStrategy()
QTestStrategy.add("defance",DefonceurStrategy())
QTestStrategy.add("attaque",FonceurStrategy())
#QTestStrategy.add("wing d",CoteStrategyd())
#QTestStrategy.add("wing g",CoteStrategyg())

'''
QTestStrategy = QStrategy.QStrategy()
QTestStrategy.add("right",SimpleStrategy(shoot_right,""))
QTestStrategy.add("left",SimpleStrategy(shoot_left,""))
QTestStrategy.add("up",SimpleStrategy(shoot_up,""))
QTestStrategy.add("down",SimpleStrategy(shoot_down,""))
'''
# Learning
#expe = QLearning(strategy = QTestStrategy,monte_carlo=False )
#expe.start(fps =1500)
#
#with open( "qstrategy.pkl","wb") as fo:
#    QTestStrategy.qtable = expe.qtable
#    print('Q TABLE', expe.qtable)
#    pkl.dump(QTestStrategy,fo)
# Test
with open("qstrategy.pkl","rb") as fi:
    QStrategy = pkl.load(fi)

    # Simulate and display the match
    #simu = RandomPos(QStrategy)
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")
team1.add("Attaquant", QStrategy)
team2.add("wing g", Strategy())  # Random strategy
simu = Simulation(team1, team2)
#simu.start()
show_simu(simu)
expe.get_res()
    
    
    





























