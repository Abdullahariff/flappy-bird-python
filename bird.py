import pygame as pg

class Bird (pg.sprite.Sprite):
    
    def __init__(self,scale_factor) :
        super(Bird,self).__init__()
        #self.scale_factor = scale_factor
        self.birdimglist = [
    pg.transform.scale_by(pg.image.load("assets/birdup.png").convert_alpha(), scale_factor),
    pg.transform.scale_by(pg.image.load("assets/birddown.png").convert_alpha(), scale_factor)
]

        
        self.imageindex=0
        self.image=self.birdimglist[self.imageindex]
        self.rect=self.image.get_rect(center=(100,100))
        self.y_speed=0
        self.gravity=10
        self.flapspeed=200
        self.animationcount=0
        self.updateon=True

    def updatebird(self,dt):
        if self.updateon:
            
            self.animation()
            self.applygravity(dt)
            if self.rect.top < 0:  # Prevent going above the screen
             self.rect.top = 0
        

            if self.rect.bottom > 500:  # Prevent going below the screen (500 is your window height)
                self.rect.bottom = 500
       
        
    def applygravity(self,dt):
       
        self.y_speed+=self.gravity*dt
        self.rect.y +=self.y_speed
           
    def flap(self,dt):
       self.y_speed=-self.flapspeed*dt

    def animation(self):
        # if self.animationcount==5:
        #     self.image=self.birdimglist[self.imageindex]
        #     if self.imageindex==0: 
        #         self.imageindex=1
        #     else:
        #         self.imageindex=0
        #     self.animationcount=0
        # self.animationcount+=1
         if self.animationcount == 5:
            self.image = self.birdimglist[self.imageindex]
            self.imageindex = 1 - self.imageindex  # Toggle between 0 and 1
            self.animationcount = 0
         self.animationcount += 1

    def resetbird(self):
         self.rect.center=(100,100)
         self.y_speed=0
         self.animationcount=0
         
         
         
         
          





   