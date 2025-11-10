import pygame
import time

WIDTH, HEIGHT = 1000, 1000
PIXEL_SIZE = 20

pygame.init()
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Método Bresenham")

def calcular_reta(x1, y1, x2, y2):    
    swap_y = False
    if y2 < y1:
        y1, y2 = -y1, -y2
        swap_y = True
    
    swap_xy = False
    if abs(y2 - y1) > abs(x2 - x1):
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        swap_xy = True
    
    if x2 < x1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    
    dy = y2 - y1
    dx = x2 - x1
    y = y1
    p = 2 * dy - dx
        
    for x in range(x1, x2+1):
        if swap_xy:
            draw_x = y
            draw_y = x
        else:
            draw_x = x
            draw_y = y
            
        if swap_y:
            draw_y = -draw_y
            
        draw_pixel(draw_x, draw_y)
        pygame.time.wait(20)
        if p >= 0:
            y += 1
            p = p + 2*(dy-dx)
        else:
            p = p + 2*dy
            
def draw_pixel(x, y, cor=(0, 0, 0)):
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
        
"""def draw_pixel(x, y, cor=(0,0,0)):
    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    
    pixel_x = center_x + (x * PIXEL_SIZE)
    pixel_y = center_y - (y * PIXEL_SIZE)
    
    pygame.draw.rect(tela, cor, (pixel_x, pixel_y, PIXEL_SIZE, PIXEL_SIZE))
    pygame.display.update()

def draw_grid():
    font = pygame.font.SysFont('Arial', 12)
    
    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    grid_cells_x = WIDTH // PIXEL_SIZE
    grid_cells_y = HEIGHT // PIXEL_SIZE
    
    for x in range(0, WIDTH, PIXEL_SIZE):
        pygame.draw.line(tela, (200, 200, 200), (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, PIXEL_SIZE):
        pygame.draw.line(tela, (200, 200, 200), (0, y), (WIDTH, y), 1)
    
    pygame.draw.line(tela, (0, 0, 0), (center_x, 0), (center_x, HEIGHT), 2)
    pygame.draw.line(tela, (0, 0, 0), (0, center_y), (WIDTH, center_y), 2)
    
    cells_from_center = grid_cells_x // 2
    
    for i in range(-cells_from_center, cells_from_center + 1):
        if i != 0:
            text = font.render(str(i), True, (100, 100, 100))
            x_pos = center_x + (i * PIXEL_SIZE)
            tela.blit(text, (x_pos + 5, center_y + 5))
        if i != 0:
            text = font.render(str(i), True, (100, 100, 100))
            y_pos = center_y - (i * PIXEL_SIZE)
            tela.blit(text, (center_x + 5, y_pos + 5))
    
    text = font.render("0", True, (255, 0, 0))
    tela.blit(text, (center_x + 5, center_y + 5))
    
    pygame.display.update()"""

if __name__ == '__main__':
    rodando = True
    tela.fill((255,255,255))
    draw_grid()
  
    start = time.time()
    for i in range(10): 
        calcular_reta(1, 1, 49, 49)
    
    tempo_medio = (time.time() - start)/10
    print(tempo_medio)
    
    
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                
    pygame.quit()
