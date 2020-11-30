"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
 
import pygame
import random
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
 
 
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([40, 40])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health=100
        self.money=0
        self.score=0
        self.keys=0

    def update(self):
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= 15
            elif event.key == pygame.K_RIGHT:
                player.rect.x += 15
            elif event.key == pygame.K_UP:
                player.rect.y -= 15
            elif event.key == pygame.K_DOWN:
                player.rect.y += 15
        if player.rect.y > 920:
            player.rect.y = 920
        if player.rect.y < 40:
            player.rect.y = 40
        if player.rect.x > 920:
            player.rect.x = 920
        if player.rect.x < 40:
            player.rect.x = 40
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

class Enemy(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    def __init__(self, x, y, color):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([40, 40])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health=100
 
# Call this function so the Pygame library can initialize itself
pygame.init()
font= pygame.font.Font('freesansbold.ttf',30)

screen = pygame.display.set_mode([1000, 1100])
 
# Set the title of the window
pygame.display.set_caption('RPG')
 
# Create the player paddle object
player = Player(500, 500)
all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
all_sprites_list.add(player)
for i in range(25):
    # This represents a block
    block = Block(RED, 40, 40)     
    # Set a random location for the block
    block.rect.x = 40*i
    block.rect.y = 0
     
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
for i in range(25):
    # This represents a block
    block = Block(RED, 40, 40)
     
    # Set a random location for the block
    block.rect.x = 40*i
    block.rect.y = 960
     
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
for i in range(25):
    # This represents a block
    block = Block(RED, 40, 40)
     
    # Set a random location for the block
    block.rect.x = 0
    block.rect.y = 40*i
     
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
for i in range(25):
    # This represents a block
    block = Block(RED, 40, 40)
     
    # Set a random location for the block
    block.rect.x = 960
    block.rect.y = 40*i
     
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

for i in range(3):
    enemy =Enemy(random.randrange(41,969),random.randrange(41,969),(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
    enemy_list.add(enemy)
    all_sprites_list.add(enemy)

 
clock = pygame.time.Clock()
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprites_list.update()


 

 
    # -- Draw everything
    # Clear screen
    screen.fill(BLACK)
    score_text = font.render('Score : ' + str(player.score), True, (0, 255,255))
    screen.blit(score_text, (0,1000))
    score_text = font.render('Health : ' + str(player.health), True, (0, 255,255))
    screen.blit(score_text, (250,1000)) 
    score_text = font.render('Keys : ' + str(player.keys), True, (0, 255,255))
    screen.blit(score_text, (500,1000))
    score_text = font.render('Money : ' + str(player.money), True, (0, 255,255))
    screen.blit(score_text, (750,1000))

 
    # Draw sprites
    all_sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()
 
    # Pause
    clock.tick(40)
 
pygame.quit()
