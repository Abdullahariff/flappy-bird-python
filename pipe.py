import pygame as pg
from random import randint

class Pipe(pg.sprite.Sprite):
    def __init__(self,scale_factor,move_speed):
         
         self.imgup = pg.transform.scale_by(pg.image.load("assets/pipeup.png").convert_alpha(), scale_factor)
         self.imgdown=pg.transform.scale_by(pg.image.load("assets/pipedown.png").convert_alpha(), scale_factor)
         self.rect_up=self.imgup.get_rect()
         self.rect_down=self.imgdown.get_rect()
         self.pipedistance=130
         self.rect_up.y=randint(150,350)
         self.rect_up.x=600
         self.rect_down.y = self.rect_up.y - self.pipedistance-self.rect_up.height
         self.rect_down.x=600
         self.move_speed=move_speed

    def drawpipes(self,win):
         win.blit(self.imgup,self.rect_up)
         win.blit(self.imgdown,self.rect_down)

    def move(self,dt):
         self.rect_up.x-=int(self.move_speed*dt)
         self.rect_down.x-=int(self.move_speed*dt)

         



    