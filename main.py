import pygame, math, random
#Go here for inf: https://www.pygame.org/docs/ref/draw.html
#PYTHON 3.11.5!!!

pygame.init()

w = 1280
h = 720
size = (w, h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
jumpClock = pygame.time.Clock()
g = 3

def drawBG(act):
    if act == 1:
        bg = pygame.image.load("testbg.png").convert()
        bg = pygame.transform.scale(bg, (1280, 720))
        screen.blit(bg, (0,0))
    elif act == 2:
       pass

def drawFG():
    #pass
    pygame.draw.rect(screen, "red", (0,670,1280,720))

def drawChar(charX, charY, charHeight, charLen):
    #pass
    pygame.draw.rect(screen, "blue", (charX, charY, charLen, charHeight))
#squareX = 100
#squareY = 100

running = True
charX = 595 #top left
charY = 550 #top left is coordinates
charHeight = 120
charLen = 90
isJumping = False
goingUp = True
velocity = 30

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not isJumping:
                    isJumping = True
                    goingUp = True
                    velocity = 48
        if event.type == pygame.QUIT: 
            running = False
  #(squareX, squareY) = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if charX >= 1:
            charX -= 10
    if keys[pygame.K_RIGHT]:
        if charX <= 595:
            charX += 10

    if isJumping:
        if goingUp:
            charY -= velocity
            velocity -= g
            if velocity == 0:
                goingUp = False
        else:
            charY += velocity
            velocity = velocity + g
            print(velocity)
            if charY >= 550:
                charY = 550
                isJumping = False
        # if(charY==550):
        #   isJumping==False
  #screen.fill("turquoise")
    drawBG(1)
  
    drawFG()

    drawChar(charX, charY, charHeight, charLen)
  

  # RENDER YOUR GAME HERE
  #pygame.draw.rect(screen, "red", (squareX - 50, squareY - 50, 50, 50))
  # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
