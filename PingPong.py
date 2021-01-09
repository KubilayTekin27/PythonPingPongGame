import pygame, sys, time, random ,string

pygame.init()


class oyuncu:
    def __init__(self, x, y, genislik, yukseklik):
        self.x = x
        self.y = y
        self.genislik = genislik
        self.yukseklik = yukseklik

    def oyuncucizdir(self):
        pygame.draw.rect(pencere, (200,200,231), [self.x, self.y, self.genislik, self.yukseklik])


oyuncu1 = oyuncu(0, 0, 10, 300)
oyuncu2 = oyuncu(1390, 300, 10, 300)
skorseysi = oyuncu(699, 0, 1, 800)

# SKOR TABLOSU
oyuncubirskor = 0
oyuncuikiskor = 0



boyut = (1400, 800)

top = pygame.image.load("top.png.png")

top = pygame.transform.scale(top, (80, 80))

pencere = pygame.display.set_mode(boyut)

topx = 200
topy = 300
xyon = 1
yyon = 1
background = pygame.image.load("./black.jpg")
font = pygame.font.Font('freesansbold.ttf', 40)

def showscore(playerscore,x,y):
    score = font.render(str(playerscore),True, (240,240,240))
    pencere.blit( score, (x,y))


clock = pygame.time.Clock()
while True:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pencere.blit(background,(0,0))

    if topx == oyuncu1.x + 10 and oyuncu1.y < topy < oyuncu1.y + 300:
        xyon *= -1

    if topx + 100 == oyuncu2.x and oyuncu2.y < topy < oyuncu2.y + 300:
        xyon *= -1

    oyuncu1.oyuncucizdir()
    oyuncu2.oyuncucizdir()
    skorseysi.oyuncucizdir()
    if topy > 700 or topy < 0:
        yyon *= -1
    topx += 5 * xyon
    topy += 5 * yyon
    # oyuncu hareketi
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        oyuncubirskor = 0
        oyuncuikiskor = 0
        xyon = 1
        yyon = 1
    if keys[pygame.K_w]:
        oyuncu1.y -= 10
    if keys[pygame.K_s]:
        oyuncu1.y += 10
    if keys[pygame.K_UP]:
        oyuncu2.y -= 10
    if keys[pygame.K_DOWN]:
        oyuncu2.y += 10

    # SKOR TABLOSU
    if topx + 100 > 1400:
        time.sleep(1)
        topx = 700
        topy = 400
        oyuncubirskor +=1

    if topx < 0:
        time.sleep(1)
        topx = 700
        topy = 400
        oyuncuikiskor +=1

    if oyuncuikiskor ==5 or oyuncubirskor == 5 :
        pencere.blit(font.render("Game Over Press R to restart", True, (240,240,240)),(420,250))
        xyon = 0
        yyon = 0



    showscore(oyuncubirskor,670,350 )
    showscore(oyuncuikiskor,705,350)

    pencere.blit(top, (topx, topy))
    pygame.display.update()
