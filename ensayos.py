import pygame
import os
import random
import time

ANCHO=1000
ALTO=600
ROJO=[255,0,0]
VERDE=[0,255,0]
BLANCO=[255,255,255]
pantalla=pygame.display.set_mode([ANCHO,ALTO])

def Linea_vida(p, x, y, vida):
    font = pygame.font.Font(None, 30)
    textoVida = font.render(str(vida), True, BLANCO)
    if vida >= 0:
        imagen_fon = pygame.Surface([200, 10])
        imagen_fon.fill(ROJO)
        imag_vida = pygame.Surface([vida*2, 10])
        imag_vida.fill(VERDE)
        p.blit(imagen_fon, (x, y))
        p.blit(imag_vida, (x, y))
        p.blit(textoVida, (x - 50, y - 5))

class jugador(pygame.sprite.Sprite):
    vida=float(100)
    id=0
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.click = False

    def choque(self):
        self.vida-=0.5

    def update(self):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        pantalla.blit(self.image,self.rect)

class Enemigo(pygame.sprite.Sprite):
    Dispara = False
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.vel=5
        self.fuego=0
        self.t=30
        self.choque=False

    def tiempo(self):
        self.t-=1
        if self.t==0:
            self.t=5
            self.fuego=1
        else:
            self.fuego=0

    def update(self):
        self.rect.x-=self.vel
        self.tiempo()
        if self.choque:
            self.choque=False
        if self.rect.x + self.rect.width< 0:
            self.kill()

        ###########
class Disparo(pygame.sprite.Sprite):
    con_aux = 0
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.vel=10
        self.dir=0
        self.sonido=pygame.mixer.Sound("sprites/Laser2.wav")
        self.choque=False

    def update(self):
        if self.con_aux < 1:
            self.sonido.play()
            self.con_aux+=1
        if self.dir==0:
            self.rect.x+=self.vel
        else:
            self.rect.x-=self.vel
        self.choque=False

if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    
    pygame.display.set_caption('Navegator')
    fondo=pygame.image.load('sprites/espacio.jpg')
    inf=fondo.get_rect()


    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()

    enemigos=pygame.sprite.Group()
    enemigos2=pygame.sprite.Group()

    sonido2=pygame.mixer.Sound("sprites/Laser3.wav")
    font= pygame.font.Font(None, 70)
    textWin=font.render("YOU WIN", True, [255,255,255])
    textLose=font.render("You Lose !!!", True, [255,255,255])



    #iconos=pygame.sprite.Group()

    iconos=pygame.sprite.Group()
    icono=jugador('sprites/naveJugador.png')
    icono.id=1
    icono.rect.y=ALTO-100
    icono.rect.x=30
    todos.add(icono)
    iconos.add(icono)

    mov_x=0
    mov_y=0
    pos_x=200
    pos_y=200

    marco=fondo.subsurface(pos_x, pos_y, ANCHO, ALTO)
    marcoinf=marco.get_rect()
    pantalla.blit(marco, [0,0])

    con=0
    auxEn = 0
    reloj = pygame.time.Clock()

    #enemigo
    for i in range(10):
        ini = random.randrange(1,200)
        x=ANCHO + ini
        y=random.randrange(ALTO-30)
        e=Enemigo('sprites/enem1.png')
        e.rect.x=x
        e.rect.y=y
        e.vel=random.randrange(1,5)
        enemigos2.add(e)
        todos.add(e)

    reloj=pygame.time.Clock()
    fin=False

#enemigo UNO
    for n in range(2):
        ini = random.randrange(1,200)
        x=ANCHO + ini
        y=random.randrange(ALTO-10)
        e1=Enemigo('sprites/enem2.png')
        e1.rect.x=x
        e1.rect.y=y
        e1.vel=random.randrange(1,3)
        e.Dispara=True
        enemigos.add(e1)
        todos.add(e1)

    balas=pygame.sprite.Group()
    e1balas=pygame.sprite.Group()
    reloj=pygame.time.Clock()
    fin=False

#enemigo DOS
    for m in range(5):
        ini = random.randrange(1,200)
        x=ANCHO + ini
        y=random.randrange(ALTO-50)
        e2=Enemigo('sprites/enem3.png')
        e2.rect.x=x
        e2.rect.y=y
        e2.vel=random.randrange(1,3)
        enemigos2.add(e2)
        todos.add(e2)

    balas=pygame.sprite.Group()
    reloj=pygame.time.Clock()
    fin=False

#enemigo TRES
    for a in range(2):
        ini = random.randrange(1,200)
        x=ANCHO + ini
        y=random.randrange(ALTO-75)
        e3=Enemigo('sprites/enem4.png')
        e3.rect.x=x
        e3.rect.y=y
        e3.vel=random.randrange(1,3)
        e3.Dispara = True
        enemigos.add(e3)
        todos.add(e3)

    balas=pygame.sprite.Group()
    e3balas=pygame.sprite.Group()
    reloj=pygame.time.Clock()
    fin=False

