import pygame
import sys
import os
import random
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()

# we will declare global constant definitions

SPEED = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE #we willl keep both food and the size the same
SEPARATION = 10 #separation betwwen two paxels
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"up":1,"Down":2, "Left":3, "Right":4}

#we will initialise screen
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_HEIGHT),pygame.HWSURFACE)

#we have hw surface which stands for hardware surface to using memory on the video card

#Resources
score_font = pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None,28)
game_over_font = pygame.font.Font(None,48)
play_again_font = score_numb_font
score_msg = score_font.render("Score : ",1,pygame.color("green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0,0,0) #we will fill background color as black
black = pygame.Color(0,0,0)

#for clock at the left corner
gameClock = pygame.time.Clock()

def checkCollision(posA,As,posB, Bs):
    if(posA.x , posB.x+Bs and posA.x+As > posB.x and posA.y < posB.y+Bs 
       and posA.y+As > posB.y):
        return True
    return False

#to check boundries here we are not limiting boundries

def checkLiits(snake):
    if (snake.x > SCREEN_WIDTH):
        snake.x = SNAKE_SIZE
        if(snake.x < 0): #this will be checked when some part in on other side and some on opposite side
            snake.x = SCREEN_WIDTH - SNAKE_SIZE
        if(snake.y > SCREEN_HEIGHT):
            snake.y = SNAKE_SIZE
        if(snake.y < 0): #this also same half
            snake.y - SCREEN_HEIGHT - SNAKE_SIZE
    
    
#we will make class for food of the snake, named apple
class Apple:
    def __init__(self,x,y,state):
        self.x = x
        self.y = y 
        self.state = state
        self.color = pygame.color.Color("orange") #color of food
        
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,APPLE_SIZE,APPLE_SIZE),0)
        
class segment:
    #initially snake will move un up direction
    self.x = x
    self.y = y
    self.direction = KEY["UP"]
    self.color = "white"
    
class snake:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.direction = KEY["UP"] 
        self.stack = []
        self.stack.append(self)
        blackBox = segment(self.x, self.y + SEPARATION)
        blackBox.direction = KEY["up"]
        blackBox.color = "NULL"
        self.stack.append(blackBox)
        
        
    #we will define moves of the snake
    
    def move(self):
        last_element = len(self.stack) -1
        while(last_element != 0):
            self.stack[last_element].direction = self.stack[last_element].direction
            self.stack[last_element].x = self.stack[last_element -1].x 
            self.stack[last_element].y = self.stack[last_element-1].y 
            last_element -=1
            if(len(self.stack) < 2):
                last_element = self
            else:
                last_segment = self.pop(last_element)
            last_segment.directiom = self.stack[0].direction
            if(self.stack[0].direction == KEY["UP"]):
                last_segment.y = self.stack[0].y - (SPEED * FPS)
            elif(self.stack[0].direction == KEY["DOWN"]):
                last_segment.y = self.stack[0].y + (SPEED * FPS)
            elif(self.stack[0].direction == KEY["LEFT"]):
                last_segment.x = self.stack[0].x - (SPEED * FPS)
            elif(self.stack[0].direction == KEY["RIGHT"]):
                last_segment.x = self.stack[0].x + (SPEED * FPS)
                self.stack.insert(0,last_segment)
    
    def getHead(self): #head of the snake
        return(self.stack[0]) #it will always be 0 index
    
     #now when the snake eat its food it will grow so for that we will add that food to stack
    
    def grow(self):
        last_element = len(self.stack) -1
        self.stack[last_element].direction = self.stack[last_element].direction
        if(self.stack[last_element].direction == KEY["UP"]):
            newSegment = segment(self.stack[last_element].x, self.stack[last_element].y + SNAKE_SIZE)
            blackBox = segment(newSegment.x , newSegment.y-SEPARATION)
            
        elif(self.stack[last_element].direction == KEY["DOWN"]):
            newSegment = segment(self.stack[last_element].x, self.stack[last_element].y +SNAKE_SIZE)
            blackBox = segment(newSegment.x, newSegment.y+SEPARATION)

        elif(self.stack[last_element].direction == KEY["LEFT"]):
            newSegment = segment(self.stack[last_element].x - SNAKE_SIZE, self.stack[last_element].y) 
            blackBox = segment(newSegment.x - SEPARATION, newSegment.y)
            
        elif(self.stack[last_element].direction == KEY["RIGHT"]):
            newSegment = segment(self.stack[last_element].x + SNAKE_SIZE, self.stack[last_element].y) 
            blackBox = segment(newSegment.x + SEPARATION, newSegment.y)
            
        blackBox = "NULL"
        self.stack.append(newSegment)
        self.stack.append(blackBox)
            
#we will define keys

def getkey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["up"]
            elif event.key == pygame.K_DOWN:
                return KEY["DOWN"]
            elif event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            elif event.key == pygame.K_RIGHT:
                return KEY["RIGHT"]
            
            #FOR EXIT
            elif event.key == pygame.K_ESCAPE:
                return "exit"
            #if we want to continue playing again
            elif event.key == pygame.K_y:
                return "yes"
            #if we don't want to play game
            elif event.key == pygame.K_n:
                return "no"
        if event.type == pygame.QUIT:
            sys.exit(0)
            
            
def endGame():
    message = game_over_font.render("Game Over",1,pygame.color("white")) 
    message_play_again = play_again_font.render("Play Again? (Y/N)",1,pygame.color("green"))
    screen.blit(message,(320,240))
    screen.blit(message_play_again,(320+12,240+40))
    
    pygame.display.flip()
    pygame.display.update()
    
    mkey = getkey()
    while(mkey != "exit"):
        if(mkey == "yes"):
            main()
        elif(mkey == "no"):
            break
        mkey = getkey()
        gameClock.tick(FPS)
    sys.exit
    
    
def drawScore(score):
    score_numb = score_numb_font.render(str(score),1,pygame.Color("red"))
    screen.blit(score_msg, (SCREEN_WIDTH - score_msg_size[0]-60,10))
    screen.blit(score_numb,(SCREEN_WIDTH - 45,14))
    
def drawGameTime(gameTime):
    game_time = score_font.render("Time:" , 1, pygame.color("white"))
    game_time_numb = score_numb_font.render(str(gameTime/1000),1,pygame.color("white"))
    screen.blit(game_time,(30,10))
    screen.blit(game_time_numb,(105,14))
    

    
    
def main():
    print("jay")
            
        