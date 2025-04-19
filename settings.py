class Settings:
    def __init__(self):
        self.bg_color=(127,169,204)
        self.screen_width=1200
        self.screen_height=800
        self.pointer_width=575
        self.pointer_hight=225
        
        self.matrix =[[6,1,0,1,9],
                      [9,9,9,9,9],
                      [0,0,0,1,7],
                      [5,0,0,1,0],
                      [0,0,1,1,0]]
        
        self.grid_node_width = 50
        self.grid_node_height = 50
        
        self.matrix90=[[self.matrix[j][i] for j in range(len(self.matrix)-1,-1,-1)] for i in range(len(self.matrix[0]))]
        self.matrix180=[[self.matrix90[j][i] for j in range(len(self.matrix90)-1,-1,-1)] for i in range(len(self.matrix90[0]))]
        self.matrix270=[[self.matrix180[j][i] for j in range(len(self.matrix180)-1,-1,-1)] for i in range(len(self.matrix180[0]))]
        self.matrix360=[[self.matrix270[j][i] for j in range(len(self.matrix270)-1,-1,-1)] for i in range(len(self.matrix270[0]))]

        self.counter=0
        self.check_count = 0