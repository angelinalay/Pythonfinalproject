import pygame
import math

pygame.init()

Width = 900
Height = 950
screen = pygame.display.set_mode([Width, Height])
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
Gray = pygame.transform.smoothscale(cat1, (15,15))
cat2 = pygame.image.load("Orangecat.png").convert_alpha()
Orange = pygame.transform.smoothscale(cat2, (15,15))
cat3 = pygame.image.load("Orange_Whitecat.png").convert_alpha()
Orange_white = pygame.transform.smoothscale(cat3, (15,15))
cat4 = pygame.image.load("Spotscat.png").convert_alpha()
Spots = pygame.transform.smoothscale(cat4, (15,15))

Mouse1 = pygame.image.load("Mouse_open.png").convert_alpha()
Mouse_open = pygame.transform.smoothscale(Mouse1, (40,40))
Mouse2 = pygame.image.load("Mouse_closed.png").convert_alpha()
Mouse_closed = pygame.transform.smoothscale(Mouse2, (40,40))

#Player/Mouse variables for displaying and movement 
Player_Images = []
for i in range(1, 3):
    Player_Images.append(Mouse_open)
    Player_Images.append(Mouse_closed)

counter = 0
direction = 0
turns = [False, False, False, False]
player_speed = 2


def draw_board():
    num1 = ((Height - 50) // 32)
    num2 = (Width // 30)
    color = 'blue'
    wall_thickness = 1
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
               screen.blit(cheese2, (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1))) 
            if board[i][j] == 2:
                screen.blit(cheese2, (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)))
            if board[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1), (j * num2 + (0.5 * num2), i * num1 + num1), wall_thickness)
            if board[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)), (j * num2 + num2, i * num1 + (0.5 * num1)), wall_thickness)
            if board[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1], 0, PI / 2, wall_thickness)
            if board[i][j] == 6:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, wall_thickness)
            if board[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI, 3 * PI / 2, wall_thickness)
            if board[i][j] == 8:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2, 2 * PI, wall_thickness)
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





def check_collison(centerx, centery, current_direction):
    turns = [False, False, False, False]
    num1 = ((Height - 50) // 32)
    num2 = (Width // 30)
    num3 = 15
    # check collision based on center x and center y of player +/- num3 
    if centerx//num2  < 29 and centerx//num2 > 0:
        r_index = int((centerx + num3) // num2)
        l_index = int((centerx - num3) // num2)
        u_index = int((centery - num3) // num1)
        d_index = int((centery + num3) // num1)
        
        if board[centery // num1][r_index] < 3:
            turns[0] = True
    
        if board[centery // num1][l_index] < 3:
            turns[1] = True
       
        if board[u_index][centerx // num2] < 3:
            turns[2] = True
            
        if board[d_index][centerx // num2] < 3:
            turns[3] = True
       #check turn checks
        if current_direction == 0 or current_direction == 1:
            # Check if player is near center vertically to allow vertical turns
            if centery % num1 < num3 or centery % num1 > num1 - num3:
                 if board[u_index][centerx // num2] < 3:
                    turns[2] = True
                 if board[d_index][centerx // num2] < 3:
                    turns[3] = True

        # If moving Up/Down (2 or 3), allow Left/Right turn checks
        if current_direction == 2 or current_direction == 3:
            # Check if player is near center horizontally to allow horizontal turns
            if centerx % num2 < num3 or centerx % num2 > num2 - num3:
                if board[centery // num1][r_index] < 3:
                    turns[0] = True
                if board[centery // num1][l_index] < 3:
                    turns[1] = True

    else:
        turns[0] = True
        turns[1] = True
    return turns
    

def move_player (Mx, My, direction, turns_allowed):
    if direction == 0 :
        Mx += player_speed
    elif direction == 1 :
        Mx -= player_speed
    if direction == 2 :
        My -= player_speed
    elif direction == 3 :
        My += player_speed
    return Mx, My 


def game():
    run = True
    counter = 0
    direction = 0
    direction_command = 0
    Mouse_x = 430
    Mouse_y = 682
    turns_allowed = [False, False, False, False]

    while run:
        timer.tick(fps)
        if counter < 19:
            counter += 1     
        else:
            counter = 0
        screen.fill('black')
        draw_board()
        draw_player(direction, counter, Mouse_x, Mouse_y)

        center_x = Mouse_x + 20
        center_y = Mouse_y + 20 

        turns_allowed = check_collison (center_x, center_y, direction)
        

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction_command = 0
                if event.key == pygame.K_LEFT:
                    direction_command = 1
                if event.key == pygame.K_UP:
                    direction_command = 2
                if event.key== pygame.K_DOWN:
                    direction_command = 3
     #gives mouse movement similar to joystick so it moves in given direction only when key is pressed down                
            if direction_command == 0 and turns_allowed[0]:
                direction = 0
            elif direction_command == 1 and turns_allowed[1]:
                direction = 1
            elif direction_command == 2 and turns_allowed[2]:
                direction = 2
            elif direction_command == 3 and turns_allowed[3]:
                direction = 3

        Mouse_x, Mouse_y = move_player(Mouse_x, Mouse_y, direction, turns_allowed)
        draw_player(direction, counter, Mouse_x, Mouse_y)


# if Mouse moves too far to right it is moved to the left, and vice versa 
        if Mouse_x > 900:
            Mouse_x = -40 
        elif Mouse_x < -40:
            Mouse_x = 900
            
 
                    
                    
        pygame.display.flip()
    pygame.quit()


game()
