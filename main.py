import pygame
import random
import sys

pygame.init()
pantalla=pygame.display.set_mode((800, 600))
pygame.display.set_caption("mi primer juego")
reloj=pygame.time.Clock()
x=100
y=200
velocidad=5
mx, my=400, 300
m2x, m2y=200, 150
radio=20
xr=750
puntaje=0
ejecutando=True
fuente = pygame.font.Font(None, 30)
while ejecutando:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            ejecutando=False
    teclas=pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        x +=velocidad
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_DOWN]:
        y+=velocidad
    if teclas[pygame.K_UP]:
        y-=velocidad
    x =max(0,min (x, 750))
    y =max(0, min(y, 550))
    jugador_rect = pygame.Rect(x, y, 50, 50)
    circulo_rect = pygame.Rect(mx,my, 20,20)
    circulo_rect2 = pygame.Rect(m2x,m2y, 20,20)
    if jugador_rect.colliderect(circulo_rect2):
        velocidad+=2
        m2x=random.randint(50, 750)
        m2y=random.randint(50, 550)
    if jugador_rect.colliderect(circulo_rect):
        puntaje+=1
        mx=random.randint(50, 750)
        my=random.randint(50, 550)
    pantalla.fill((148, 26, 18))
    pygame.draw.rect(pantalla, (10,7,6), (x, y, 50, 50))
    pygame.draw.circle(pantalla, (255,193,7), (mx,my), 20)
    pygame.draw.circle(pantalla, (15, 217, 25), (m2x,m2y), 20)
    pygame.draw.rect(pantalla,(207, 172, 0), (650,20,130,50))
    texto=fuente.render(f"puntaje:{puntaje}",True,(255,255,255))
    pantalla.blit(texto,(660,32))
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()