import time
import pygame
import math

WIDTH, HEIGHT = 500, 500
PIXEL_SIZE = 2

pygame.init()
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Preenchimento por Varredura")

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

def algoritmo_varredura(pontos, cor_preenchimento=(255, 0, 0)):
    tabela_arestas = []
    
    for i in range(len(pontos)):
        x1, y1 = pontos[i]
        x2, y2 = pontos[(i + 1) % len(pontos)]
        
        if y1 == y2:
            continue

        if y1 < y2:
            y_min = y1
            y_max = y2
            x_y_min = x1
        else:
            y_min = y2
            y_max = y1
            x_y_min = x2
    
        dx_dy = (x2 - x1) / (y2 - y1)
        tabela_arestas.append([y_min, y_max, x_y_min, dx_dy])
 
    y_min = min(aresta[0] for aresta in tabela_arestas)
    y_max = max(aresta[1] for aresta in tabela_arestas)
     
    for y_varredura in range(y_min, y_max + 1):
        interseccoes = []
        
        for aresta in tabela_arestas:
            y_min_aresta, y_max_aresta, x_y_min, inv_m = aresta
            
            if y_min_aresta <= y_varredura < y_max_aresta:
                x_intersecao = inv_m * (y_varredura - y_min_aresta) + x_y_min
                interseccoes.append(x_intersecao)
        
        interseccoes.sort()
        
        for i in range(0, len(interseccoes), 2):
            if i + 1 < len(interseccoes):
                x_inicio = round(interseccoes[i])
                x_fim = round(interseccoes[i + 1])
                
                for x in range(x_inicio + 1, x_fim):
                    draw_pixel(x, y_varredura, cor_preenchimento)
                    pygame.event.pump() 
        pygame.time.wait(20)

def preencher_retangulo(x1, y1, x2, y2, cor_preenchimento=(255, 0, 0)):
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    
    for y_varredura in range(y_min + 1, y_max):
        for x in range(x_min + 1, x_max):
            draw_pixel(x, y_varredura, cor_preenchimento)
            pygame.event.pump() 
        pygame.time.wait(20)

def preencher_circunferencia(xc, yc, raio, cor_preenchimento=(0, 255, 0)):
    for y_varredura in range(yc - raio, yc + raio + 1):
        delta = (raio**2 - (y_varredura - yc)**2)
        if delta >= 0:
            x1 = xc - round(math.sqrt(delta))
            x2 = xc + round(math.sqrt(delta))
            for x in range(x1 + 1, x2):
                draw_pixel(x, y_varredura, cor_preenchimento)
                pygame.event.pump() 
        pygame.time.wait(20)

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

def mostrar_menu():
    print("\n" + "="*50)
    print("          SISTEMA DE PREENCHIMENTO POR VARREDURA")
    print("="*50)
    print("1. Pintar Retângulo")
    print("2. Pintar Circunferência")
    print("3. Pintar Polígono A")
    print("4. Pintar Polígono D")
    print("5. Sair")
    print("="*50)
    
    try:
        opcao = int(input("Escolha uma opção (1-4): "))
        return opcao
    except ValueError:
        print("Opção inválida! Digite um número.")
        return 0

def limpar_tela():
    tela.fill((255, 255, 255))
    draw_grid()

if __name__ == '__main__':
    rodando = True
    
    while rodando:
        limpar_tela()
        opcao = mostrar_menu()
        
        if opcao == 1:
            x1,y1 = 50,100
            x2,y2 = 200,175
            
            pontos_retangulo = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
            
            for i in range(len(pontos_retangulo)):
                xa, ya = pontos_retangulo[i]
                xb, yb = pontos_retangulo[(i + 1) % len(pontos_retangulo)]
                linha_bresenham(xa, ya, xb, yb, (0, 0, 255))
            
            pygame.time.wait(100)
 
            start_time = time.time()
            preencher_retangulo(x1, y1, x2, y2, (255, 0, 0))
            end_time = time.time()
            print(end_time - start_time)
            
        elif opcao == 2:
            try:
                raio = int(input("Digite o raio da circunferência (5-25): "))
                if raio < 5 or raio > 25:
                    print("Raio deve ser entre 5 e 15!")
                    continue
                    
                centro_x, centro_y = 90, 50
                
                circunferencia_bresenham(centro_x, centro_y, raio, (0, 0, 255))
                pygame.time.wait(100)
                
                start_time = time.time()
                preencher_circunferencia(centro_x, centro_y, raio, (0, 255, 0))
                end_time = time.time()
                print(end_time - start_time)
                
            except ValueError:
                print("Raio inválido!")
                
        elif opcao == 3:
            pontos_poligono = [
                    (50, 50),
                    (200, 80),
                    (210, 135),
                    (110, 210),
                    (40, 150),
                    (90, 125)
                ]
            
            for i in range(len(pontos_poligono)):
                x1, y1 = pontos_poligono[i]
                x2, y2 = pontos_poligono[(i + 1) % len(pontos_poligono)]
                linha_bresenham(x1, y1, x2, y2, (0, 0, 255))
            
            pygame.time.wait(100)
            
            start_time = time.time()
            algoritmo_varredura(pontos_poligono, (255, 255, 0))
            end_time = time.time()
            print(end_time - start_time)
            
        elif opcao == 4:
            pontos_poligono = [
        (75, 75),
        (35, 115), 
        (75, 155),
        (115, 115),
        (135, 135),
        (155, 115),
        (195, 155),
        (235, 115),
        (195, 75),
        (155, 115),
        (135, 95),
        (115, 115)
    ]
            
            for i in range(len(pontos_poligono)):
                x1, y1 = pontos_poligono[i]
                x2, y2 = pontos_poligono[(i + 1) % len(pontos_poligono)]
                linha_bresenham(x1, y1, x2, y2, (0, 0, 255))
            
            pygame.time.wait(100)
            
            start_time = time.time()
            algoritmo_varredura(pontos_poligono, (255, 255, 0))
            end_time = time.time()
            print(end_time - start_time)
            
        elif opcao == 5:
            print("Saindo...")
            rodando = False
        
        if opcao != 5:
            input("Pressione Enter para continuar...")
    
    pygame.quit()
