#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:31:34 2019

@author: 3804546
"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*

class SuperState(object):
    def __init__(self,state,id_team,id_player):
        self.state=state
        self.id_team=id_team
        self.id_player=id_player
    @property
    def ball(self):
        return self.state.ball.position
    @property
    def vball(self):
        return self.state.ball.vitesse
    @property
    def player(self):
        return self.state.player_state(self.id_team, self.id_player).position
    @property
    def goal(self):
        return Vector2D((self.id_team%2)*GAME_WIDTH, GAME_HEIGHT/2)
    @property
    def dgoal(self):
        return (self.goal-self.player).norm
    @property
    def dball(self):
        return (self.ball-self.player).norm
    @property
    def dplayer(self):
        res=GAME_WIDTH
        for joueur in self.state.players:
            if(joueur[0]==(self.id_team%2)+1):
                if((self.state.player_state(joueur[0],joueur[1]).position-self.player).norm<res):
                    res=(self.state.player_state(joueur[0],joueur[1]).position-self.player).norm
        return res
    