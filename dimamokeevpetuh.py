from tkinter import *
from random import *
import time
SX=1200
SY=700
VMAX=10

def create_ball():
    b=ball(rx(),ry(),rv(),rv(),rr())
    balls.append(b)
    b.draw_ball(b.color)
    b.move_ball()

def click(event):
    x, y = event.x, event.y
    for ball_name in balls:
        if((ball_name.x - x)**2 + (ball_name.y - y)**2) < ball_name.r**2:
            ball_name.kill_ball()
        
def rx():
    return(randint(SX//3,(2*SX)//3))
def ry():
    return(randint(SY//3,(2*SY)//3))
def rv():
    return(randint(-1 * VMAX, VMAX))
def rr():
    rr=600//(20+pasha.score)
    return(rr)
class player:
    def __init__(self,name):
        self.score=0
        self.name=name
        self.maxscore=0
        self.number_balls=1
    
class ball:
    def __init__(self, x, y, vx, vy, r):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.r=r
        self.color='blue'
        self.died_time=0
        self.points=3
        
    def draw_ball(self,col):
        canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = col, width=0)
        
    def move_ball(self):
        if pasha.score <=-20:
            fi=open('record.txt','r+')
            fi.write(' '+ str(pasha.maxscore))
            root.after(1000,exit())
        if self.died_time == 0:
            self.draw_ball('white')
            self.x+=self.vx
            self.y+=self.vy
            self.draw_ball(self.color)
            if (self.x > SX) or (self.x < 0):
                self.vx=-self.vx
                pasha.score -=1
                l['text'] = 'Счёт игрока ' + pasha.name + ' = ' +  str(pasha.score) + ' Ваш максимум = ' + str(pasha.maxscore)
            if (self.y > SY) or (self.y < 0):
                self.vy=-self.vy
                pasha.score -=1
                l['text'] = 'Счёт игрока ' + pasha.name + ' = ' +  str(pasha.score) + ' Ваш максимум = ' + str(pasha.maxscore)
        else:
            self.died_time -=1
        root.after(30,self.move_ball)
        
    def kill_ball(self):
        global s
        self.draw_ball('white')
        self.vx=rv()
        self.vy=rv()
        self.x=rx()
        self.y=ry()
        self.r=rr()
        self.died_time = 30
        pasha.score += self.points
        if pasha.score > pasha.maxscore :
            pasha.maxscore = pasha.score
            l['text'] = 'Счёт игрока ' + pasha.name + ' = ' +  str(pasha.score) + ' Ваш максимум = ' + str(pasha.maxscore)
        if pasha.score >= pasha.number_balls*10:
            create_ball()
            pasha.number_balls+=1



            
root=Tk()
root.geometry(str(SX)+'x'+str(SY))
canv = Canvas(root,bg='white')
canv.pack(fill = BOTH, expand = 1)
balls= []

pasha=player('Pasha')

create_ball()
l = Label(bg='black', fg='white', width=100)
l['text'] = 'Счёт игрока ' + pasha.name + ' = ' +  str(pasha.score) + ' Ваш максимум = ' + str(pasha.maxscore)
l.pack()


canv.bind('<Button-1>', click)

mainloop()
