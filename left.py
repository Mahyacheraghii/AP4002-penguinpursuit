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