import pygame, random

# Inicialização da fonte
pygame.font.init()

# Dimensões da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Quantidade de quadradinhos iniciais:
quadrados_iniciais = 20

# Outras inicializações:
tempo_inicial = 10  # 10 segundos
terminou = False
preto = (0, 0, 0)
branco = (255, 255, 255)


# Criando classe Quadradinho: serve para organizar a estrutura do programa
class Quadradinho():
    def __init__(self):
        self.largura = 30
        self.altura = 30
        self.x = random.randint(0, largura_tela - self.largura)
        self.y = random.randint(20, altura_tela - self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)

# Para imprimir o texto com o tempo e a pontuação final
def mostra_tempo(tempo, pontos):
    font = pygame.font.Font(None, 24)
    text = font.render("Tempo: " + str(tempo) + "s | Pontuação: " + str(pontos), 1, branco)
    textpos = text.get_rect(centerx=tela.get_width() / 2)
    tela.blit(text, textpos)


# Mostra a tela final com a pontução obtida. Representa o placar final.
def mostra_pontuacao_final(tela, pontos):
    tela.fill(preto)  # Limpa tela
    font = pygame.font.Font(None, 36)
    text = font.render("Pontuação: " + str(pontos) + " quadradinhos", 1, branco)
    textpos = text.get_rect(center=(tela.get_width() / 2, tela.get_height() / 2))
    tela.blit(text, textpos)


# Início do programa:

# Desenhar os quadradinhos iniciais
lista = []
for i in range(0, quadrados_iniciais):
    q = Quadradinho()
    q.desenha(tela)
    lista.append(q)

# Indica o relogio de aparecimento de quadros do jogo
clock = pygame.time.Clock()

# Variavel para contar quantas esperas de 50Hz ou 0,02s
conta_clocks = 0

# Conta quantos quadradinhos clicou
pontos = 0

# Variavel para contar regressivamente os quantos segundos se passaram
conta_segundos = tempo_inicial

while not terminou:

    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        # Clicando...
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Obtem as coordenadas do mouse na tela
            pos = pygame.mouse.get_pos()

            # Checa se clicou em algum dos quadrados
            for q in lista:
                if q.area.collidepoint(pos):
                    lista.remove(q)
                    pontos = pontos + 1

        if event.type == pygame.QUIT:
            terminou = True

    conta_clocks = conta_clocks + 1

    # A cada 50 cont_clocks, temos 1s (0,02s x 50 = 1s)
    if conta_clocks == 50:
        if conta_segundos >= 0:
            conta_segundos = conta_segundos - 1
        conta_clocks = 0
        # Cria um novo quadradinho a cada segundo
        q = Quadradinho()
        lista.append(q)

    if conta_segundos >= 0:  # Neste caso, ainda tem tempo
        # Limpar tela para atualizar o texto
        tela.fill(preto)
        # Como a tela foi apagada,vamos desenhar os quadrados novamente
        for i in lista:
            i.desenha(tela)
            # Mostra o tempo atualizado
        mostra_tempo(conta_segundos, pontos)
    else:  # Acabou o tempo de 10s
        # Exibe a tela final
        mostra_pontuacao_final(tela, pontos)
        # Vamos remover todos os quadrados da lista
        for q in lista:
            lista.remove(q)

            # Atualiza o desenho na tela
    pygame.display.update()

    # Configura 50 atualizações de tela por segundo
    clock.tick(50)

# Finaliza a janela do jogo
pygame.display.quit()