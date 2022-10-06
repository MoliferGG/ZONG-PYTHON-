# Interested People in reading code *THANK YOU FOR YOUR TIME*
# This is a more or less attemt in making the clasic game "PONG" , but with changes of my own free liking hence the name ZONG

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Importing neccesary modules

import pygame , random , sys 

pygame.init() # Initializing the pygame module


# Window HEIGHT and WIDTH a nd Declaration of window 

window_width , window_height = 700 , 500  
window = pygame.display.set_mode((window_width,window_height)) 
window.fill((100,200,100))

#Title of the window

pygame.display.set_caption("ZONG")


font = pygame.font.Font('freesansbold.ttf', 60)
text = font.render('ZONG' , True , (0,0,0))
textRect = text.get_rect()
textRect.center = (window_width//2 , window_height//2)
window.blit(text,textRect)


font = pygame.font.Font('freesansbold.ttf', 30)
text = font.render('Press ENTER to begin' , True , (0,0,0))
textRect = text.get_rect()
textRect.center = (window_width//2 , 350)
window.blit(text,textRect)


# Clock aka FPS

clock  = pygame.time.Clock()

# Some global variables for usage throughout the code

global white_ball ,  player_LiveR , click , scorePlayerOne, scorePlayerTwo , score

# Data for the ball 

ball_speed_x , ball_speed_y =  5, 5
randomPosX  = random.randrange(200 , 400) 
randomPosY = random.randrange(200 , 400) 
ball = pygame.Rect(randomPosX , randomPosY, 30, 30)


# Colours

WHITE = (255,255,255) 
white_ball =  (255,255,255)

# Keeps record of the player live

player_LiveR = 1
click = False
clickR = False


# Data for the paddles

Paddle_Length = 200 
paddleposY = (window_height/2) - (Paddle_Length/2) # Some basic math to display the paddle in the right position on the screen
paddleposY_A , paddleposY_D = paddleposY , paddleposY
 
# Score count

scorePlayerOne = 0
scorePlayerTwo = 0
score = 0


# Sounds for the game

game_OverSound = pygame.mixer.Sound('GameOver.wav')
bounce = pygame.mixer.Sound('HitPaddle.wav')
music = pygame.mixer.music.load('Background.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(2.0)

# Paddle function includes data related to displaying the two paddle

def Paddle (): 
    if clickR == True: 
        global paddle_One , paddle_Two , Paddle_Length , paddleposY , paddleposY_D , paddleposY_A
    
        paddle_One  = pygame.draw.rect(window , WHITE ,  
                                    pygame.Rect(5,paddleposY_A,15,Paddle_Length)) 
        paddle_Two  = pygame.draw.rect(window , WHITE ,  
                                    pygame.Rect(680,paddleposY_D,15,Paddle_Length)) 
    
    
# Line function draws the separation line between the window    


def Line (): 
    if clickR == True :
        line = pygame.draw.line(window, WHITE , (window_width/2 , 0 ) ,  
                            (window_width/2 , window_height)) 

# Ball function keeps check of the ball and how its reacting to its enviorment 

def Ball():
    if clickR == True:
        global ball_speed_x, ball_speed_y , scorePlayerTwo , scorePlayerOne
    
        ball.x += ball_speed_x
        ball.y += ball_speed_y
        if ball.top <= 0 or ball.bottom >= window_height:
            ball_speed_y *= -1
        if ball.left <= 0 or ball.right >= window_width:
            ball_speed_x *= -1
        
        if ball.colliderect(paddle_One):
            ball_speed_x *= -1
            bounce.play()
            scorePlayerOne +=1
        elif ball.colliderect(paddle_Two):
            ball_speed_x *= -1
            bounce.play()
            scorePlayerTwo +=1
            
# Keeps check of the score of each singular player

def Score():
    global scorePlayerTwo , scorePlayerOne , score
    
    if scorePlayerOne > scorePlayerTwo :
        score = scorePlayerOne
    if scorePlayerTwo > scorePlayerOne:
        score = scorePlayerTwo
    else :
        score = 'Equal'



# The input function keeps checks of the inputs given by the player        
      

def Input():
    global click , clickR
    if click == False:
        global paddle_One , paddle_Two, Paddle_Length , player_LiveR  , paddleposY , paddleposY_A , paddleposY_D 
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if player_LiveR == 0:
                    sys.exit()
            if click == False and clickR == False:
                click = True
            # Movement for Player One 
            if event.key == pygame.K_UP:
                if paddle_One.top == 0 :
                    paddleposY_A +=5
                else :
                    paddleposY_A -=5
            if event.key == pygame.K_DOWN:
                if paddle_One.bottom == window_height:
                    paddleposY_A -=5
                else:
                    paddleposY_A +=5
            if event.key == pygame.K_LEFT:
                if paddle_Two.top == 0 : 
                    paddleposY_D +=5
                else :
                    paddleposY_D -=5
            if event.key == pygame.K_RIGHT:
                if paddle_Two.bottom == window_height : 
                    paddleposY_D -=5
                else :
                    paddleposY_D +=5
            

# Death function as the name suggests handles the death of the ball when it goes out of the screen
            
            
def Death():
    if clickR == True :
        global  player_LiveR , ball_speed_x , ball_speed_y , white_ball , ball , PlayerOne
        if ball.x >660:
            game_OverSound.play()
            player_LiveR  = 0
            ball_speed_y = 0
            ball_speed_x = 0
            white_ball = (0,0,0)
            ball = pygame.Rect(30 , 0, 0, 0)
            PlayerOne = True # Keeps check who won (Sluggy but gets the work done.)
        elif ball.x <= 10 :
            game_OverSound.play()
            player_LiveR  = 0
            ball_speed_x = 0
            ball_speed_y = 0
            white_ball = (0,0,0)
            ball = pygame.Rect(30 , 0, 0, 0)
            PlayerOne = False
        

# End Screen function shows the end screen (Cast Data) and score and the name of the player who has won        
  

def EndScreen():
    if clickR == True :
        global player_LiveR , PlayerOne , score  , scorePlayerTwo, scorePlayerOne 
        if player_LiveR == 0:
            pygame.mixer.music.stop()
            window.fill((0,0,0))
            Score()
            scoreholder = str(score)
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render('Oh no you lost press ESCAPE to close.' , True , (255,255,255))
            textRect = text.get_rect()
            textRect.center = (window_width//2 , window_height //2)
            window.blit(text,textRect)
        
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render(str('Score : ' + scoreholder) , True , (255,255,255))
            textRect = text.get_rect()
            textRect.center = (window_width//2 , 300)
            window.blit(text,textRect)

            if scorePlayerOne > scorePlayerTwo:
                font = pygame.font.Font('freesansbold.ttf', 30)
                text = font.render('Player One has won.' , True , (255,255,255))
                textRect = text.get_rect()
                textRect.center = (window_width//2 , 365)
                window.blit(text,textRect)
            elif scorePlayerTwo > scorePlayerOne:
                font = pygame.font.Font('freesansbold.ttf', 30)
                text = font.render('Player Two has won.' , True , (255,255,255))
                textRect = text.get_rect()
                textRect.center = (window_width//2 , 365)
                window.blit(text,textRect)
            font = pygame.font.Font('freesansbold.ttf', 14)
            text = font.render('Made by Aranya Mohanty // Molifer.' , True , (255,255,255))
            textRect = text.get_rect()
            textRect.center = (570 , 470)
            window.blit(text,textRect)  


def mainMenu():
    global click ,  clickR
    if click == True :
        if event.type == pygame.KEYDOWN:
            click = False
            clickR = True

def GameScore():
    global scorePlayerOne , scorePlayerTwo
    if clickR == True :
        ScoreP_ONE = str(scorePlayerOne)
        ScoreP_TWO = str(scorePlayerTwo)
    
        font = pygame.font.Font('freesansbold.ttf', 60)
        text = font.render(ScoreP_ONE , True , (0,0,0))
        textRect = text.get_rect()
        textRect.center = (230 , 30)
        window.blit(text,textRect)
    
        font = pygame.font.Font('freesansbold.ttf', 60)
        text = font.render(ScoreP_TWO , True , (0,0,0))
        textRect = text.get_rect()
        textRect.center = (530 , 30)
        window.blit(text,textRect)

# Main Loop Helper variable

running  = True        

# Main loop for running the program 

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            
    mainMenu()
    
    if clickR == True :
        window.fill((100,100,100))
        
    Line()
    Input() 
    Paddle()
    Ball()
    EndScreen()
    Death()
    GameScore()
    
    
    if clickR == True:
        pygame.draw.ellipse(window , white_ball , ball) # Just draws the ball [using ellipse instead of circle for easier calculation]
    
    #Updating the window
    pygame.display.flip()
    clock.tick(60) 
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
