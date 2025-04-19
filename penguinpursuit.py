from settings import Settings
from penguin1 import Penguin1
from penguin2 import Penguin2
from pointer import Pointer
from fish import Fish
import pygame
import sys
import time
from time import sleep
from start_button import StartButton
from gameover_button import EndButton

class PenguinPursuit:
    def __init__(self):
        
        pygame.init()
        self.settings=Settings()
        self.b=0
        # self.c=0

        self.game_active = False
        self.show_button = True

        # screen
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("penguin pursuit")
        self.clock=pygame.time.Clock()

        self.play_button = StartButton(self, "play")
        self.gameover_button = EndButton(self, "Game Over!")
        
        #make penguin
        self.penguin1=Penguin1(self)
        self.penguin2=Penguin2(self)
        self.fish=Fish(self)
        self.pointer=Pointer(self)
        
        self.settings.counter = 0
            
    def run_game_1(self):
        self.a=time.time()
        while True:
            self.check_event()
            self.update_screen()
            if self.game_active:   
                self.visualizeGrid()
                # self.rotate()
                self.p2_move()
                self.b=time.time()   
                self.c=time.time()
            self.end_game()
            self.clock.tick(90)
                             
    def visualizeGrid(self):
        y =275
        for row in self.settings.matrix:
            x = 475
            for item in row:
                if item == 0:
                    self.createSquare(x, y, (255, 255, 255))
                    
                if item == 1:
                    self.createSquare(x, y, (0, 0, 0))
                    
                if item == 4:
                    self.createSquare(x, y, (255, 255,255))
                    self.penguin2.rect=(x,y)
                    self.penguin1.rect=(x,y)   
                     
                if item == 5:
                    self.createSquare(x, y, (255, 255,255))
                    self.penguin1.rect=(x,y)
                
                if item == 6:
                    self.createSquare(x, y, (255, 255,255))
                    self.penguin2.rect=(x,y)
                
                if item == 7:
                    self.createSquare(x, y, (255, 255,255))
                    self.fish.rect=(x,y)
                    
                if item == 8:
                    self.createSquare(x, y, (255, 255, 255))
                    self.penguin1.rect=(x, y)
                    self.fish.rect=(x,y)
                    
                if item == 9:
                    self.createSquare(x, y, (255, 255, 255))
                       
                if item == 10:
                    self.createSquare(x, y, (255, 255, 255))
                    self.penguin2.rect=(x, y)
                    self.fish.rect=(x,y)
                    
                if item == 14:
                    self.createSquare(x, y, (255, 255, 255))
                    self.penguin1.rect=(x, y)
                
                # if item == 20:
                #     self.createSquare(x, y, (255, 255, 255))
                #     self.penguin1.rect=(x, y)
                    
                    
                x += self.settings.grid_node_width    
            y += self.settings.grid_node_height
            
    def createSquare(self,x, y, color):
        pygame.draw.rect(self.screen, color, [x, y, self.settings.grid_node_width, self.settings.grid_node_height ])
    
    def check_coordinates_p1(self):
            
        self.lst5=[(index1, row.index(5)) for index1, row in enumerate(self.settings.matrix) if 5 in row]
        self.lst4=[(index1, row.index(4)) for index1, row in enumerate(self.settings.matrix) if 4 in row]
        self.lst8=[(index1, row.index(8)) for index1, row in enumerate(self.settings.matrix) if 8 in row]
        self.lst10=[(index1, row.index(10)) for index1, row in enumerate(self.settings.matrix) if 10 in row]
        self.lst14=[(index1, row.index(14)) for index1, row in enumerate(self.settings.matrix) if 14 in row]
        
        if len(self.lst5)==1:
            self.p1y=self.lst5[0][0]
            self.p1x=self.lst5[0][1]
        
        elif len(self.lst4)==1:
            self.p1y=self.lst4[0][0]
            self.p1x=self.lst4[0][1]
            
        elif len(self.lst8)==1:
            self.p1y=self.lst8[0][0]
            self.p1x=self.lst8[0][1]
            
        elif len(self.lst10)==1:
            self.p1y=self.lst10[0][0]
            self.p1x=self.lst10[0][1]  
            
        elif len(self.lst14)==1:
            self.p1y=self.lst14[0][0]
            self.p1x=self.lst14[0][1]
    
    def check_coordinates_p2(self):
        self.lstp2=[(index, row.index(6)) for index, row in enumerate(self.settings.matrix) if 6 in row]
        if len(self.lstp2)==1:
            self.p2y=self.lstp2[0][0]
            self.p2x=self.lstp2[0][1] 
            
        elif len(self.lst4)==1:
            self.p2y=self.lst4[0][0]
            self.p2x=self.lst4[0][1]
            
    def check_event(self):
        self.check_coordinates_p1()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()      
            
            elif event.type == pygame.KEYDOWN and self.settings.check_count == 0: 
                  
                if event.key==pygame.K_RIGHT and self.p1x!=4:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y][self.p1x+1]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y][self.p1x+1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x+1]=4
                            self.settings.counter+=1
                        
                if event.key==pygame.K_LEFT and self.p1x!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y][self.p1x-1]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y][self.p1x-1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x-1]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x-1]=4
                            self.settings.counter+=1
                                       
                if event.key==pygame.K_UP and self.p1y!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y-1][self.p1x]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y-1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y-1][self.p1x]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y-1][self.p1x]=4
                            self.settings.counter+=1
                        
                if event.key==pygame.K_DOWN and self.p1y!=4:
                    
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y+1][self.p1x]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y+1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y+1][self.p1x]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y+1][self.p1x]=4
                            self.settings.counter+=1
                                          
            elif event.type == pygame.KEYDOWN and self.settings.check_count == 1:
                
                self.check_coordinates_p1()
                if event.key==pygame.K_RIGHT and self.p1y!=4:
                    
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y+1][self.p1x]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y+1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y+1][self.p1x]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y+1][self.p1x]=4
                            self.settings.counter+=1
                            
                if event.key==pygame.K_LEFT and self.p1y!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y-1][self.p1x]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y-1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y-1][self.p1x]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y-1][self.p1x]=4
                            self.settings.counter+=1
                                
                if event.key==pygame.K_UP and self.p1x!=4:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y][self.p1x+1]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y][self.p1x+1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x+1]=4
                            self.settings.counter+=1
                            
                if event.key==pygame.K_DOWN and self.p1x!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y][self.p1x-1]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y][self.p1x-1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x-1]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x-1]=4
                            self.settings.counter+=1
                            
            elif event.type == pygame.KEYDOWN and self.settings.check_count == 2:
                
                self.check_coordinates_p1()
                if event.key==pygame.K_RIGHT and self.p1x!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y][self.p1x-1]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y][self.p1x-1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x-1]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x-1]=4
                            self.settings.counter+=1
                            
                if event.key==pygame.K_LEFT and self.p1x!=4:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y][self.p1x+1]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y][self.p1x+1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x+1]=4
                            self.settings.counter+=1

                if event.key==pygame.K_UP and self.p1y!=4:
                    
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y+1][self.p1x]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y+1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y+1][self.p1x]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y+1][self.p1x]=4
                            self.settings.counter+=1
                            
                if event.key==pygame.K_DOWN and self.p1y!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y-1][self.p1x]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y-1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y-1][self.p1x]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y-1][self.p1x]=4
                            self.settings.counter+=1
                            
            elif event.type == pygame.KEYDOWN and self.settings.check_count == 3:
                
                self.check_coordinates_p1()
                if event.key==pygame.K_RIGHT and self.p1y!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y-1][self.p1x]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y-1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y-1][self.p1x]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y-1][self.p1x]=4
                            self.settings.counter+=1
                            
                if event.key==pygame.K_LEFT and self.p1y!=4:
                    
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y+1][self.p1x]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y+1][self.p1x]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y+1][self.p1x]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y+1][self.p1x]=4
                            self.settings.counter+=1
                            
                if event.key==pygame.K_UP and self.p1x!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y][self.p1x-1]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y][self.p1x-1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x-1]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x-1]=4
                            self.settings.counter+=1
                            
                if event.key==pygame.K_DOWN and self.p1x!=4:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=4
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:    
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                                self.settings.matrix[self.p1y][self.p1x]=9
                                self.settings.matrix[self.p1y][self.p1x+1]=5
                                self.settings.counter+=1  
                                
                        if self.settings.matrix[self.p1y][self.p1x+1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.settings.counter+=1
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x+1]=4
                            self.settings.counter+=1

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos =pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True
            self.show_button = False

    def p2_move(self):
        self.check_coordinates_p2()
        self.c=time.time()
        near=[(self.p2y,self.p2x+1),(self.p2y,self.p2x-1),(self.p2y-1,self.p2x),(self.p2y+1,self.p2x)]             
        
        if 4.9<((self.c-self.a)%5)<4.99:
            for i in range(0,len(near)):
                lst=[near[i]]  
                lst=[lst[0][0],lst[0][1]]
                
                if lst[0]!=5 and lst[1]!=5 and lst[0]!=-1 and lst[1]!=-1:
                    
                    if self.settings.matrix[self.p2y][self.p2x]==6:
                        if self.settings.matrix[lst[0]][lst[1]]==9 or self.settings.matrix[lst[0]][lst[1]]==7 :
                            self.settings.matrix[self.p2y][self.p2x]=0
                            self.settings.matrix[lst[0]][lst[1]]=6
                            sleep(0.1)

                        if self.settings.matrix[lst[0]][lst[1]]==14:
                            self.settings.matrix[self.p2y][self.p2x]=0
                            self.settings.matrix[lst[0]][lst[1]]=4
                            sleep(0.1)
                            
                    if self.settings.matrix[self.p2y][self.p2x]==4:  
                        if self.settings.matrix[lst[0]][lst[1]]==9 or self.settings.matrix[lst[0]][lst[1]]==7 :
                            self.settings.matrix[self.p2y][self.p2x]=5
                            self.settings.matrix[lst[0]][lst[1]]=6
                            sleep(0.1)
                        
    def rotate(self):
        if self.settings.counter==5 and self.settings.check_count == 0:
            self.pointer.rect=(725,375)
            self.pointer.image=pygame.image.load("./photos/pointer90.PNG")
            self.settings.matrix=[[self.settings.matrix[j][i] for j in range(len(self.settings.matrix)-1,-1,-1)] for i in range(len(self.settings.matrix[0]))]
            # sleep(0.1)
            self.settings.counter = 0
            self.settings.check_count += 1
            
        if self.settings.counter==5 and self.settings.check_count == 1:
            self.pointer.rect=(575,525)
            self.pointer.image=pygame.image.load("./photos/pointer180.PNG")
            self.settings.matrix=[[self.settings.matrix[j][i] for j in range(len(self.settings.matrix)-1,-1,-1)] for i in range(len(self.settings.matrix[0]))]
            self.settings.counter = 0
            self.settings.check_count += 1
            
        if self.settings.counter==5 and self.settings.check_count == 2:
            self.pointer.rect=(425,375)
            self.pointer.image=pygame.image.load("./photos/pointer270.PNG")
            self.settings.matrix=[[self.settings.matrix[j][i] for j in range(len(self.settings.matrix)-1,-1,-1)] for i in range(len(self.settings.matrix[0]))]
            self.settings.counter = 0
            self.settings.check_count += 1
                
        if self.settings.counter==5 and self.settings.check_count == 3:
            self.pointer.rect=(575,225)
            self.pointer.image=pygame.image.load("./photos/pointer.PNG")
            self.settings.matrix=[[self.settings.matrix[j][i] for j in range(len(self.settings.matrix)-1,-1,-1)] for i in range(len(self.settings.matrix[0]))]
            self.settings.counter = 0
            self.settings.check_count = 0
     
    def end_game(self):
        if (self.b-self.a)>=30:
            self.game_active = False
            self.gameover_button.draw_button()

        if len(self.lst8)==1:
            # sleep(1)
            sys.exit()
        elif len(self.lst10)==1:
            sys.exit()
             
    def update_screen(self):
        if self.game_active:
            self.penguin1.blitme()
            self.penguin2.blitme()
            self.fish.blitme()
            self.pointer.blitme()
        if self.show_button:
            self.play_button.draw_button()
        pygame.display.flip()
        self.screen.fill(self.settings.bg_color) 
    
if __name__== "__main__":
    for i in range (1,8):
        pp=PenguinPursuit()
        if i ==1:
            pp.run_game_1()
 