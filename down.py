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