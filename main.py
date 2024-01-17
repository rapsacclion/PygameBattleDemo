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
glitchness = 0
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()
crashed = False
onTick = False
x_pos = 0
y_pos = 0
xfpos = 500
yfpos = 600
fightbound = ((300, 300), (450, 450))


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
playerrect = playerbody[0].get_rect()
bgimg = pygame.image.load("fight_bg0.png").convert_alpha()
bgimg = pygame.transform.scale(bgimg, (333, 166))
bgrect = bgimg.get_rect()
bgrect.center = (500, 600)
bgmask = pygame.mask.from_surface(bgimg)
title = pygame.image.load("title_1.png")
title = pygame.transform.scale(title, (1000, 1000))
skippitydoodah = pygame.image.load("title_2.png")
skippitydoodah = pygame.transform.scale(skippitydoodah, (1000, 1000))
fight_1 = pygame.image.load("fight00.png")
fightrect = fight_1.get_rect()
fightmask = pygame.mask.from_surface(fight_1)

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
def getcol(rect1, rect2, mask1, mask2):
    #print(rect1.topright, rect2.topright)
    offset = (rect1.topright[0]-rect2.topright[0], rect1.topright[1]-rect2.topright[1]+rect1.height-rect2.height)
    yes = mask1.overlap(mask2, offset)
    return yes

#final setup
pygame.mixer.music.set_volume(0.7)
gameDisplay.fill(white)
go = False
direction = 0
mode = 0
#mode = 0 - title
#mode = 1 - fight
#mode = 2 - play
debug = True
aaaaaa = 4
bossphase = 0
'''
0 = cutscene
1 = simple
2 = fire hands
3 = claws circle fire hands
4 = eyes circle claws hands fire hands hands
5 = everything
'''
bosstalk = {
    0: "number zero",
    1: "test one",
    2: "test the two",
    3: "there is a three",
    4: "two and two",
    5: "i n f i n i  t e   p o w e r"
}
#main loop
while not crashed:
    gameDisplay.fill(white)
    playerrect.center = (x_pos, y_pos)
    if mode == 0:
        if aaaaaa >= 2:
            gameDisplay.blit(skippitydoodah, (0, 0))
            aaaaaa -= 1
        else:
            gameDisplay.blit(title, (0, 0))
    pressed_keys = pygame.key.get_pressed()
    if mode == 1:
        gameDisplay.blit(bgimg, bgrect)
        fightrect.center = (xfpos, yfpos)
        gameDisplay.blit(fight_1, fightrect)
        if not getcol(bgrect, fightrect, bgmask, fightmask):
            if xfpos > bgrect.center[0]:
                xfpos -= 5
            if xfpos < bgrect.center[0]:
                xfpos += 5
            if yfpos > bgrect.center[1]:
                yfpos -= 5
            if yfpos < bgrect.center[1]:
                yfpos += 5
        if bossphase != 6:
            paragraph = bosstalk[bossphase]
            if go:
                bossphase += 1
        else:
            paragraph = 'congrats'
        if bossphase == 0:
            pass
        if pressed_keys[pygame.K_w]:
            yfpos -= 5
        if pressed_keys[pygame.K_a]:
            xfpos -= 5
        if pressed_keys[pygame.K_s]:
            yfpos += 5
        if pressed_keys[pygame.K_d]:
            xfpos += 5
    if mode == 2:
        if pressed_keys[pygame.K_w]:
            direction = 3
            y_pos += 5
            #paragraph = "e!"
        if pressed_keys[pygame.K_a]:
            direction = 2
            x_pos += 5
            #paragraph = "ah!"
        if pressed_keys[pygame.K_s]:
            direction = 0
            y_pos -= 5
            #paragraph = "ooh!"
        if pressed_keys[pygame.K_d]:
            direction = 1
            x_pos -= 5
            #paragraph = "skippity boop dobbity dah dippity dee dop ba doo"
        gameDisplay.blit(bgimg, (x_pos, y_pos))
        character(direction)
    go = False
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
                if mode == 0:
                    mode = 1
                else:
                    go = True
            if event.key == pygame.K_RETURN:
                print(x_pos,y_pos)
    if paragraph != "": #for text
        x = 0
        y = 0
        pygame.draw.rect(gameDisplay, black, (48, 784, 864, 96))
        pygame.draw.rect(gameDisplay, white, (64, 800, 832, 64))
        for letter in paragraph:
            printat(x+64+(random.randint(-glitchness, glitchness)/2), y+800+random.randint(-glitchness, glitchness), letter)
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