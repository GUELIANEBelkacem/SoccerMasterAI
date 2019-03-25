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
    hoha=0
    hoha1=0
    hoha2=0
    hoha3=0
    hoha4=0
    runorhit=0
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
                li=[(self.state.player_state(joueur[0], joueur[1]).position.y),joueur[1]]
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
                li=[(self.state.player_state(joueur[0], joueur[1]).position.y),joueur[1]]
                l.append(li)
                
        l.sort(key=lambda l:l[0], reverse=True)
        l.pop()
        l.pop()
        return l
    @property 
    def betweend(self):
        if(SuperState.hoha==1):
            l=self.dtwod
            SuperState.hoha1=l[1][1]
            SuperState.hoha2=l[0][1]
            a=self.state.player_state(((self.id_team%2)+1), SuperState.hoha1).position+(self.state.player_state(((self.id_team%2)+1),SuperState.hoha2).position-self.state.player_state(((self.id_team%2)+1), SuperState.hoha1).position)/2
            SuperState.hoha=0
            return a
        else:
            if(self.ball.x==GAME_WIDTH/2)and(self.ball.y==GAME_HEIGHT/2):
                l=self.dtwod
                SuperState.hoha1=l[1][1]
                SuperState.hoha2=l[0][1]
                a=self.state.player_state(((self.id_team%2)+1), SuperState.hoha1).position+(self.state.player_state(((self.id_team%2)+1),SuperState.hoha2).position-self.state.player_state(((self.id_team%2)+1), SuperState.hoha1).position)/2
                return a
            else:
                a=self.state.player_state(((self.id_team%2)+1), SuperState.hoha1).position+(self.state.player_state(((self.id_team%2)+1),SuperState.hoha2).position-self.state.player_state(((self.id_team%2)+1), SuperState.hoha1).position)/2
                return a
            
    
    @property 
    def betweeng(self):
        '''
        print(SuperState.hoha)
        print(SuperState.hoha1)
        print(SuperState.hoha2)
        print(SuperState.hoha3)
        print(SuperState.hoha4)
        '''
        if(SuperState.hoha==1):
            l=self.dtwog
            SuperState.hoha3=l[1][1]
            SuperState.hoha4=l[0][1]
            a=self.state.player_state(((self.id_team%2)+1), SuperState.hoha3).position+(self.state.player_state(((self.id_team%2)+1),SuperState.hoha4).position-self.state.player_state(((self.id_team%2)+1), SuperState.hoha3).position)/2
            SuperState.hoha=0
            
            return a
        
        else:
            if(self.ball.x==GAME_WIDTH/2)and(self.ball.y==GAME_HEIGHT/2):
                l=self.dtwog
                SuperState.hoha3=l[1][1]
                SuperState.hoha4=l[0][1]
                a=self.state.player_state(((self.id_team%2)+1), SuperState.hoha3).position+(self.state.player_state(((self.id_team%2)+1),SuperState.hoha4).position-self.state.player_state(((self.id_team%2)+1), SuperState.hoha3).position)/2
                return a
            else:
                a=self.state.player_state(((self.id_team%2)+1), SuperState.hoha3).position+(self.state.player_state(((self.id_team%2)+1),SuperState.hoha4).position-self.state.player_state(((self.id_team%2)+1), SuperState.hoha3).position)/2
                return a

    def ang(self, v1, v2):
        a=math.acos((v1.x*v2.x+v1.y*v2.y)/abs(v1.norm*v2.norm))
        return a

    
    @property 
    def shouldipass(self):
        l=[]
        a=False
        #0.31
        if(self.dgoal>GAME_WIDTH*0.31):
            for joueur in self.state.players:
                if(joueur[0]==((self.id_team%2)+1)):
                    l.append(self.state.player_state(joueur[0], joueur[1]).position)
            for e in l:
                tic=e-self.player
                toc=self.poplayerfr-self.player
                if(self.ang(tic,toc)>1):
                    a=True
        return a
    
    @property 
    def amid(self):
        a=False
        if(self.dball<20):
            a=True
        
        return a
    
    @property 
    def amig(self):
        a=False
        if(self.dball<20):
            a=True
        
        return a
    
    @property
    def closefriend(self):
        a=self.poplayerfr
        l=[]
        ll=[]
        for joueur in self.state.players:
            if(joueur[0]==self.id_team and joueur[1]!=self.id_player):
                if(abs((self.goal-self.player).x)>abs((self.goal-self.state.player_state(joueur[0], joueur[1]).position).x)):
                    l.append(self.state.player_state(joueur[0], joueur[1]).position)
        
        for joueur in self.state.players:
            if(joueur[0]==((self.id_team%2)+1)):
                if(abs((self.goal-self.player).x)>abs((self.goal-self.state.player_state(joueur[0], joueur[1]).position).x)):
                    ll.append(self.state.player_state(joueur[0], joueur[1]).position)
                
                
    
        if(len(l)==0):
            if(len(ll)<2):
                SuperState.runorhit=1
                return a
            else:
                SuperState.runorhit=1
                return a
        else:
            SuperState.runorhit=0
            a=l[0]
            for e in l:
                if (abs((self.goal-a).x)<abs((self.goal-e).x)):
                    a=e
            return a        
    @property    
    def hitorrun(self):
 a=self.poplayerfr
        l=[]
        ll=[]
        for joueur in self.state.players:
            if(joueur[0]==self.id_team and joueur[1]!=self.id_player):
                if(abs((self.goal-self.player).x)>abs((self.goal-self.state.player_state(joueur[0], joueur[1]).position).x)):
                    l.append(self.state.player_state(joueur[0], joueur[1]).position)
        
        for joueur in self.state.players:
            if(joueur[0]==((self.id_team%2)+1)):
                if(abs((self.goal-self.player).x)>abs((self.goal-self.state.player_state(joueur[0], joueur[1]).position).x)):
                    ll.append(self.state.player_state(joueur[0], joueur[1]).position)
        
        if(len(l)==0):
                return 1
        else:
            return 0        
            
        
        
        

'''    
    @property
    def anticiperx(self):
        return abs(self.my_goal.x-GAME_WIDTH*3/8)
                            if (abs((self.goal-self.player).x)<abs((self.goal-a).x)):
'''        
'''    
    @property
    def cangle(self):
        if abs((self.goal-self.player).y)<1:
            return ((self.goal-self.player).x+200)/40
        else:
            return abs(((self.goal-self.player).x+200)/((self.goal-self.player).y**0.1))/40
'''       