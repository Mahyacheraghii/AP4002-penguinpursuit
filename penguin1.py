import pygame

class Penguin1():
    def __init__(self,pp_game):
        self.screen=pp_game.screen
        self.screen_rect=self.screen.get_rect()
        
        self.image=pygame.image.load("./photos/penguin1.PNG")
        self.rect=self.image.get_rect()

    #image    
    def blitme(self):
        self.screen.blit(self.image,self.rect)