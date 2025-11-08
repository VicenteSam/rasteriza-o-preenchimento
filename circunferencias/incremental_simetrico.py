import pygame
import math
import time

WIDTH, HEIGHT = 1000, 1000
PIXEL_SIZE = 20

pygame.init()
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Método Incremental Simétrico")

def calcular_circunferencia(xc, yc, r):
    x = r
    y = 0
    theta = 1/r
    c = math.cos(theta)
    s = math.sin(theta)
    
    iteracoes = 0
    pixels_pintados = 0
    
    while y <= x:
        iteracoes += 1
        pixels_pintados += 8
        
        draw_pixel(x + xc, y + yc)
        draw_pixel(y + xc, x + yc)
        draw_pixel(-y + xc, x + yc)
        draw_pixel(-x + xc, y + yc)
        draw_pixel(-x + xc, -y + yc)
        draw_pixel(-y + xc, -x + yc)
        draw_pixel(y + xc, -x + yc)
        draw_pixel(x + xc, -y + yc)
        pygame.time.wait(10)
        
        xt = x
        x = x * c - y * s
        y = y * c + xt * s

    return iteracoes, pixels_pintados
        
        
        
def draw_pixel(x, y, cor=(0,0,0)):
    cartesian_y = (HEIGHT // PIXEL_SIZE) - 1 - y
    pygame.draw.rect(tela, cor, (x * PIXEL_SIZE, cartesian_y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    pygame.display.update()

def draw_grid():
    font = pygame.font.SysFont('Arial', 12)
    grid_cells = HEIGHT // PIXEL_SIZE
    
    for x in range(0, WIDTH, PIXEL_SIZE):
        pygame.draw.line(tela, (200, 200, 200), (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, PIXEL_SIZE):
        pygame.draw.line(tela, (200, 200, 200), (0, y), (WIDTH, y), 1)
    
    for x in range(0, grid_cells):
        text = font.render(str(x), True, (100, 100, 100))
        tela.blit(text, (x * PIXEL_SIZE + 5, HEIGHT - 15))
    
    for y in range(0, grid_cells):
        cartesian_y = grid_cells - 1 - y
        text = font.render(str(cartesian_y), True, (100, 100, 100))
        tela.blit(text, (5, y * PIXEL_SIZE + 5))
    
    pygame.draw.line(tela, (150, 150, 150), (0, HEIGHT - PIXEL_SIZE), (WIDTH, HEIGHT - PIXEL_SIZE), 2)
    pygame.draw.line(tela, (150, 150, 150), (PIXEL_SIZE, 0), (PIXEL_SIZE, HEIGHT), 2)
    
    pygame.display.update()
        
if __name__ == '__main__':
    rodando = True
    tela.fill((255,255,255))
    draw_grid()
    
    total_iteracoes = 0
    total_pixels = 0
    
    start = time.time()
    for i in range(10):
        iteracoes, pixels = calcular_circunferencia(25,25,24)
        total_iteracoes += iteracoes
        total_pixels += pixels
        
    tempo_medio = (time.time() - start)/10
    print(tempo_medio, total_iteracoes, total_pixels)
    
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                
    pygame.quit()