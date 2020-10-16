import pygame
def bounce():
    global ball_y_speed, ball_x_speed,p2_score,p1_score

    if ball.top <= 0 or ball.bottom >= 800:
        ball_y_speed *=-1
    if ball.colliderect(p1) or ball.colliderect(p2):
        ball_x_speed *=-1
    if ball.left <= 0:
        p1_score+=1
        center()
       
    if ball.right >= 1000:
        p2_score+=1
        center()
        
def borders():
    if p1.top <=0:
        p1.top = 0
    if p1.bottom >= 800:
        p1.bottom = 800
    if p2.top <=0:
        p2.top = 0
    if p2.bottom >= 800:
        p2.bottom = 800
def computer():
    if p2.top < ball.top:
        p2.top +=p2_speed
    if p2.bottom > ball.top:
        p2.bottom = p2.bottom - p2_speed
    
def center():
    ball.center=(494,393)

    
    

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
LGREY = (218, 218, 218)
BLUE = (0, 0, 255)
YELLOW =(255,255,0)
pygame.init()


size = (1000, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pong")
done = False





 
    # --- Game logic should go here
game_font = pygame.font.Font("freesansbold.ttf",32)
ball_x_speed = 5
ball_y_speed = 5
p1_score = 0
p2_score = 0
p1_speed = 0
p2_speed = 6
x_speed2 = 0
y_speed2= 0
x_pos = 494
y_pos = 393
x_offset =4
y_offset =4
ycord=400
ycord2=400
p1 = pygame.Rect(30, ycord, 10, 200)
p2 =  pygame.Rect(970, ycord2, 10, 200)
ball = pygame.Rect(x_pos, y_pos, 12.5 , 12.5)
clock = pygame.time.Clock()

# Current position


 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
 
    if event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
        
        if event.key == pygame.K_UP:
            p1_speed = -6
        elif event.key == pygame.K_DOWN:
            p1_speed = 6
        
 
    # User let up on a key
    if event.type == pygame.KEYUP:
        
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            p1_speed = 0
        
    # --- Game Logic
    ball.x += ball_x_speed
    ball.y += ball_y_speed
    bounce()
    p1.y += p1_speed
    
    borders()
    computer()
    
    # Move the object according to the speed vector.
    
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    p1_text = game_font.render(f"{p1_score}",False, WHITE)
    screen.blit(p1_text,(514,373))
    p2_text = game_font.render(f"{p2_score}",False, WHITE)
    screen.blit(p2_text,(474,373))
    # --- Drawing code should go here
    pygame.draw.rect(screen, WHITE,p1)
    pygame.draw.rect(screen, WHITE, p2)
    pygame.draw.ellipse(screen , WHITE, ball)
    pygame.draw.aaline(screen, LGREY, (500, 0), (500,800))
    
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
