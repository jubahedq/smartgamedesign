import pygame, math, random
#Go here for inf: https://www.pygame.org/docs/ref/draw.html
#PYTHON 3.11.5!!!

pygame.init()

w = 1280
h = 720
size = (w, h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
walkTransition = pygame.time.Clock()
g = 3
OffsetX=0
xCoord = 60
# rightBound = leftBound + 120
Ledge=True
Redge=False
pabloF = pygame.image.load("pablofront1.png").convert_alpha()
pabloW0 = pygame.image.load("walk0.png").convert_alpha()
pabloW1 = pygame.image.load("walk1.png").convert_alpha()
pabloW2 = pygame.image.load("walk2.png").convert_alpha()
pabloW3 = pabloW1
# pabloR = pygame.image.load("pabloright1.png").convert_alpha()
# for each platform...
# (xCoord, y coordinate (in pixels), width (xCoords), height (in pixels))
platforms = [(90,200,20,30)]
walkFrame = 0

def drawBG(act):
    global Ledge, Redge
    if act == 1:
        bg = pygame.image.load("testbg.png").convert()
        bg = pygame.transform.scale(bg, (3200, 720))
        if OffsetX == 0:
            # print(1)
            Ledge = True
            Redge = False
        elif OffsetX <= -1920:
            # print(2)
            Ledge = False
            Redge = True
        else:
            # print(3)
            Ledge = False
            Redge = False
        screen.blit(bg, (OffsetX,0))
    elif act == 2:
       pass
       
def drawFG():
    #pass
    pygame.draw.rect(screen, "red", (0,670,1280,720))

def drawChar(charX, charY, charHeight, charLen, isMoving, direction, playerClock):
    global walkFrame
    #direction True = moving right
    #direction False = moving left
    #isMoving, self explanatory
    if (not isMoving):
        char = pygame.transform.scale(pabloF, (charLen, charHeight))
        screen.blit(char, (charX,charY))
        walkFrame = 0
    else:
        match walkFrame:
            case 0:
                char = pygame.transform.scale(pabloW0, (charLen, charHeight))
            case 1:
                char = pygame.transform.scale(pabloW1, (charLen, charHeight))
            case 2:
                char = pygame.transform.scale(pabloW2, (charLen, charHeight))
            case 3:
                char = pygame.transform.scale(pabloW3, (charLen, charHeight))

        if playerClock == 5:
            if walkFrame == 3:
                walkFrame = 0
            else:
                walkFrame += 1
        
        # char = pygame.transform.scale(pabloR, (charLen, charHeight))
        if (not direction): #moving left
            char = pygame.transform.flip(char, True, False)
        screen.blit(char, (charX,charY))
        # walkTransition.tick(10)
    #     pygame.draw.rect(screen, "blue", (charX, charY, charLen, charHeight))
    # pygame.draw.rect(screen, "blue", (charX, charY, charLen, charHeight))
#squareX = 100
#squareY = 100
        
def drawPlatforms():
    global platforms
    return


        






running = True
charX = 595 #top left
charY = 550 #top left is coordinates
charHeight = 120
charLen = 60
isJumping = False
goingUp = True
velocity = 30
playerClock = 0
while running:
    isMoving = False
    direction = False
    # print(Ledge, Redge, OffsetX)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not isJumping:
                    isJumping = True
                    goingUp = True
                    velocity = 30
        if event.type == pygame.QUIT: 
            running = False
  #(squareX, squareY) = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        # if (Ledge and charX >= 1):
        #     charX -= 10
        isMoving = True
        
        if ((not Ledge) and charX == 595):
            xCoord -= 1
            OffsetX += 10
        elif (charX >= 1):
            xCoord -= 1
            charX -= 10
    if keys[pygame.K_RIGHT]:
        
        isMoving = True
        direction = True
        # if (Redge and charX <= 1190):
        #     charX += 10
        if ((not Redge) and charX == 595):
            OffsetX -= 10
            xCoord += 1
        elif (charX <= 1220):
            charX += 10
            xCoord += 1

    if isJumping:
        if goingUp:
            charY -= velocity
            velocity -= g
            if velocity == 0:
                goingUp = False
        else:
            charY += velocity
            velocity = velocity + g
            # print(velocity)
            if charY >= 550:
                charY = 550
                isJumping = False
        # if(charY==550):
        #   isJumping==False
  #screen.fill("turquoise")
    drawBG(1)
  
    drawFG()

    leftBound = -OffsetX//10
    rightBound = leftBound + 120

    drawPlatforms()

    drawChar(charX, charY, charHeight, charLen, isMoving, direction, playerClock)

    print("\nplayer pos: ",xCoord,"\n","left bound: ", leftBound,"\nright bound: ", rightBound)
  

  # RENDER YOUR GAME HERE
  #pygame.draw.rect(screen, "red", (squareX - 50, squareY - 50, 50, 50))
  # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)
    playerClock += 1
    if playerClock > 5:
        playerClock = 0

pygame.quit()

