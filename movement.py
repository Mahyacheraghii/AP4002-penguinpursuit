import pygame
import sys
from settings import Settings

class Movemont:
    
    def __init__(self):
        self.settings=Settings()
        
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
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:      
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
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x+1]=5
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
                        if self.settings.matrix[self.p1y][self.p1x+1]==9:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=14
                            self.settings.counter+=1
                                
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.settings.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.settings.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==14:      
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
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y][self.p1x-1]=5
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
                                
                    if self.settings.matrix[self.p1y][self.p1x]==14:      
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
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y-1][self.p1x]=5
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
                              
                    if self.settings.matrix[self.p1y][self.p1x]==14:      
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
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=9
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.settings.counter+=1
                        
            elif event.type == pygame.KEYDOWN and self.settings.check_count == 1:
                
                self.check_coordinates_p1()
                if event.key==pygame.K_RIGHT and self.p1y!=4:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=4
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.counter+=1
                                
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.counter+=1    
                            
                if event.key==pygame.K_LEFT and self.p1y!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=4
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.counter+=1
                                
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.counter+=1  
                            
                if event.key==pygame.K_UP and self.p1x!=4:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=4
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.counter+=1

                if event.key==pygame.K_DOWN and self.p1x!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=4
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.counter+=1
                            
            elif event.type == pygame.KEYDOWN and self.settings.check_count == 2:
                
                self.check_coordinates_p1()
                if event.key==pygame.K_RIGHT and self.p1x!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=4
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.counter+=1

                if event.key==pygame.K_LEFT and self.p1x!=4:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=4
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.counter+=1

                if event.key==pygame.K_UP and self.p1y!=4:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=4
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.counter+=1
                                
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.counter+=1    
                            
                if event.key==pygame.K_DOWN and self.p1y!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=4
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.counter+=1     
                            
            elif event.type == pygame.KEYDOWN and self.settings.check_count == 3:
                
                self.check_coordinates_p1()
                if event.key==pygame.K_RIGHT and self.p1y!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=4
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y-1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y-1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y-1][self.p1x]=8
                            self.counter+=1     
                            
                if event.key==pygame.K_LEFT and self.p1y!=4:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=4
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.counter+=1
                                
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y+1][self.p1x]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y+1][self.p1x]=8
                            self.counter+=1    
                                
                if event.key==pygame.K_UP and self.p1x!=0:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=4
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x-1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x-1]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x-1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x-1]=8
                            self.counter+=1
                            
                if event.key==pygame.K_DOWN and self.p1x!=4:
                    if self.settings.matrix[self.p1y][self.p1x]==5:
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==6:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=4
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=0
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.counter+=1
                            
                    if self.settings.matrix[self.p1y][self.p1x]==4:    
                        
                        if self.settings.matrix[self.p1y][self.p1x+1]==0:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=5
                            self.counter+=1
                            
                        if self.settings.matrix[self.p1y][self.p1x+1]==7:
                            self.settings.matrix[self.p1y][self.p1x]=6
                            self.settings.matrix[self.p1y][self.p1x+1]=8
                            self.counter+=1
                                