#enemigo CUATRO
    for c in range(5):
        ini = random.randrange(1,200)
        x=ANCHO + ini
        y=random.randrange(ALTO-90)
        e4=Enemigo('sprites/enem5.png')
        e4.rect.x=x
        e4.rect.y=y
        e4.vel=random.randrange(1,3)
        enemigos2.add(e4)
        todos.add(e4)

    balas=pygame.sprite.Group()
    reloj=pygame.time.Clock()
    fin=False

################para el contador en tiempo pantalla
    Fuente=pygame.font.SysFont("Arial",30)
    gana=False
    pierde=False
    aux=1
    startTime=time.time()
    retraso=True
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ic in iconos:
                    if ic.rect.collidepoint(event.pos):
                        print "icono " + str(ic.id)
                        b=jugador('sprites/naveJugador.png')
                        con+=1
                        b.id=con
                        b.rect.y=ALTO-80
                        col=True
                        while col:
                            col=False
                            colision=pygame.sprite.spritecollide(b,jugadores,False)
                            for bl in colision:
                                if bl.id != b.id:
                                    b.rect.left=bl.rect.right
                                    col=True
                        todos.add(b)
                        jugadores.add(b)

                for bl in jugadores:
                    if bl.rect.collidepoint(event.pos):
                        bl.click=True

            if event.type == pygame.MOUSEBUTTONUP:
                for bl in jugadores:
                    if bl.click == True:
                        bl.click = False
                        col=True
                        while col:
                            col=False
                            colision=pygame.sprite.spritecollide(bl,jugadores,False)
                            for e in colision:
                                if bl.id != e.id:
                                    bl.rect.left=e.rect.right
                                    if bl.rect.x > ANCHO:
                                        bl.rect.x=ANCHO/2
                                    col=True

        if auxEn % 15 == 0:   
            for i in jugadores:
                if not i.click and not retraso and not pierde:
                    b=Disparo('sprites/bala4.png')
                    sonido2.play()
                    sonido2.play()
                    b.rect.x=i.rect.x
                    b.rect.y=i.rect.y + i.rect.height/2
                    balas.add(b)
                    todos.add(b)
        #quitar enemigos cuando dispara el jugador
        for b in balas:
            ls_imp=pygame.sprite.spritecollide(b,enemigos,True)
            ls_imp2=pygame.sprite.spritecollide(b,enemigos2,True)
            for b_imp in ls_imp:
                b.kill()
            for b_imp in ls_imp2:
                b.kill()

            if b.rect.x>ANCHO:
                b.kill()


        if auxEn % 20 == 0: #Retraso entre los disparos de enemigos
            #balas para enemigo UNO
            for e1 in enemigos:
                if e1.fuego==1:
                    b=Disparo('sprites/bala2.png')
                    b.rect.x=e1.rect.x
                    b.rect.y=e1.rect.y
                    b.dir=1
                    e1balas.add(b)
                    todos.add(b)
                if e1.rect.x<0:
                    e1.kill()

            #balas para enemigo TRES
            for e3 in enemigos:
                if e3.fuego==1:
                    b=Disparo('sprites/bala2.png')
                    b.rect.x=e3.rect.x
                    b.rect.y=e3.rect.y
                    b.dir=1
                    e3balas.add(b)
                    todos.add(b)
                if e3.rect.x<0:
                    e3.kill()
        auxEn+=1

        #COLISIONES ENEMIGOS
        for i in jugadores:
            if not i.click:
                l_col=pygame.sprite.spritecollide(i,enemigos,False)
                l_col2=pygame.sprite.spritecollide(i,enemigos2,False)
                for en in l_col:
                    en.choque=True #genera el sonido en false
                    icono.choque()
                for en in l_col2:
                    en.choque=True #genera el sonido en false
                    icono.choque()
            
        #ENEMIGOS SALEN DE LA PANTALLA
        for en in enemigos:
            if en.rect.x + en.rect.width <= 0:
                icono.vida-=10
        for en in enemigos2:
            if en.rect.x + en.rect.width <= 0:
                icono.vida-=10

        '''
        if icono.vida<=0: #el jugador se golpea y le quita vida
            fin=True
        '''

        if enemigos == 0 and enemigos2 == 0:
            pantalla.blit(textWin, (300 - textWin.get_width()))

        endTime = time.time()
        if endTime - startTime > 5:
            retraso = False
        if not retraso:
            todos.update()
            marco=fondo.subsurface(pos_x, pos_y, ANCHO, ALTO)
            pantalla.blit(marco, [0,0])
            Linea_vida(pantalla, 100, 30, icono.vida)
            todos.draw(pantalla)
            reloj.tick(60)
            pygame.display.update()
            if(len(enemigos)<=0 and len(enemigos2)<=0 and icono.vida>=0):
                gana=True
            elif(icono.vida<=0 and not pierde):
                pierde=True
                todos.remove(jugadores)
            if(gana):
                pantalla.blit(textWin, [300, 250])
            elif(pierde):
                pantalla.blit(textLose, [300, 250])
            pygame.display.flip()

        else:
            jugadores.update()
            iconos.update()
            marco=fondo.subsurface(pos_x, pos_y, ANCHO, ALTO)
            pantalla.blit(marco, [0,0])
            Linea_vida(pantalla, 100, 30, icono.vida)
            todos.draw(pantalla)
            reloj.tick(60)
            pygame.display.update()
            pygame.display.flip()