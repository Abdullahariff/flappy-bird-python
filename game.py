import pygame as pg
import sys,time
from bird import Bird
from pipe import Pipe
pg.init()

class Game:
    def __init__(self):
        #setting window config
        self.width =  600
        self.height=500
        self.scale_factor=1.5
        self.win=pg.display.set_mode((self.width,self.height))
        self.clock=pg.time.Clock()
        self.move_speed=250
        self.bird=Bird(self.scale_factor)
        self.isenterpressed=False
        self.pipes=[]
        self.startmonitoring=False
        self.score=0
        self.font=pg.font.Font("assets/font.ttf",24)
        self.scoretext=self.font.render("Score: 0",True,(0,0,0))
        self.scoretext_rect=self.scoretext.get_rect(center=(100,30))
        self.restarttext=self.font.render("Restart",True,(0,0,0))
        self.restarttext_rect=self.restarttext.get_rect(center=(300,450))
        self.gamestarted=True

        self.pipegeneratecounter=71
        self.setupbgandground()

        self.gameloop()

    def gameloop(self):
        lasttime=time.time()
        while True:
            #calculating delta time
            newtime=time.time()
            dt=newtime-lasttime
            lasttime=newtime
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type==pg.KEYDOWN and self.gamestarted:
                    print(f"Key Pressed: {event.key}, isenterpressed={self.isenterpressed}")
                    if event.key==pg.K_RETURN:
                        self.isenterpressed=True
                    if event.key==pg.K_SPACE and self.isenterpressed:
                        self.bird.flap(dt)
                if event.type==pg.MOUSEBUTTONUP:
                    self.restarttext_rect.collidepoint(pg.mouse.get_pos())
                    print("restrart clicked")
                    self.restartgame()
            self.update(dt)
            self.collisions()
            self.checkscore()
            self.drawingeverything()
            pg.display.update()
            self.clock.tick(60)
    def restartgame(self):
        self.score=0
        self.scoretext=self.font.render("Score: 0",True,(0,0,0))
        self.isenterpressed=False
        self.gamestarted=True
        self.bird.resetbird()
        self.pipes.clear()
        self.pipegeneratecounter=71
        self.bird.updateon=True
        print(f"Game restarted: isenterpressed={self.isenterpressed}, gamestarted={self.gamestarted}, bird.updateon={self.bird.updateon}")



    def checkscore(self):
        if len(self.pipes)>0:
            if (self.bird.rect.left>self.pipes[0].rect_down.left and 
                self.bird.rect.right<self.pipes[0].rect_down.right and not self.startmonitoring):
                    self.startmonitoring=True
            if self.bird.rect.left>self.pipes[0].rect_down.right and self.startmonitoring:
                self.startmonitoring=False
                self.score+=1
                self.scoretext=self.font.render(f"Score: {self.score}",True,(0,0,0))

                
    def collisions(self):
        if len(self.pipes):
            if (self.bird.rect.bottom>450 or self.bird.rect.colliderect(self.pipes[0].rect_down)or
                self.bird.rect.colliderect(self.pipes[0].rect_up)):
                    self.bird.updateon=False
                    self.isenterpressed=False
                    self.gamestarted=False

    def update(self,dt):
        if self.isenterpressed:
         #moving the ground
         
         
         self.ground1rect.x-=int(self.move_speed*dt)
         self.ground2rect.x-=int(self.move_speed*dt)

         if self.ground1rect.right<0:
            self.ground1rect.x=self.ground2rect.right
         if self.ground2rect.right<0:
            self.ground2rect.x=self.ground1rect.right
        #generating pipes
         if self.pipegeneratecounter>70:
             self.pipes.append(Pipe(self.scale_factor,self.move_speed))
             self.pipegeneratecounter=0
             
         self.pipegeneratecounter+=1
        #moving the pipes
         for pipe in self.pipes:
             pipe.move(dt)
        #Removing pipes when out of screen
         if len(self.pipes)!=0:
             if self.pipes[0].rect_up.right<0:
                 self.pipes.pop(0)
                 
            
         self.bird.updatebird(dt)
          

    
    def drawingeverything(self):
        self.win.blit(self.bg_img,(0,-450))
        for pipe in self.pipes:
         pipe.drawpipes(self.win)


        self.win.blit(self.ground1img,self.ground1rect)
        self.win.blit(self.ground2img,self.ground2rect)
        self.win.blit(self.bird.image,self.bird.rect)
        self.win.blit(self.scoretext,self.scoretext_rect)
        if not self.gamestarted:
            self.win.blit(self.restarttext,self.restarttext_rect)

    
    def setupbgandground (self):
        #loading bg and ground images
        self.bg_img=pg.transform.scale_by( pg.image.load("assets/bg.png").convert(),self.scale_factor)
        self.ground1img=pg.transform.scale_by(pg.image.load("assets/ground.png").convert(),self.scale_factor)
        self.ground2img=pg.transform.scale_by(pg.image.load("assets/ground.png").convert(),self.scale_factor)

        self.ground1rect=self.ground1img.get_rect()
        self.ground2rect=self.ground2img.get_rect()
        self.ground1rect.x=0
        self.ground2rect.x=self.ground1rect.right
        self.ground1rect.y=400
        self.ground2rect.y=400
        

game=Game()