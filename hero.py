class Hero:
    def __init__(self, position, land):
            self.camera_mode = None
            self.game_mode = True
            self.land = land
            self.hero = loader.loadModel('smiley')
            self.hero.setColor((255//100, 0//100, 0//100, 1))
            self.hero.setScale(0.5)
            self.hero.setPos(position)
            self.hero.reparentTo(render)
            
            self.camera_bind()
            self.accept_events()    
    def camera_bind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.camera_mode = True
        
    def camera_up(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.camera_mode = False
    def switch_camera(self):
        if self.camera_mode:
            self.camera_up()
        else:
            self.camera_bind()
            
    def change_mode(self):
        if self.game_mode:
            self.game_mode = False  
        else:
            self.game_mode = True
            
    def turn_left(self):
        self.hero.setH(self.hero.getH() + 5 % 360)
        
    def turn_right(self):
        self.hero.setH(self.hero.getH() - 5 % 360) 
        
    def move_to(self, angle):
        """"обираємо як рухати гравця в залежності від напрямку""" 
        if self.game_mode:
            self.just_move(angle)
        else:
            self.try_move(angle)
    def just_move(self,angle):
        """"рухаємо гравця вперед""" 
        pos = self.look_at(angle)
        self.hero.setPos(pos)
        
        
    
    def try_move(self,angle):
        """"рухаємо гравця по ігровому режиму""" 
        pos = self.look_at(angle)
        if self.look_at(angle):
            if self.land.is_empty(pos):
                pos = self.land.find_highest(pos)
                self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.is_empty(pos):
                self.hero.setPos(pos)
        
    def check_dir(self, angle):
       ''' повертає заокруглені зміни координат X, Y,
       відповідні переміщенню у бік кута angle.
       Координата Y зменшується, якщо персонаж дивиться на кут 0,
       та збільшується, якщо дивиться на кут 180.
       Координата X збільшується, якщо персонаж дивиться на кут 90,
       та зменшується, якщо дивиться на кут 270.
           кут 0 (від 0 до 20) -> Y - 1
           кут 45 (від 25 до 65) -> X + 1, Y - 1
           кут 90 (від 70 до 110) -> X + 1
           від 115 до 155 -> X + 1, Y + 1
           від 160 до 200 -> Y + 1
           від 205 до 245 -> X - 1, Y + 1
           від 250 до 290 -> X - 1
           від 290 до 335 -> X - 1, Y - 1
           від 340 -> Y - 1
       '''
       if 0 <= angle <= 20:
           return 0, -1
       elif angle <= 65:
           return 1, -1
       elif angle <= 110:
           return 1, 0
       elif angle <= 155:
           return 1, 1
       elif angle <= 200:
           return 0, 1
       elif angle <= 245:
           return -1, 1
       elif angle <= 290:
           return -1, 0
       elif angle <= 335:
           return -1, -1
       else:
           return 0, -1
       
    def look_at(self,angle):
        x = round(self.hero.getX())
        y = round(self.hero.getY())
        z = round(self.hero.getZ())
        
        dx, dy = self.check_dir(angle)
        
        return x + dx, y + dy, z
    
    def forward(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)
        
    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)
   
    def right(self):
        angle = (self.hero.getH() - 90) % 360
        self.move_to(angle)
        
    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)
        
        
    def up(self):
        self.hero.setZ(self.hero.getZ() + 1)
        
    def down(self):
        if self.game_mode:
            self.hero.setZ(self.hero.getZ() - 1)
         
    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.game_mode:
            self.land.add_block(pos)
        else:
            self.land.build_block(pos)
            
    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.game_mode:
            self.land.destroy_block(pos)
        else:
            self.land.del_block_from(pos)
       

        
        
    def accept_events(self):
        base.accept('c', self.switch_camera)
        base.accept('a', self.turn_left)
        base.accept('a''-repeat', self.turn_left)
        base.accept('d', self.turn_right)
        base.accept('d''-repeat', self.turn_right)
        base.accept('w', self.forward)
        base.accept('w''-repeat', self.forward) 
        base.accept('s', self.back)
        base.accept('s''-repeat', self.back)
        base.accept('q', self.left)
        base.accept('q''-repeat', self.left)  
        base.accept('e', self.right)
        base.accept('e''-repeat', self.right)
        base.accept('r', self.up)
        base.accept('r''-repeat', self.up)
        base.accept('f', self.down)
        base.accept('f''-repeat', self.down)
        base.accept('z', self.change_mode)
        base.accept('mouse1', self.build)
        base.accept('v', self.destroy)
        base.accept('o', self.land.load_map_from_file)
        base.accept('p', self.land.save_map)