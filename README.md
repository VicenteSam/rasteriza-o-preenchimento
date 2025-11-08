# 📊 Relatório Comparativo: Algoritmos de Computação Gráfica

![Python](https://img.shields.io/badge/Python-3.12.3-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.6.1-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Uma análise comparativa abrangente dos principais algoritmos de rasterização e preenchimento em computação gráfica, implementados em Python com Pygame.

## 🎯 Objetivo

Comparar o desempenho, qualidade visual e eficiência computacional de diferentes algoritmos gráficos através de métricas quantitativas e análise qualitativa.

## 🚀 Algoritmos Implementados

### 📈 Algoritmos de Linha
- **Analítico** (Equação da reta)
- **DDA** (Digital Differential Analyzer)
- **Bresenham** (Otimizado para inteiros)

### ⭕ Algoritmos de Circunferência
- **Incremental Simétrico**
- **Paramétrico** (Equações trigonométricas)
- **Bresenham** (Otimizado)

### 🎨 Algoritmos de Preenchimento
- **Flood Fill**
- **Varredura** (Scanline)

## 📋 Métricas de Avaliação

- ⏱️ **Tempo de execução** (milissegundos)
- 👁️ **Qualidade visual** (análise qualitativa)
- 🔢 **Número de iterações/pixels**
- 🎯 **Precisão e casos de uso**

## 🏆 Resultados Destacados

### 🥇 Melhores Algoritmos por Categoria

| Categoria | Algoritmo Vencedor | Justificativa |
|-----------|-------------------|---------------|
| **Linhas** | **Bresenham** | Elimina operações float, maior precisão, funciona em todos os octantes |
| **Circunferências** | **Bresenham** | Mais eficiente, sem operações float, usa estratégia de ponto médio |
| **Preenchimento** | **Varredura** | Mais rápido e robusto, lida com formas complexas sem erros |

### 📊 Performance - Tempos Médios

**Linhas (49px):**
- Analítico: 1.3838 ms
- DDA: 1.3839 ms  
- Bresenham: 1.3838 ms

**Circunferências (r=24):**
- Incremental: 0.6767 ms
- Paramétrico: 5.9704 ms ❌
- Bresenham: 0.6509 ms ✅

**Preenchimento (Retângulo):**
- Flood Fill: 8.3588 ms
- Varredura: 1.8967 ms ✅

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12.3
- **Biblioteca Gráfica:** Pygame 2.6.1
- **Hardware:** i5-11400, 16GB RAM, GPU 3060 Ti
- **Resolução:** 1000×1000 pixels


## 🔍 Principais Conclusões

1. **Bresenham é imbatível** para rasterização de primitivas
2. **Algoritmos com operações float** são significativamente mais lentos
3. **Varredura supera Flood Fill** em cenários complexos
4. **Otimizações matemáticas** impactam diretamente na performance

## 📈 Gráficos e Visualizações

O relatório inclui comparações visuais detalhadas mostrando:
- Linhas em diferentes ângulos (45°, acima e abaixo)
- Circunferências com diferentes raios
- Preenchimento de formas simples e complexas
- Análise qualitativa da qualidade do desenho
