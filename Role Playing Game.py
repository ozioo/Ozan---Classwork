import sys
import time
import pygame
import random 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
block_count=0
enemy_count=0
block_temp_x=[]
block_temp_y=[]
spawn_2= False
spawn_3= False
game_over=False

map1 = """                                                      
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
w     www                              w
w             wwww                     w
w                                      w
w                                      w
w                                      w
w                                      w
w                                      w
w     www                              w
w             wwww                     w
w                                      w
w            wwwww                     w
w                                      w
w                                  w   w
w                                      w
w    wwww                              w
www    w                               w
w      w                www            w 
w   wwwww                              w
w    wwww                          w   w
w    w                           w   w w   
w                                     ww   
w   wwwwww                      www wwww   
w     w                                w   
w                                      w
w                        w             w
w                        w             w
w                        wwww          w
w                                      w 
w                                      w
w                        w             w
w                        wwww          w
w                        w             w
w                        wwww          w
w   wwwww                              w
w    wwww                          w   w
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""

map2="""                                                      
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
www    w           w                   w
w      w           w    www            w 
w      w           w                   w
w      wwwww          w                w
w      wwwww          w                w
w     www                              w
w             wwww                     w
w                                      w
w            wwwww                     w
w   wwwwww                      www wwww   
w     w                                w   
w                                      w
w                                  w   w
w                                      w
w    wwww          w                   w
www    w           w                   w
w      w           w    www            w 
w   wwwww          w                   w
w    wwww          w               w   w
w                  w             w   w w   
w                  w                  ww   
w     wwwwwwwwwwwwwwwwwwwwwwwwwwwww wwww   
w     w                                w   
w                                      w
w                        w             w
w                        w             w
w                        wwww          w
w                                      w 
w                                      w
w      w           w    www            w 
w   wwwww          w                   w
w    w            w              w   w w
w                w                    ww
w    wwww          w               w   w
w                                      w
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""

