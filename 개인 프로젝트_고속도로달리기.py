import pygame
import random
from time import sleep

screen_width = 460
screen_height = 680
BLUE = (0,0,255)
RED = (255,0,0)
carRoad_height = 680

def car1(x,y):
    screen.blit(MyCar,(x,y))


def badcar1(BadCar_x,BadCar_y):
    screen.blit(BadCar,(BadCar_x, BadCar_y))


def badcar2(BadCar2_x,BadCar_y):
    screen.blit(BadCar2,(BadCar2_x, BadCar2_y))


    
def backGround(carRoad,x,y):
    global screen, carRoad1, carRoad2
    screen.blit(carRoad,(x,y))


def inscreen():
    global x, y
    
    if x < 0:
        x=0
    elif x > 380:
        x = 380
    elif y < 0:
        y = 0
    elif y > 580:
        y = 580


def Message(text):
    global screen
    textfont = pygame.font.Font(None, 80)
    text = textfont.render(text, True, RED)
    textpos = text.get_rect()
    textpos.center = (screen_width/2, screen_height/2)
    screen.blit(text,textpos)
    pygame.display.update()
    sleep(2)
    Gamestart()


def crashed():
    global screen
    Message("Crashed!!")


def RoadScore(count):
    global screen, White
    font = pygame.font.SysFont(None, 25)
    text = font.render("SCORE: " + str(count), True, BLUE)
    screen.blit(text,(0,0))    


def Gamestart():
    global screen, FPS, MyCar, BadCar, carRoad1, carRoad2,\
           x, y, BadCar_x, BadCar_y, BadCar2_x, BadCar2_y

    x = 250
    y = 480
    x_move = 0
    y_move = 0
    BadCar_x = 0
    BadCar_y = -120
    BadCar2_x = 380
    BadCar2_y = -120

    carRoad1_y = 0
    carRoad2_y = -carRoad_height
    carRoad1_x = 0
    carRoad2_x = 0

    MyScore = 0

    OUTSCREEN = False
    while not OUTSCREEN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                OUTSCREEN = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
                elif event.key == pygame.K_DOWN:
                    y_move = 5
                elif event.key == pygame.K_LEFT:
                    x_move = -5
                elif event.key == pygame.K_RIGHT:
                    x_move = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0

        inscreen()

        if (BadCar_y <= (y+60) and (BadCar_y+120) >= (y+60)) and \
        (BadCar_x <= (x+40) and (BadCar_x+80) >= (x+40)):
            crashed()
        if (BadCar2_y <= (y+60) and (BadCar2_y+120) >= (y+60)) and \
        (BadCar2_x <= (x+40) and (BadCar2_x+80) >= (x+40)):
            crashed()
            
        y += y_move
        x += x_move

        carRoad1_y += 3
        carRoad2_y += 3

        MyScore += 3

        BadCar_y += random.randint(5,20)
        if BadCar_y >= 680:
            BadCar_x = random.randint(0,380)
            BadCar_y = -120

        BadCar2_y += random.randint(5,20)
        if BadCar2_y >= 680:
            BadCar2_x = random.randint(0,380)
            BadCar2_y = -120
        
        if carRoad1_y >= carRoad_height:
            carRoad1_y = -carRoad_height

        if carRoad2_y >= carRoad_height:
            carRoad2_y = -carRoad_height

        backGround(carRoad1, carRoad1_x, carRoad1_y)
        backGround(carRoad2, carRoad2_x, carRoad2_y)
        
        car1(x,y)
        badcar1(BadCar_x,BadCar_y)
        badcar2(BadCar2_x,BadCar2_y)

        RoadScore(MyScore)
        
        pygame.display.update()
        FPS.tick(60)

    pygame.quit()
    exit()



def initGame():
    global screen, FPS, MyCar, BadCar, BadCar2, carRoad1, carRoad2, x, y

    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("고속도로 달리기")
    MyCar = pygame.image.load("mycar.jpg")
    BadCar = pygame.image.load("badcar.jpg")
    BadCar2 = pygame.image.load("badcar2.jpg")
    carRoad1 = pygame.image.load("road.jpg")
    carRoad2 = pygame.image.load("road.jpg")
    
    FPS = pygame.time.Clock()

    Gamestart()


initGame()
