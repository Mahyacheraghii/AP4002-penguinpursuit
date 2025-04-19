import pygame
from settings import Settings
class Pointer():
    
    def __init__(self,pp_game):
        self.screen=pp_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=Settings()
        self.image=pygame.image.load("./photos/pointer.PNG")
        self.rect=(self.settings.pointer_width,self.settings.pointer_hight)

    #image    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    