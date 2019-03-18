#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:31:34 2019

@author: 3804546
"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import*
import numpy as np
import numpy.linalg as la
import math

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
    def my_goal(self):
        return Vector2D(((self.id_team+1)%2)*GAME_WIDTH, GAME_HEIGHT/2)
    @property
    def dgoal(self):
        return (self.goal-self.player).norm
    @property
    def dball(self):
        return (self.ball-self.player).norm
    @property
    def dplayeren(self):
        res=GAME_WIDTH
        for joueur in self.state.players:
            if(joueur[0]==((self.id_team%2)+1)):
                if((self.state.player_state(joueur[0],joueur[1]).position-self.player).norm<res):
                    res=(self.state.player_state(joueur[0],joueur[1]).position-self.player).norm
        return res
    
    @property
    def dplayerfr(self):
        res=GAME_WIDTH
        for joueur in self.state.players:
            if(joueur[0]==(self.id_team) and joueur[1]!=self.id_player):
                if((self.state.player_state(joueur[0],joueur[1]).position-self.player).norm<res):
                    res=(self.state.player_state(joueur[0],joueur[1]).position-self.player).norm
        return res
    
    @property
    def idplayerfr(self):
        res=GAME_WIDTH
        a=self.id_player
        for joueur in self.state.players:
            if(joueur[0]==(self.id_team) and joueur[1]!=self.id_player):
                if((self.state.player_state(joueur[0],joueur[1]).position-self.player).norm<res):
                    res=(self.state.player_state(joueur[0],joueur[1]).position-self.player).norm
                    a=joueur[1]
        return a
    
    @property
    def idplayeren(self):
        res=GAME_WIDTH
        a=self.id_player
        for joueur in self.state.players:
            if(joueur[0]==((self.id_team%2)+1)):
                if((self.state.player_state(joueur[0],joueur[1]).position-self.player).norm<res):
                    res=(self.state.player_state(joueur[0],joueur[1]).position-self.player).norm
                    a=joueur[1]
        return a
    
    @property
    def isplayerfr(self):
        a=False
        for joueur in self.state.players:
            if(joueur[0]==(self.id_team) and joueur[1]!=self.id_player):
                if((self.state.player_state(joueur[0],joueur[1]).position-self.state.ball.position).norm<(PLAYER_RADIUS+BALL_RADIUS)*2):
                    a=True
        return a
    
    @property
    def poplayerfr(self):
        return self.state.player_state(self.id_team, self.idplayerfr).position
    
    @property
    def poplayeren(self):
        return self.state.player_state(((self.id_team%2)+1), self.idplayeren).position
    
    @property
    def dballen(self):
        return (self.state.player_state(((self.id_team%2)+1), self.idplayeren).position-self.ball).norm
        
    

    @property
    def alpha(self):
        a=abs(((self.goal-self.player).x)*2/(self.dgoal+1))+100
        return a
    @property 
    def pass_alpha(self):
        a=self.dplayerfr*3.5
        return a+10
    
    @property
    def anticiper(self):
        return self.dball*self.vball*(0.3)
    
    @property 
    def anticipery(self):
        a=(self.my_goal.y-self.ball.y)/(self.my_goal.x-self.ball.x+1)
        b=self.my_goal.y-a*self.my_goal.x
        return a*self.anticiperx+b
    
    @property
    def anticiperx(self):
        return self.my_goal.x-(self.my_goal.x-self.poplayeren.x)*0.6
    
    
#start of 3 and 4
        
    @property 
    def our_ball(self):
        a=True
        lus=[]
        lthem=[]
        minus=0
        minthem=0
        
        for joueur in self.state.players:
            if(joueur[0]==(self.id_team)):
                lus.append((self.state.player_state(joueur[0], joueur[1]).position-self.ball).norm)
            else:
                lthem.append((self.state.player_state(joueur[0], joueur[1]).position-self.ball).norm)
        minus=min(lus)
        minthem=min(lthem)
        if(minus>minthem):
            a=False


        return a
        
    
    @property 
    def dtwod(self):
        l=[]
        for joueur in self.state.players:
            if(joueur[0]==((self.id_team%2)+1)):
                li=[self.state.player_state(joueur[0], joueur[1]).position.y,joueur[1]]
                l.append(li)
                
        l.sort(key=lambda l:l[0])
        l.pop()
        l.pop()
        return l
    
    
    @property 
    def dtwog(self):
        l=[]
        for joueur in self.state.players:
            if(joueur[0]==((self.id_team%2)+1)):
                li=[self.state.player_state(joueur[0], joueur[1]).position.y,joueur[1]]
                l.append(li)
                
        l.sort(key=lambda l:l[0], reverse=True)
        l.pop()
        l.pop()
        return l
    @property 
    def betweend(self):
        l=self.dtwod
        a=(self.state.player_state(((self.id_team%2)+1),l[0][1]).position-self.state.player_state(((self.id_team%2)+1), l[1][1]).position)/2
        return a
    
    @property 
    def betweeng(self):
        l=self.dtwog
        a=(self.state.player_state(((self.id_team%2)+1), l[0][1]).position-self.state.player_state(((self.id_team%2)+1), l[1][1]).position)/2
        return a
    

    def ang(self, v1, v2):
        a=math.acos((v1.x*v2.x+v1.y*v2.y)/abs(v1.norm*v2.norm))
        return a

    
    @property 
    def shouldipass(self):
        l=[]
        a=True
        if(self.dgoal>GAME_WIDTH*0.25):
            for joueur in self.state.players:
                if(joueur[0]==((self.id_team%2)+1)):
                    l.append(self.state.player_state(joueur[0], joueur[1]).position)
            for e in l:
                tic=e-self.player
                toc=self.poplayerfr-self.player
                if(self.ang(tic,toc)<0.5236):
                    a=False
        return a
    
    @property 
    def ami(self):
        a=False
        if(self.dball<PLAYER_RADIUS+BALL_RADIUS+20):
            a=True
        
        return a
            
            
        
        

'''    
    @property
    def anticiperx(self):
        return abs(self.my_goal.x-GAME_WIDTH*3/8)
'''        
'''    
    @property
    def cangle(self):
        if abs((self.goal-self.player).y)<1:
            return ((self.goal-self.player).x+200)/40
        else:
            return abs(((self.goal-self.player).x+200)/((self.goal-self.player).y**0.1))/40
'''       