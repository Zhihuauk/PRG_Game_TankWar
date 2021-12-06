# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 22:04:40 2021

@author: liuxx
"""

import pygame as pg

class tank:
    def __init__(self,number,pos,direction):
        self.num=number
        self.speed=1
        self.atk=1
        self.hp=30
        self.pos=pos
        self.size=50
        self.direction=direction
    
    def point(self):
        return [(self.pos[0],self.pos[1]),(self.pos[0]+self.size,self.pos[1]),(self.pos[0],self.pos[1]+self.size),(self.pos[0]+self.size,self.pos[1]+self.size)]
    
    def move_up(self):
        self.pos[1]-=self.speed
        
    def move_down(self):
        self.pos[1]+=self.speed
        
    def move_left(self):
        self.pos[0]-=self.speed
        
    def move_right(self):
        self.pos[0]+=self.speed
    
pg.init()
screen = pg.display.set_mode((1280,800))
bg_color=pg.Color(255,255,255)    #rgb
screen.fill(bg_color)
a=tank(0,[100,100],0)
enemy=[tank(1,[1000,400],0),tank(1,[250,600],2)]

def judge(pont,enemy,direction):
    for i in enemy:
        if direction==0 and (pg.Rect(i.pos[0],i.pos[1],i.size,i.size).collidepoint(pont[0][0],pont[0][1]) or pg.Rect(i.pos[0],i.pos[1],i.size,i.size).collidepoint(pont[1][0],pont[1][1])):
            return False
        if direction==1 and (pg.Rect(i.pos[0],i.pos[1],i.size,i.size).collidepoint(pont[2][0],pont[2][1]) or pg.Rect(i.pos[0],i.pos[1],i.size,i.size).collidepoint(pont[3][0],pont[3][1])):
            return False
        if direction==2 and (pg.Rect(i.pos[0],i.pos[1],i.size,i.size).collidepoint(pont[0][0],pont[0][1]) or pg.Rect(i.pos[0],i.pos[1],i.size,i.size).collidepoint(pont[2][0],pont[2][1])):
            return False
        if direction==3 and (pg.Rect(i.pos[0],i.pos[1],i.size,i.size).collidepoint(pont[1][0],pont[1][1]) or pg.Rect(i.pos[0],i.pos[1],i.size,i.size).collidepoint(pont[3][0],pont[3][1])):
            return False
    return True

def judge_wall():
    pass

while True:
    e=pg.event.poll()
    if e.type==pg.QUIT:
        pg.quit()
        break
    elif pg.key.get_pressed()[pg.K_UP]:
        if judge(a.point(),enemy,0):
            a.move_up()
        if not judge(a.point(),enemy,0):
            a.move_down()
   
    elif pg.key.get_pressed()[pg.K_DOWN]:
        if judge(a.point(),enemy,1):
            a.move_down()
        if not judge(a.point(),enemy,1):
            a.move_up()
  
    elif pg.key.get_pressed()[pg.K_LEFT]:
        if judge(a.point(),enemy,2):
            a.move_left()
        if not judge(a.point(),enemy,2):
            a.move_right()
 
    elif pg.key.get_pressed()[pg.K_RIGHT]:
        if judge(a.point(),enemy,3):
            a.move_right()
        if not judge(a.point(),enemy,3):
            a.move_left()
  
    elif pg.key.get_pressed()[pg.K_SPACE]:
        a.move_right()
    # i=enemy[1]
    # print(pg.Rect(i.pos[0],i.pos[1],i.size,i.size).collidepoint(a.point()[0][0],a.point()[0][1]))
    # print(pg.Rect(i.pos[0],i.pos[1],i.size,i.size).collidepoint(a.point()[1][0],a.point()[1][1]))
    # print(pg.Rect(i.pos[0],i.pos[1],i.size,i.size).collidepoint(a.point()[2][0],a.point()[2][1]))
    # print(pg.Rect(i.pos[0],i.pos[1],i.size,i.size).collidepoint(a.point()[3][0],a.point()[3][1]))
    # print('\n')
        
    
    # print(a.point())
    screen.fill(pg.Color(255,255,255))
    pg.draw.rect(screen,pg.Color(0,0,0),pg.Rect(a.pos[0],a.pos[1],a.size,a.size))
    for i in enemy:
        pg.draw.rect(screen,pg.Color(200,0,0),pg.Rect(i.pos[0],i.pos[1],i.size,i.size))
        # if i.direction==0:
        #     i.move_up()
        # elif i.direction==1:
        #     i.move_down()
        # elif i.direction==2:
        #     i.move_left()
        # elif i.direction==3:
        #     i.move_right()
        
    pg.display.flip()
    # for i in range(0,10000):
    #     i=1

    