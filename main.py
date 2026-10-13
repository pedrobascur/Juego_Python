import pygame
import random


pygame.init()
pantalla=pygame.display.set_mode((800, 600))
pygame.display.set_caption("mi primer juego")
reloj=pygame.time.Clock()

pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)

#aparicion y velocidad jugador#
x=100
y=200
velocidad=5

#aparicion de monedas y puntaje
mx, my=400, 300
m2x, m2y=200, 150
radio=20
xr=750
puntaje=0

#vida y espada jugador
vida=100
espada_activa=False
tiempo_espada=0
daño_espada=25
espada_atacando=False
golpe_realizado=False
#buffs
velocidad_extra=10
tiempo_de_velocidad=0

#bandido
vida_bandido=125
daño_bandido=25
bandido_x=600
bandido_y=300
bandido_rect=pygame.Rect(bandido_x,bandido_y,50,50)
bala_x=0
bala_y=0
bala_activa=False
velocidad_bala=8
super_ataqueB=pygame.time.get_ticks()
tiempo_bandido=random.randint(20000,30000)

#primer bucle
estado="inicio"
ejecutando=True
fuente = pygame.font.Font(None, 30)
while ejecutando:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            ejecutando=False
            if evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_SPACE:
                    espada_atacando=True
                    golpe_realizado=False
            if evento.type==pygame.KEYUP:
                if evento.key==pygame.K_SPACE:
                    espada_atacando=False

#inicio
    teclas=pygame.key.get_pressed()
    if estado=="inicio":
        pantalla.fill((30,30,30))
        titulo=fuente.render(
            "presione enter para jugar", True,(255,255,255))
        pantalla.blit(titulo,(150,280))
        if teclas[pygame.K_RETURN]:
            estado="jugando"
        pygame.display.flip()
        reloj.tick(60)
        continue

#game over    
    if estado=="fin":
        pantalla.fill((30,30,30))
        msg=fuente.render(
            "game OVER bitch --- puntaje "+str(puntaje), True, (255,255,255))
        if teclas[pygame.K_RETURN]:
            x, y = 100, 200
            vida = 100
            puntaje = 0
            estado="Jugando"
        pantalla.blit(msg,(150,250))
        ayuda=fuente.render(
            "presiona ENTER para reintentar", True, (200,200,200))
        pantalla.blit(ayuda,(130,320))
        pygame.display.flip()
        reloj.tick(60)
        continue
#teclas
    velocidad_actual=velocidad
    if tiempo_de_velocidad>0:
        velocidad_actual+=velocidad_extra
        tiempo_de_velocidad-=1
    if teclas[pygame.K_RIGHT]:
        x +=velocidad_actual
    if teclas[pygame.K_LEFT]:
        x -= velocidad_actual
    if teclas[pygame.K_DOWN]:
        y+=velocidad_actual
    if teclas[pygame.K_UP]:
        y-=velocidad_actual
    if teclas[pygame.K_SPACE]:
        espada_activa=True
        tiempo_espada=10
    x =max(0,min (x, 750))
    y =max(0, min(y, 550))
    jugador_rect = pygame.Rect(x, y, 50, 50)
    if espada_atacando:
        espada_rect=pygame.Rect(x+50, y+15, 40,20)
        if espada_rect.colliderect(bandido_rect1) and not golpe_realizado:
            vida_bandido-=daño_espada
            golpe_realizado=True
    if espada_activa:
        tiempo_espada-=1
        if tiempo_espada==0:
            espada_activa=False
    circulo_rect = pygame.Rect(mx,my, 20,20)
    circulo_rect2 = pygame.Rect(m2x,m2y, 20,20)
    sonido_monedapuntaje=pygame.mixer.Sound("moneda.wav")
    sonido_monedavelocidad=pygame.mixer.Sound("moneda_brillante.wav")

    if jugador_rect.colliderect(circulo_rect2):
        sonido_monedavelocidad.play()
        tiempo_de_velocidad=600
        m2x=random.randint(50, 750)
        m2y=random.randint(50, 550)
    if jugador_rect.colliderect(circulo_rect):
        vida+=20
        if vida>200:
            vida=200
        sonido_monedapuntaje.play()
        mx=random.randint(50, 750)
        my=random.randint(50, 550)
    pantalla.fill((148, 26, 18))
    pygame.draw.rect(pantalla, (10,7,6), (x, y, 50, 50))
    if espada_activa:
        pygame.draw.rect(pantalla, (220, 220, 220), espada_rect)
    pygame.draw.circle(pantalla, (255,193,7), (mx,my), 20)
    pygame.draw.circle(pantalla, (15, 217, 25), (m2x,m2y), 20)
    pygame.draw.rect(pantalla,(207, 172, 0), (650,20,130,50))
    bandido_rect1=pygame.Rect(600,200,60,60)
    pygame.draw.rect(pantalla,(235, 225, 52),(bandido_rect1))
    texto_vidaB=fuente.render(
        f"bandido:{max(0,vida_bandido)}HP",
        True,
        (255,255,255)
    )
    pantalla.blit(texto_vidaB,(550,160))
    texto=fuente.render(f"puntaje:{puntaje} vida {vida}",True,(255,255,255))
    pantalla.blit(texto,(600,32))
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()