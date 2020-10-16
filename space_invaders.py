"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/qbEEcQXw8aw
"""
 
import pygame
import random
pygame.init()
 
# Set the height and width of the screen
screen_width = 1000
screen_height = 800
score = 0
screen = pygame.display.set_mode([screen_width, screen_height])
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

 
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, color, x, y):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        
        #self.width=100
        #self.height=100
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.counter = 0
        self.count = 0
        self.speed = 8
  
         # If block is too far down, reset to top of screen.
        
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
    
        
 
    def update(self):
        global speed
  
         # Move block down one pixel
        self.rect.x += self.speed
        self.counter +=1
        if self.counter == 55:
             self.rect.y +=10
             self.speed *=-1
             self.counter = 0

     
        
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
        
 
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        self.rect.x = pos[0]
 
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()
        
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 11
font= pygame.font.Font('freesansbold.ttf',12)
over_font = font= pygame.font.Font('freesansbold.ttf',40)

"""def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text,(450,350))"""

    
    
    
    

    
 
# Initialize Pygame


    
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

bullet_list = pygame.sprite.Group()
BLOCK_COUNT=0
count=2
for i in range(60, 260, 50):
    
    for x in range(10, 510, 50):
    # This represents a block
        x=x+50
        print(x)
        block = Block(GREEN, x, i)
        BLOCK_COUNT+=1
        
         
        # Set a random location for the block
       
     
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)
        
 
# Create a red player block
#player = Player(RED, 20, 15)
#all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
player = Player()
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
game_over = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 

player.rect.y = 780
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        count = 0
        if event.type == pygame.QUIT:
            done = True
        
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            while count < 1:
            
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                count+=1
 
    # --- Game logic
 
    # Call the update() method on all the sprites
    all_sprites_list.update()
    
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 10
            BLOCK_COUNT-=1
            print(score)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)


    for block in block_list:
        if block.rect.y > 750:
            game_over = True
            all_sprites_list.remove(player)
            for block in block_list:
                block_list.remove(block)
                all_sprites_list.remove(block)
                screen.fill(WHITE)



                
                
            
        
        
 
    # --- Draw a frame
 
    # Clear the screen
    screen.fill(BLACK)
    score_text = font.render('Score : ' + str(score), True, (255, 255,255))
    screen.blit(score_text, (0,0))
 
    # Draw all the spites
    all_sprites_list.draw(screen)
    if game_over == True:
        over_text = over_font.render('GAME OVER', True, (255, 255, 255))
        screen.blit(over_text,(450,350))
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(20)
 
pygame.quit()
