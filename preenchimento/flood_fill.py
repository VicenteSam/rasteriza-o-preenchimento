import time
import pygame

WIDTH, HEIGHT = 1000, 1000
PIXEL_SIZE = 20

pygame.init()
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flood Fill")

def circunferencia_bresenham(xc, yc, r, cor=(0, 0, 0)):
    x = 0
    y = r
    p = 1 - r
    
    while x <= y:
        draw_pixel(x + xc, y + yc, cor)
        draw_pixel(y + xc, x + yc, cor)
        draw_pixel(-x + xc, y + yc, cor)
        draw_pixel(-y + xc, x + yc, cor)
        draw_pixel(-x + xc, -y + yc, cor)
        draw_pixel(-y + xc, -x + yc, cor)
        draw_pixel(x + xc, -y + yc, cor)
        draw_pixel(y + xc, -x + yc, cor)
        
        pygame.event.pump() 
        pygame.time.wait(50)
        
        if p >= 0:
            y -= 1
            p = p + 2*x - 2*y + 5
            x += 1
        else:
            p = p + 2*x + 3
            x += 1
            
def linha_bresenham(x1, y1, x2, y2, cor=(0, 0, 0)):
    dx = x2 - x1
    dy = y2 - y1
    
    if x2 < x1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    
    swap_y = False
    if y2 < y1:
        y1 = -y1
        y2 = -y2
        swap_y = True

    swap_xy = False
    if abs(dy) > abs(dx):
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx
        swap_xy = True
        
    dx = x2 - x1
    dy = y2 - y1
    y = y1
    p = 2*dy-dx
        
    for x in range(x1, x2+1):
        if swap_xy:
            draw_x = y
            draw_y = x
        else:
            draw_x = x
            draw_y = y
            
        if swap_y:
            draw_y = -draw_y
            
        draw_pixel(draw_x, draw_y, cor)
        pygame.event.pump()
        pygame.time.wait(50)
        if p >= 0:
            y += 1
            p = p + 2*(dy-dx)
        else:
            p = p + 2*dy
            
def flood_fill(x, y, cor, novaCor):
    if get_color(x, y) == cor:
        draw_pixel(x, y, novaCor)
        pygame.time.wait(10)
        
        flood_fill(x + 1, y, cor, novaCor)
        flood_fill(x, y + 1, cor, novaCor)
        flood_fill(x - 1, y, cor, novaCor)
        flood_fill(x, y - 1, cor, novaCor)
    
def get_color(x,y):
    pixel_x = x * PIXEL_SIZE
    pixel_y = (HEIGHT // PIXEL_SIZE - 1 - y) * PIXEL_SIZE
    
    return tela.get_at((pixel_x, pixel_y))[:3]
        
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

def mostrar_menu():
    print("\n" + "="*50)
    print("          SISTEMA FLOOD FILL")
    print("="*50)
    print("1. Pintar Retângulo")
    print("2. Pintar Circunferência")
    print("3. Pintar Polígono A")
    print("4. Pintar Polígono D")
    print("5. Sair")
    print("="*50)
    
    try:
        opcao = int(input("Escolha uma opção (1-5): "))
        return opcao
    except ValueError:
        print("Opção inválida! Digite um número.")
        return 0

def limpar_tela():
    tela.fill((255, 255, 255))
    draw_grid()
    
if __name__ == '__main__':
    rodando = True
    
    pontos_retangulo = [(3, 10), (40, 10), (40, 25), (3, 25)]
    pontos_poligono_A = [(15,15),(40,20),(42,27),(22,42),(10,30),(18,25)]
    pontos_poligono_D = [(15,15),(7,23),(15,31),(23,23),(27,27),(31,23),(39,31),(47,23),(39,15),(31,23),(27,19),(23,23)]
    
    while rodando:
        limpar_tela()
        opcao = mostrar_menu()
        
        if opcao == 1:
            for i in range(len(pontos_retangulo)):
                xa, ya = pontos_retangulo[i]
                xb, yb = pontos_retangulo[(i + 1) % len(pontos_retangulo)]
                linha_bresenham(xa, ya, xb, yb, (0, 0, 255))
            
            pygame.time.wait(100)
            
            start_time = time.time()
            flood_fill(20, 17, (200, 200, 200), (255, 0, 0))
            tempo = time.time() - start_time
            print(tempo)
            
        elif opcao == 2:
            try:
                raio = int(input("Digite o raio da circunferência (5-25): "))
                if raio < 5 or raio > 25:
                    print("Raio deve ser entre 5 e 25!")
                    continue
                    
                centro_x, centro_y = 25, 25
                circunferencia_bresenham(centro_x, centro_y, raio, (0, 0, 255))
                pygame.time.wait(100)
                
                start_time = time.time()
                flood_fill(centro_x, centro_y, (200, 200, 200), (0, 255, 0))
                tempo = time.time() - start_time
                print(tempo)
                
            except ValueError:
                print("Raio inválido!")
                
        elif opcao == 3:
            for i in range(len(pontos_poligono_A)):
                x1, y1 = pontos_poligono_A[i]
                x2, y2 = pontos_poligono_A[(i + 1) % len(pontos_poligono_A)]
                linha_bresenham(x1, y1, x2, y2, (0, 0, 255))
            
            pygame.time.wait(100)
            
            start_time = time.time()
            flood_fill(25, 25, (200, 200, 200), (255, 255, 0))
            tempo = time.time() - start_time
            print(tempo)
            
        elif opcao == 4:
            for i in range(len(pontos_poligono_D)):
                x1, y1 = pontos_poligono_D[i]
                x2, y2 = pontos_poligono_D[(i + 1) % len(pontos_poligono_D)]
                linha_bresenham(x1, y1, x2, y2, (0, 0, 255))
            
            pygame.time.wait(100)
            
            start_time = time.time()
            flood_fill(27, 23, (200, 200, 200), (255, 0, 255))
            tempo = time.time() - start_time
            print(tempo)
            
        elif opcao == 5:
            print("Saindo...")
            rodando = False
            
        else:
            print("Opção inválida! Tente novamente.")
        
        if opcao != 5:
            input("Pressione Enter para continuar...")
    
    pygame.quit()
