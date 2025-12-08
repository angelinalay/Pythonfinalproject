import pygame
import math

pygame.init()

Width = 900
Height = 950
SCREEN_WIDTH = Width
SCREEN_HEIGHT = Height
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
PI = math.pi


board = [
[6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
[3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
[4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4],
[5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
[3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
[3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
[3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
[7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
         ]


#Images
cheese = pygame.image.load("cheese.png").convert_alpha()
cheese2 = pygame.transform.smoothscale(cheese,(25,25))
cat1 = pygame.image.load("graycat.png").convert_alpha()
Gray = pygame.transform.smoothscale(cat1, (40,40))
cat2 = pygame.image.load("Orangecat.png").convert_alpha()
Orange = pygame.transform.smoothscale(cat2, (40,40))
cat3 = pygame.image.load("Orange_Whitecat.png").convert_alpha()
Orange_white = pygame.transform.smoothscale(cat3, (40,40))
cat4 = pygame.image.load("Spotscat.png").convert_alpha()
Spots = pygame.transform.smoothscale(cat4, (40,40))
Mouse1 = pygame.image.load("Mouse_open.png").convert_alpha()
Mouse_open = pygame.transform.smoothscale(Mouse1, (40,40))
Mouse2 = pygame.image.load("Mouse_closed.png").convert_alpha()
Mouse_closed = pygame.transform.smoothscale(Mouse2, (40,40))


#Cat Starting Position
Cat1_x = 56
Cat1_y = 58
Cat1_direction = 0
Cat1_dead = False
Cat1_box = False
cat_speed = 2
Cat2_dead = False
Cat2_box = False 


#Player/Mouse variables for displaying and movement 
Player_Images = []
for i in range(1, 3):
    Player_Images.append(Mouse_open)
    Player_Images.append(Mouse_closed)

counter = 0
direction = 0
turns_allowed = [False, False, False, False]
player_speed = 2




class Catz:
    def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box,id):
        self.xpos = x_coord
        self.ypos = y_coord
        self.center_x = self.xpos + 22
        self.center_y = self.ypos + 22
        self.target = target
        self.speed = speed
        self.img = img
        self.id = id
        self.direction = direct
        self.in_box = box
        self.dead = dead 
        self.turns, self.in_box = self.check_catcollisions()
        self.rect = self.draw()
    
    def draw(self):
        if True:
            screen.blit(self.img, (self.xpos, self.ypos))
        ghost_rect = pygame.rect.Rect((self.center_x -18, self.center_y -18), (36,36))
        return ghost_rect
    def check_catcollisions(self):
        num1 = ((Height - 50) // 32)
        num2 = (Width // 30)
        num3 = 15

        self.turns = [False, False, False, False]
        if 0 < self.center_x // 30 < 29:
            if board[(self.center_y - num3) // num1][self.center_x // num2] == 9:
                self.turns[2] = True
            if board[self.center_y // num1][(self.center_x - num3) // num2] < 3 \
                    or (board[self.center_y // num1][(self.center_x - num3) // num2] == 9 and (
                    self.in_box or self.dead)):
                self.turns[1] = True
            if board[self.center_y // num1][(self.center_x + num3) // num2] < 3 \
                    or (board[self.center_y // num1][(self.center_x + num3) // num2] == 9 and (
                    self.in_box or self.dead)):
                self.turns[0] = True
            if board[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
                    or (board[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
                    self.in_box or self.dead)):
                self.turns[3] = True
            if board[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
                    or (board[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
                    self.in_box or self.dead)):
                self.turns[2] = True
        if self.direction == 2 or self.direction == 3:
                if 12 <= self.center_x % num2 <= 18:
                    if board[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
                            or (board[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[2] = True
                if 12 <= self.center_y % num1 <= 18:
                    if board[self.center_y // num1][(self.center_x - num2) // num2] < 3 \
                            or (board[self.center_y // num1][(self.center_x - num2) // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[1] = True
                    if board[self.center_y // num1][(self.center_x + num2) // num2] < 3 \
                            or (board[self.center_y // num1][(self.center_x + num2) // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[0] = True
        if self.direction == 0 or self.direction == 1:
                if 12 <= self.center_x % num2 <= 18:
                    if board[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
                            or (board[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[3] = True
                    if board[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
                            or (board[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[2] = True
                if 12 <= self.center_y % num1 <= 18:
                    if board[self.center_y // num1][(self.center_x - num3) // num2] < 3 \
                            or (board[self.center_y // num1][(self.center_x - num3) // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[1] = True
                    if board[self.center_y // num1][(self.center_x + num3) // num2] < 3 \
                            or (board[self.center_y // num1][(self.center_x + num3) // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[0] = True
        else:
            self.turns[0] = True
            self.turns[1] = True
        if 350 < self.xpos < 550 and 370 < self.ypos < 480:
            self.in_box = True
        else:
            self.in_box = False
        return self.turns, self.in_box

    def move_Gray (self):
        
        if self.direction == 0:
            if self.target[0] > self.xpos and self.turns[0]:
                self.xpos += self.speed
            elif not self.turns[0]:
                if self.target [1] > self.ypos and self.turns[3]:
                    self.direction = 3
                    self.ypos += self.speed
                elif self.target[1] < self.ypos and self.turns[2]:
                    self.direction = 2
                    self.ypos -= self.speed
                elif self.target[0] < self.xpos and self.turns[1]:
                    self.direction = 1
                    self.xpos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.ypos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.ypos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.xpos -= self.speed
            elif self.turns[0]:
                if self.target[1] > self.ypos and self.turns[3]:
                    self.direction = 3
                    self.ypos += self.speed
                if self.target[1] < self.ypos and self.turns[2]:
                    self.direction = 2
                    self.ypos -= self.speed
                else:
                    self.xpos += self.speed
        elif self.direction == 1:
            if self.target[1] > self.ypos and self.turns[3]:
                self.direction = 3
            elif self.target[0] < self.xpos and self.turns[1]:
                self.xpos -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.ypos and self.turns[3]:
                    self.direction = 3
                    self.ypos += self.speed
                elif self.target[1] < self.ypos and self.turns[2]:
                    self.direction = 2
                    self.ypos -= self.speed
                elif self.target[0] > self.xpos and self.turns[0]:
                    self.direction = 0
                    self.xpos += self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.ypos += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.ypos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.xpos += self.speed
            elif self.turns[1]:
                if self.target[1] > self.ypos and self.turns[3]:
                    self.direction = 3
                    self.ypos += self.speed
                if self.target[1] < self.ypos and self.turns[2]:
                    self.direction = 2
                    self.ypos -= self.speed
                else:
                    self.xpos -= self.speed
        elif self.direction == 2:
            if self.target[0] < self.xpos and self.turns[1]:
                self.direction = 1
                self.xpos -= self.speed
            elif self.target[1] < self.ypos and self.turns[2]:
                self.direction = 2
                self.ypos -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.xpos and self.turns[0]:
                    self.direction = 0
                    self.xpos += self.speed
                elif self.target[0] < self.xpos and self.turns[1]:
                    self.direction = 1
                    self.xpos -= self.speed
                elif self.target[1] > self.ypos and self.turns[3]:
                    self.direction = 3
                    self.ypos += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.xpos -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.ypos += self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.xpos += self.speed
            elif self.turns[2]:
                if self.target[0] > self.xpos and self.turns[0]:
                    self.direction = 0
                    self.xpos += self.speed
                elif self.target[0] < self.xpos and self.turns[1]:
                    self.direction = 1
                    self.xpos -= self.speed
                else:
                    self.ypos -= self.speed
        elif self.direction == 3:
            if self.target[1] > self.ypos and self.turns[3]:
                self.ypos += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.xpos and self.turns[0]:
                    self.direction = 0
                    self.xpos += self.speed
                elif self.target[0] < self.xpos and self.turns[1]:
                    self.direction = 1
                    self.xpos -= self.speed
                elif self.target[1] < self.ypos and self.turns[2]:
                    self.direction = 2
                    self.ypos -= self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.ypos -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.xpos -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.xpos += self.speed
            elif self.turns[3]:
                if self.target[0] > self.xpos and self.turns[0]:
                    self.direction = 0
                    self.xpos += self.speed
                elif self.target[0] < self.xpos and self.turns[1]:
                    self.direction = 1
                    self.xpos -= self.speed
                else:
                    self.ypos += self.speed
        if self.xpos < -30:
            self.xpos = 900
        elif self.xpos > 900:
            self.xpos - 30
        return self.xpos, self.ypos, self.direction

                    

def draw_board():
    # num1 = (950 - 50) // 32 = 28
    num1 = ((Height - 50) // 32)
    # num2 = 900 // 30 = 30
    num2 = (Width // 30)
    color = 'blue'
    wall_thickness = 3 
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            
            if board[i][j] == 1:
               screen.blit(cheese2, (j * num2 + (0.5 * num2) - cheese2.get_width()//2, i * num1 + (0.5 * num1) - cheese2.get_height()//2)) 
            if board[i][j] == 2:
                screen.blit(cheese2, (j * num2 + (0.5 * num2) - cheese2.get_width()//2, i * num1 + (0.5 * num1) - cheese2.get_height()//2))
            if board[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1), (j * num2 + (0.5 * num2), i * num1 + num1), wall_thickness)
            if board[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)), (j * num2 + num2, i * num1 + (0.5 * num1)), wall_thickness)
            if board[i][j] == 5 or board[i][j] == 6 or board[i][j] == 7 or board[i][j] == 8:
                # Vertical segment 
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1 ),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), wall_thickness)
                # Horizontal segment 
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2 , i * num1 + (0.5 * num1)), wall_thickness)
            if board[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)), (j * num2 + num2, i * num1 + (0.5 * num1)), wall_thickness)


def draw_player(direction, counter, Mouse_x, Mouse_y):
    # 0 = right, 1 = left, 2 = up, 3 = down 
    if direction == 0:
        screen.blit(Player_Images[counter //10], (Mouse_x,Mouse_y))
    if direction == 1:
        screen.blit(pygame.transform.flip(Player_Images[counter //10], True,False),( Mouse_x,Mouse_y))                 
    if direction == 2:
        screen.blit(pygame.transform.rotate(Player_Images[counter //10], 90), (Mouse_x,Mouse_y))
    if direction == 3:
        screen.blit(pygame.transform.rotate(Player_Images[counter //10],270),(Mouse_x,Mouse_y))
    return pygame.Rect(Mouse_x, Mouse_y, 40, 40)


def check_collison(centerx, centery, current_direction):
    turns = [False, False, False, False]
    
    
    num1 = ((Height - 50) // 32) 
    num2 = (Width // 30)        
    num3 = 15 # Half the cell width (30/2) for turn check buffer
    
    # Check if the player is within the maze boundary (0 to 29 columns)
    if centerx // num2 < 29 and centerx // num2 > 0:
        r_index = int((centerx + num3) // num2)
        l_index = int((centerx - num3) // num2)
        u_index = int((centery - num3) // num1)
        d_index = int((centery + num3) // num1)
        
        # Check Right movement (0)
        if board[centery // num1][r_index] < 3:
            turns[0] = True
        
        # Check Left movement (1)
        if board[centery // num1][l_index] < 3:
            turns[1] = True
            
        # Check Up movement (2)
        if board[u_index][centerx // num2] < 3:
            turns[2] = True
            
        # Check Down movement (3)
        if board[d_index][centerx // num2] < 3:
            turns[3] = True
        
        # If moving Left/Right (0 or 1), allow Up/Down turn checks
        if current_direction == 0 or current_direction == 1:
            if centery % num1 < num3 or centery % num1 > num1 - num3:
                 if board[u_index][centerx // num2] < 3:
                    turns[2] = True
                 if board[d_index][centerx // num2] < 3:
                    turns[3] = True

        # If moving Up/Down (2 or 3), allow Left/Right turn checks
        if current_direction == 2 or current_direction == 3:
            if centerx % num2 < num3 or centerx % num2 > num2 - num3:
                if board[centery // num1][r_index] < 3:
                    turns[0] = True
                if board[centery // num1][l_index] < 3:
                    turns[1] = True
    else:
        turns[0] = True
        turns[1] = True
        
    return turns
    

def move_player (Mx, My, current_direction, allowed_turns):
    
    # Only move if the current direction is allowed
    if current_direction == 0 and allowed_turns[0]:
        Mx += player_speed
    elif current_direction == 1 and allowed_turns[1]:
        Mx -= player_speed
    elif current_direction == 2 and allowed_turns[2]:
        My -= player_speed
    elif current_direction == 3 and allowed_turns[3]:
        My += player_speed
    
    return Mx, My 

def check_eat(score, Mouse_x,Mouse_y):
    num1 = (Height -50)//32
    num2 = Width //30
    center_x = Mouse_x + 20 
    center_y = Mouse_y + 20 
    if 0 < Mouse_x < 870:
        if board[center_y // num1][center_x//num2] == 1 or board[center_y // num1][center_x//num2] == 2 :
            board[center_y//num1][center_x//num2] = 0
            score+=10
    return score 

def score_board(score):
    score_text = font.render(f'Score: {score}', True, 'white')
    screen.blit(score_text, (400, 425))

def game():
    global turns_allowed, direction
    
    run = True
    counter = 0
    direction = 0
    direction_command = 0
    Mouse_x = 430
    Mouse_y = 663
    score = 0
    targets = [(Mouse_x,Mouse_y)]
    Cat1_x = 56
    Cat1_y = 58
    Cat1_direction = 0 
    Cat2_y = 300
    Cat2_x=300
    Cat2_direction = 0 
    while run:
        timer.tick(fps)
        if counter < 19:
            counter += 1     
        else:
            counter = 0
        
        screen.fill('black')
        draw_board()
        
        # Player center 
        center_x = Mouse_x + 20 
        center_y = Mouse_y + 20 
        
        draw_player(direction, counter, Mouse_x, Mouse_y)
        cat1 = Catz(Cat1_x, Cat1_y, targets[0], cat_speed, Gray, Cat1_direction, Cat1_dead, Cat1_box,0)
        cat2 = Catz(Cat2_x, Cat2_y, targets[0], cat_speed, Spots, Cat2_direction, Cat2_dead, Cat2_box,1)

        turns_allowed = check_collison(center_x, center_y, direction)

        # Handle Player Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                # Set the requested direction (direction_command)
                if event.key == pygame.K_RIGHT:
                    direction_command = 0
                elif event.key == pygame.K_LEFT:
                    direction_command = 1
                elif event.key == pygame.K_UP:
                    direction_command = 2
                elif event.key == pygame.K_DOWN:
                    direction_command = 3
     
        # When player inputs direction change
        if direction_command == 0 and turns_allowed[0]:
            direction = 0
        elif direction_command == 1 and turns_allowed[1]:
            direction = 1
        elif direction_command == 2 and turns_allowed[2]:
            direction = 2
        elif direction_command == 3 and turns_allowed[3]:
            direction = 3

        # 4. Move the player based on the *current* active direction
        Mouse_x, Mouse_y = move_player(Mouse_x, Mouse_y, direction, turns_allowed)
        Cat1_x, Cat1_y, Cat1_direction = cat1.move_Gray()
        Cat2_x, Cat2_y, Cat2_direction = cat2.move_Gray()
        score = check_eat(score, Mouse_x, Mouse_y)
        score_board(score)


        # Tunnel logic: adjusted for 900 screen width and 40 pixel player size
        if Mouse_x > SCREEN_WIDTH:
            Mouse_x = -40 
        elif Mouse_x < -40:
            Mouse_x = SCREEN_WIDTH 
            
 
                    
                    
        pygame.display.flip()
    pygame.quit()


game()

#I referenced this youtube tutorial for this project --> https://www.youtube.com/watch?v=9H27CimgPsQ&t=6759s




