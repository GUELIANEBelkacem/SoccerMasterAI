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
    tactic1=0
    tactic2=0
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
    def dgoaly(self):
        return abs((self.goal-self.player).y)
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
        a=(self.closefriend-self.player).norm*2.2+15
        return a
    
    @property
    def anticiper(self):
        return self.dball*self.vball*(0.3)
    #0.3
    
   
    def anticipertest(self,avade):
        a=avade*self.dball*self.vball
        return a
    
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
        if(len(l)==4):
            l.pop()
            l.pop()
        if(len(l)==3):
            l.pop()
        if(len(l)==1):
            l[1][0]=l[0][0]
            l[1][1]=l[0][1]
        return l
    
    
    @property 
    def dtwog(self):
        l=[]
        for joueur in self.state.players:
            if(joueur[0]==((self.id_team%2)+1)):
                li=[(self.state.player_state(joueur[0], joueur[1]).position.y),joueur[1]]
                l.append(li)
                
        l.sort(key=lambda l:l[0], reverse=True)
        if(len(l)==4):
            l.pop()
            l.pop()
        if(len(l)==3):
            l.pop()
        if(len(l)==1):
            l[1][0]=l[0][0]
            l[1][1]=l[0][1]
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
    def amitwod(self):
        a=False
        if(self.dball<0):
            a=True
        
        return a
    
    @property 
    def amitwog(self):
        a=False
        if(self.dball<0):
            a=True
        
        return a
    
    @property 
    def amid(self):
        a=False
        if((self.state.player_state(((self.id_team%2)+1), SuperState.hoha1).position+(self.state.player_state(((self.id_team%2)+1),SuperState.hoha2).position-self.state.player_state(((self.id_team%2)+1), SuperState.hoha1).position)/2-self.state.ball.position).norm < ((self.state.player_state(((self.id_team%2)+1),SuperState.hoha2).position-self.state.player_state(((self.id_team%2)+1), SuperState.hoha1).position)/2).norm + 5 ):
            a=True
        
        return a

    @property 
    def amig(self):
        a=False
        if((self.state.player_state(((self.id_team%2)+1), SuperState.hoha3).position+(self.state.player_state(((self.id_team%2)+1),SuperState.hoha4).position-self.state.player_state(((self.id_team%2)+1), SuperState.hoha3).position)/2-self.state.ball.position).norm < ((self.state.player_state(((self.id_team%2)+1),SuperState.hoha4).position-self.state.player_state(((self.id_team%2)+1), SuperState.hoha3).position)/2).norm + 5 ):
            a=True
        
        return a
    '''
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
    '''
    @property
    def closefriend(self):
        l=self.friend_list
        if(l.index([self.player,self.id_player,abs((self.player-self.goal).x)])+1>3):
            return l[2][0]
        else:
            return l[l.index([self.player,self.id_player,abs((self.player-self.goal).x)])+1][0]
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
                return True
        else:
            return False   
        
        
#strategy change
    
    @property    
    def friend_list(self):
        l=[]
   
        for joueur in self.state.players:
            if(joueur[0]==self.id_team ):
                    li=[self.state.player_state(joueur[0], joueur[1]).position,joueur[1],abs((self.state.player_state(joueur[0], joueur[1]).position-self.goal).x)]
                    l.append(li)
        l.sort(key=lambda l:l[2], reverse=True)
        return l
    

    @property    
    def enemy_list(self):  
        l=[]
        for joueur in self.state.players:
            if(joueur[0]==((self.id_team%2)+1)):
                    li=[self.state.player_state(joueur[0], joueur[1]).position,joueur[1],abs((self.state.player_state(joueur[0], joueur[1]).position-self.goal).x)]
                    l.append(li)
        l.sort(key=lambda l:l[2], reverse=True)
        return l
        
        
    @property
    def anticiperx2(self):
        return abs(self.my_goal.x-GAME_WIDTH*0.25)
    
    @property
    def anticiperx3(self):
        return abs(self.my_goal.x-GAME_WIDTH*0.67)
    
    @property
    def anticiperx4(self):
        return abs(self.my_goal.x-GAME_WIDTH*0.85)
    
    @property 
    def anticiper2(self):
        l=self.friend_list
        ll=self.enemy_list
        if(abs(ll[0][0].x - self.my_goal.x) < abs(self.anticiperx2 - self.my_goal.x) and abs(ll[1][0].x - self.my_goal.x) > abs(self.anticiperx2 - self.my_goal.x)):
            a=(ll[0][0].y-ll[1][0].y)/(ll[0][0].x-ll[1][0].x+1)
            b=ll[0][0].y-a*ll[0][0].x
            y=a*self.anticiperx2+b
            return Vector2D(self.anticiperx2,y)
        else:
            a=(ll[0][0].y-self.my_goal.y)/(ll[0][0].x-self.my_goal.x+1)
            b=self.my_goal.y-a*self.my_goal.x
            y=a*self.anticiperx2+b
            return Vector2D(self.anticiperx2,y)
            #return Vector2D(self.anticiperx2,abs(GAME_HEIGHT*(self.id_team+1)%2 - GAME_HEIGHT*0.2))
   
    @property
    def anticiper3(self):
        l=self.friend_list
        ll=self.enemy_list
        if(abs(ll[1][0].x - self.my_goal.x) < abs(self.anticiperx3 - self.my_goal.x) and abs(ll[2][0].x - self.my_goal.x) > abs(self.anticiperx3 - self.my_goal.x)):
            a=(ll[1][0].y-ll[2][0].y)/(ll[1][0].x-ll[2][0].x+1)
            b=ll[1][0].y-a*ll[1][0].x
            y=a*self.anticiperx3+b
            return Vector2D(self.anticiperx3,y)
        else:
            return Vector2D(self.anticiperx3,abs(GAME_HEIGHT*(self.id_team+1)%2 - GAME_HEIGHT*0.835))
    
    @property
    def anticiper4(self):
        l=self.friend_list
        ll=self.enemy_list
        if(abs(ll[2][0].x - self.my_goal.x) < abs(self.anticiperx4 - self.my_goal.x) and abs(ll[3][0].x - self.my_goal.x) > abs(self.anticiperx4 - self.my_goal.x)):
            a=(ll[2][0].y-ll[3][0].y)/(ll[2][0].x-ll[3][0].x+1)
            b=ll[2][0].y-a*ll[2][0].x
            y=a*self.anticiperx4+b
            return Vector2D(self.anticiperx4,y)
        else:
            return Vector2D(self.anticiperx4,abs(GAME_HEIGHT*(self.id_team+1)%2 - GAME_HEIGHT*0.5))

        
            
    @property
    def anticiperxdif(self):
        return abs(self.my_goal.x-GAME_WIDTH*0.02)
    
    
    @property
    def anticiperdif(self):
            p = self.poplayeren
            a=(p.y-self.my_goal.y)/(p.x-self.my_goal.x+1)
            b=self.my_goal.y-a*self.my_goal.x
            y=a*self.anticiperxdif+b
            return Vector2D(self.anticiperxdif,y)

        
        

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