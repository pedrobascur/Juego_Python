import pygame
import random
import sys

pygame.init()
pantalla=pygame.display.set_mode((800, 600))
pygame.display.set_caption("mi primer juego")
reloj=pygame.time.Clock()

pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)
x=100
y=200
velocidad=5
mx, my=400, 300
m2x, m2y=200, 150
ox, oy= 600, 100
radio=20
xr=750
puntaje=0
vidas=3
velocidad_extra=10
tiempo_de_velocidad=0
invulnerable=False
estado="inicio"
ejecutando=True
fuente = pygame.font.Font(None, 30)
while ejecutando:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            ejecutando=False
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
    if estado=="fin":
        pantalla.fill((30,30,30))
        msg=fuente.render(
            "game OVER bitch --- puntaje "+str(puntaje), True, (255,255,255))
        if teclas[pygame.K_RETURN]:
            x, y = 100, 200
            vidas = 3
            puntaje = 0
            estado="Jugando"
        pantalla.blit(msg,(150,250))
        ayuda=fuente.render(
            "presiona ENTER para reintentar", True, (200,200,200))
        pantalla.blit(ayuda,(130,320))
        pygame.display.flip()
        reloj.tick(60)
        continue
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
    x =max(0,min (x, 750))
    y =max(0, min(y, 550))
    jugador_rect = pygame.Rect(x, y, 50, 50)
    circulo_rect = pygame.Rect(mx,my, 20,20)
    circulo_rect2 = pygame.Rect(m2x,m2y, 20,20)
    obstaculo_rect = pygame.Rect(ox, oy, 40, 40)
    sonido_monedapuntaje=pygame.mixer.Sound("moneda.wav")
    sonido_monedavelocidad=pygame.mixer.Sound("moneda_brillante.wav")

    if jugador_rect.colliderect(circulo_rect2):
        sonido_monedavelocidad.play()
        tiempo_de_velocidad=600
        m2x=random.randint(50, 750)
        m2y=random.randint(50, 550)
    if jugador_rect.colliderect(circulo_rect):
        puntaje+=1
        sonido_monedapuntaje.play()
        mx=random.randint(50, 750)
        my=random.randint(50, 550)
    if jugador_rect.colliderect(obstaculo_rect):
        vidas-=1
        ox=random.randint(50,750)
        oy=random.randint(50,550)
        if vidas<=0:
            estado="fin"
    pantalla.fill((148, 26, 18))
    pygame.draw.rect(pantalla, (10,7,6), (x, y, 50, 50))
    pygame.draw.circle(pantalla, (255,193,7), (mx,my), 20)
    pygame.draw.circle(pantalla, (15, 217, 25), (m2x,m2y), 20)
    pygame.draw.rect(pantalla,(207, 172, 0), (650,20,130,50))
    pygame.draw.rect(pantalla,(0,0,0),(ox,oy, 50, 50))
    texto=fuente.render(f"puntaje:{puntaje} vidas {vidas}",True,(255,255,255))
    pantalla.blit(texto,(600,32))
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()