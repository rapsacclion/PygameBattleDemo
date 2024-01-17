import pygame, random

pygame.mixer.init()
pygame.init()

# variables and setup
display_width = 1000
display_height = 1000
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('demo')
TICK = pygame.USEREVENT + 1
pygame.time.set_timer(TICK, 250)
paragraph = ""
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()
crashed = False
onTick = False
x_pos = 0
y_pos = 0

# image imports
alphabet = []
playerbody = []
basic = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","?",".",","]
for t in range(0, 30):
    iternum = ""
    if len(str(t)) == 1:
        iternum = "0"+str(t)
    else:
        iternum = str(t)
    alphabet.append(pygame.image.load("alphabet"+iternum+".png"))
for t in range(0, 5):
    playerbody.append(pygame.image.load("character_"+str(t)+".png"))
bgimg = pygame.image.load("fight_bg0.png")
title = pygame.image.load("title_1.png")
skippitydoodah = pygame.image.load("title_2.png")
title = pygame.transform.scale(title, (1000, 1000))
skippitydoodah = pygame.transform.scale(skippitydoodah, (1000, 1000))
spek = pygame.mixer.Sound("charspeak1.wav")

#function declaration
def printat(x, y, letter):
    letterprintindex = 0
    try:
        letterprintindex += basic.index(letter.lower())
        gameDisplay.blit(alphabet[letterprintindex], (x, y))
    except:
        pass
def character(direction):
    gameDisplay.blit(playerbody[direction], (display_width/2-32, display_height/2-32))
    
#final setup
pygame.mixer.music.set_volume(0.7)
gameDisplay.fill(white)
direction = 0
mode = 0
#mode = 0 - title
#mode = 1 - fight

#main loop
while not crashed:
    gameDisplay.fill(white)
    if mode == 0:
        rando = random.randint(random.randint(0, 25), 50)
        if rando >= 50:
            gameDisplay.blit(skippitydoodah, (0, 0))
        else:
            gameDisplay.blit(title, (0, 0))
    pressed_keys = pygame.key.get_pressed()
    if mode == 1:
        if pressed_keys[pygame.K_w]:
            direction = 3
            y_pos += 5
            paragraph = "e!"
        if pressed_keys[pygame.K_a]:
            direction = 2
            x_pos += 5
            paragraph = "ah!"
        if pressed_keys[pygame.K_s]:
            direction = 0
            y_pos -= 5
            paragraph = "ooh!"
        if pressed_keys[pygame.K_d]:
            direction = 1
            x_pos -= 5
            paragraph = "skippity boop dobbity dah dippity dee dop ba doo"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == TICK:
            onTick = not onTick
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                pass
            if event.key == pygame.K_z:
                pass
            if event.key == pygame.K_SPACE:
                mode = 1
            if event.key == pygame.K_RETURN:
                pass
    if mode == 1:
        gameDisplay.blit(bgimg, (x_pos, y_pos))
        character(direction)
    if paragraph != "": #for text
        x = 0
        y = 0
        glitchness = 0
        pygame.draw.rect(gameDisplay, black, (48, 784, 864, 96))
        pygame.draw.rect(gameDisplay, white, (64, 800, 832, 64))
        for letter in paragraph:
            printat(x+64, y+800+random.randint(-glitchness, glitchness), letter)
            x += 32
            if x >= 832:
                x = 0
                y += 32
            if y >= 64:
                break
            
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()