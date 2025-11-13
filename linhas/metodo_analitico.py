import os
import psutil
import pygame
import time

WIDTH, HEIGHT = 1000, 1000
PIXEL_SIZE = 20

pygame.init()
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Método Analítico")

def calcular_reta(x1, y1, x2, y2):
    if x1 == x2:
        for y in range(y1, y2+1):
            draw_pixel(x1, y)
            pygame.time.wait(20)
    else:
        m = (y2 - y1)/(x2 - x1)
        b = y2 - m*x2
        
        for x in range(x1, x2+1):
            y = m*x + b
            draw_pixel(x, round(y))
            pygame.time.wait(20)
        
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
    
    process = psutil.Process(os.getpid())
    memoria_antes = process.memory_info().rss / 1024 / 1024
    
    start = time.time()
    for i in range(1):
        calcular_reta(1, 1, 49, 49)
    
    tempo_medio = (time.time() - start)/10
    print(tempo_medio)
    
    memoria_depois = process.memory_info().rss / 1024 / 1024
    memoria_algoritmo = memoria_depois - memoria_antes
    print(memoria_algoritmo)
    
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                
    pygame.quit()
