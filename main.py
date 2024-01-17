import pygame, random, math

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

# boss sprites

boss = pygame.image.load("demosprite23.png")
boss = pygame.transform.scale(boss, (128, 128))
mad = pygame.image.load("demosprite25.png")
mad = pygame.transform.scale(mad, (128, 128))
bossrect = boss.get_rect()
lhorn = pygame.image.load("demon potato00.png")
rhorn = pygame.image.load("demon potato01.png")
lhorn = pygame.transform.scale(lhorn, (64, 64))
rhorn = pygame.transform.scale(rhorn, (64, 64))
hornrect = lhorn.get_rect()
lcrab = pygame.image.load("demon potato11.png")
rcrab = pygame.image.load("demon potato09.png")
lcrab = pygame.transform.scale(lcrab, (64, 64))
rcrab = pygame.transform.scale(rcrab, (64, 64))
lcrab1 = pygame.image.load("demon potato10.png")
rcrab1 = pygame.image.load("demon potato08.png")
lcrab1 = pygame.transform.scale(lcrab1, (64, 64))
rcrab1 = pygame.transform.scale(rcrab1, (64, 64))
crabrect = lcrab.get_rect()
circle1 = pygame.image.load("demon potato02.png")
circle2 = pygame.image.load("demon potato03.png")
circle1 = pygame.transform.scale(circle1, (160, 160))
circle2 = pygame.transform.scale(circle2, (160, 160))
circlerect = circle1.get_rect()
mouth1 = pygame.image.load("demon potato12.png")
mouth2 = pygame.image.load("demon potato13.png")
mouth1 = pygame.transform.scale(mouth1, (80, 80))
mouth2 = pygame.transform.scale(mouth2, (80, 80))
mouthrect = mouth1.get_rect()


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
creepy = False
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
time = 0
while not crashed:
    time += 0.01
    if creepy:
        if onTick:
            gameDisplay.fill((0, 0, 0))
        else:
            gameDisplay.fill((random.randint(0, int(math.cos(time)*75)+76), 0, 0))
    else:
        gameDisplay.fill(white)
    playerrect.center = (x_pos, y_pos)
    if mode == 0:
        creepy = True
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
            paragraph = 'congrats. that was the first build! more out soon'
            creepy = False
        bosscoords = (500+math.cos(time*2*(bossphase+1))*10, 300+math.sin(time*5*(bossphase+1))*10)
        lhcoords = (bosscoords[0]-48+math.cos(time)*-5, bosscoords[1]-48+math.sin(time)*5)
        rhcoords = (bosscoords[0]+48+math.cos(time)*5, bosscoords[1]-48+math.sin(time)*5)
        circlecoords = (bosscoords[0], bosscoords[1])
        mouthcoords = (bosscoords[0], bosscoords[1]+16)
        examplecoords = (bosscoords[0], bosscoords[1])
        rccoords = (lhcoords[0]-32, lhcoords[1]+128+24*math.cos(time*1.5))
        lccoords = (rhcoords[0]+32, rhcoords[1]+128+24*math.cos(time*1.5))
        bossrect.center = bosscoords
        if bossphase == 0:
            gameDisplay.blit(boss, bossrect)
        if bossphase == 1:
            gameDisplay.blit(mad, bossrect)
            hornrect.center = lhcoords
            gameDisplay.blit(lhorn, hornrect)
            hornrect.center = rhcoords
            gameDisplay.blit(rhorn, hornrect)
        if bossphase == 2:
            gameDisplay.blit(mad, bossrect)
            hornrect.center = lhcoords
            gameDisplay.blit(lhorn, hornrect)
            hornrect.center = rhcoords
            gameDisplay.blit(rhorn, hornrect)
            if onTick:
                crabrect.center = lccoords
                gameDisplay.blit(lcrab, crabrect)
                crabrect.center = rccoords
                gameDisplay.blit(rcrab, crabrect)
            else:
                crabrect.center = lccoords
                gameDisplay.blit(lcrab1, crabrect)
                crabrect.center = rccoords
                gameDisplay.blit(rcrab1, crabrect)
        if bossphase == 3:
            gameDisplay.blit(mad, bossrect)
            hornrect.center = lhcoords
            gameDisplay.blit(lhorn, hornrect)
            hornrect.center = rhcoords
            gameDisplay.blit(rhorn, hornrect)
            circlerect.center = circlecoords
            if onTick:
                gameDisplay.blit(circle1, circlerect)
                crabrect.center = lccoords
                gameDisplay.blit(lcrab, crabrect)
                crabrect.center = rccoords
                gameDisplay.blit(rcrab, crabrect)
            else:
                gameDisplay.blit(circle2, circlerect)
                crabrect.center = lccoords
                gameDisplay.blit(lcrab1, crabrect)
                crabrect.center = rccoords
                gameDisplay.blit(rcrab1, crabrect)
        if bossphase == 4:
            gameDisplay.blit(mad, bossrect)
            hornrect.center = lhcoords
            gameDisplay.blit(lhorn, hornrect)
            hornrect.center = rhcoords
            gameDisplay.blit(rhorn, hornrect)
            circlerect.center = circlecoords
            if onTick:
                gameDisplay.blit(circle1, circlerect)
                crabrect.center = lccoords
                gameDisplay.blit(lcrab, crabrect)
                crabrect.center = rccoords
                gameDisplay.blit(rcrab, crabrect)
            else:
                gameDisplay.blit(circle2, circlerect)
                crabrect.center = lccoords
                gameDisplay.blit(lcrab1, crabrect)
                crabrect.center = rccoords
                gameDisplay.blit(rcrab1, crabrect)
            mouthrect.center = mouthcoords
            if onTick:
                gameDisplay.blit(mouth1, mouthrect)
                crabrect.center = lccoords
                gameDisplay.blit(lcrab, crabrect)
                crabrect.center = rccoords
                gameDisplay.blit(rcrab, crabrect)
            else:
                gameDisplay.blit(mouth2, mouthrect)
                crabrect.center = lccoords
                gameDisplay.blit(lcrab1, crabrect)
                crabrect.center = rccoords
                gameDisplay.blit(rcrab1, crabrect)
        if bossphase == 5:
            gameDisplay.blit(mad, bossrect)
            hornrect.center = lhcoords
            gameDisplay.blit(lhorn, hornrect)
            hornrect.center = rhcoords
            gameDisplay.blit(rhorn, hornrect)
            circlerect.center = circlecoords
            mouthrect.center = mouthcoords
            if random.randint(0, 1):
                gameDisplay.blit(mouth1, mouthrect)
                gameDisplay.blit(circle1, circlerect)
                crabrect.center = lccoords
                gameDisplay.blit(lcrab, crabrect)
                crabrect.center = rccoords
                gameDisplay.blit(rcrab, crabrect)
            else:
                gameDisplay.blit(mouth2, mouthrect)
                gameDisplay.blit(circle2, circlerect)
                crabrect.center = lccoords
                gameDisplay.blit(lcrab1, crabrect)
                crabrect.center = rccoords
                gameDisplay.blit(rcrab1, crabrect)
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