map3="""                                                      
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
w                                      w
w                                      w
w                                      w
w     www                              w
w             wwww                     w
w                              ww      w
w       wwwwwwwwww             ww      w
w        www    ww             ww      w
w                         ww   wwwwww  w
w                         ww           w
w    wwww                 ww           w
www    w                  ww           w
w      w                wwww           w
w   wwwww                              w
w    wwww                          w   w
w    w            w              w   w w
w                w                    ww
w   wwwwww      w               www wwww
w     w        w                       w
w             w                        w
w            w                         w
w           w                          w
w          w                           w
w         w                            w
w        w                             w
w       w                              w
w                        w             w
w     wwww                  w          w
w                        wwww          w
w  ww                       ww         w
w     www                    ww        w
w   www                      ww        w
w                         ww           w
w                                      w
w                                      w
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)

        self.health=100
        self.score=0
        self.keys=0
        self.money=0
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
class Enemy(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    def __init__(self, x, y, color):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x =4
        self.y=-4
        self.health=100
    def update(self):
        self.rect.y += self.y
        self.rect.x += self.x
        if self.rect.x <= 25:
            self.rect.x=25
            self.x*=-1  
        if self.rect.x >= 975:
            self.rect.x=975
            self.x*=-1  
        if self.rect.y <= 50:
            self.rect.y=50 
            self.y*=-1 
        if self.rect.y >= 900:
            self.rect.y=900
            self.y*=-1 
class health(pygame.sprite.Sprite):
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
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(WHITE)
        self.x=2
        self.y=2        
        self.rect = self.image.get_rect()
        
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 11   
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
        self.rect = self.image.get_rect()

 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
def tiles(map_id):
    global tile
    for y, line in enumerate(map_id):
        for x, c in enumerate(line):
            if c == "w":
                block = Block(BLACK, (24), (24))
                block.rect.x = x*25
                block.rect.y = y*25
                global block_count
                global temp_x
                global temp_y
                block_count +=1
                block_temp_x.insert(block_count,x*25) 
                block_temp_y.insert(block_count,y*25) 
                block_list.add(block)
                
map1 = map1.splitlines()
map2 = map2.splitlines()
map3 = map3.splitlines()                
pygame.init()
font= pygame.font.Font('freesansbold.ttf',30)
block_list = pygame.sprite.Group()
player = Player(500, 500)
all_sprites_list = pygame.sprite.Group()

bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
all_sprites_list.add(player)

def collisions():
    global enemy_x
    global enemy_y
    for block in block_list:
 
        # See if it hit a block
        boundary_hit_list = pygame.sprite.spritecollide(block, enemy_list, False)
 
        # For each block hit, remove the bullet and add to the score
        for enemy in boundary_hit_list:
            switch=random.randrange(0,2)
            if switch == 0:
                enemy.x *=-1
            if switch == 1:
                enemy.y *=-1
            
            

    for enemy in enemy_list:
 
        # See if it hit a block
        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for enemy in enemy_hit_list:
            enemy_list.remove(enemy)
            all_sprites_list.remove(enemy)
            player.health -= 20
            player.keys+= 1
            
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
        # For each block hit, remove the bullet and add to the score
        for enemy in block_hit_list:
            enemy_list.remove(enemy)
            all_sprites_list.remove(enemy)
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            player.score+= 10
            player.keys+= 1
            

            
    for block in block_list:

        wall_hit_list = pygame.sprite.spritecollide(block, bullet_list, True)

        for bullet in  wall_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    
    return
def enemy_spawn(number):

    temp_x=0
    temp_y=0
    for i in range(number):
    
        e_x=random.randrange(150,850)
        e_y=random.randrange(150,850)
        if e_x == temp_x and e_y == temp_y:
            e_x=random.randrange(150,850)
            e_y=random.randrange(150,850)
        for l in range(block_count):
            if e_x == block_temp_x[l] and e_y == block_temp_y[l] : 
                e_x-=70
                e_y-=70             
        enemy =Enemy(e_x,e_y,(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
        enemy_list.add(enemy)
        all_sprites_list.add(enemy)
        temp_x = e_x
        temp_y = e_y
        global enemy_count
        enemy_count=+1
def scoreboard():
    score_text = font.render('Score : ' + str(player.score), True, (0, 255,255))
    screen.blit(score_text, (0,970))
    score_text = font.render('Health : ' + str(player.health), True, (0, 255,255))
    screen.blit(score_text, (250,970)) 
    score_text = font.render('Keys : ' + str(player.keys), True, (0, 255,255))
    screen.blit(score_text, (500,970))
    score_text = font.render('Money : ' + str(player.money), True, (0, 255,255))
    screen.blit(score_text, (750,970))

number=5

enemy_spawn(number)

# Set the width and height of the screen [width, height]
size = (1000, 1100)
screen = pygame.display.set_mode(size)
tiles(map1)
player.walls = block_list


pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-15, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(15, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -15)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 15)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(15, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-15, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 15)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -15)
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
            
            # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
            # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x +17
                bullet.rect.y = player.rect.y
            # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
 
    # --- Game logic should go here
    all_sprites_list.update()


    collisions() 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(RED)
    if player.health == 0:
        print("you have died")
        sys. exit()
    req_amount=5
    if player.keys == req_amount :
        
        block_list.empty()
        if spawn_2== False:
            tiles(map2)
            spawn_3= True
        elif spawn_3==True:
            tiles(map3)
            spawn_3= False
            
        else:
            game_over=True

        if game_over==True:
            print("you have won")
            sys. exit()

            

            


            
        block_temp_x=[]
        block_temp_y=[]
        block_count=0


        if game_over!=True:
            enemy_spawn(5)

        
        player.keys=0

        spawn_2= True
   

 
    # --- Drawing code should go here
    scoreboard()
    block_list.draw(screen)
    all_sprites_list.draw(screen)



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(30)
 
# Close the window and quit.
pygame.quit()
